# -*- coding:utf-8 -*-
import os
from jinja2 import Environment, FileSystemLoader
import codecs
import shutil
import json
from markdown import Markdown
from datetime import datetime

env = Environment (
    loader = FileSystemLoader("templates")
)

Path_md = 'Markdowns/'
Path_Out_Articles = 'Articles/'
Path_Out_Pages = 'Pages/'
Index_DAT = 'index.dat'
Index_Articles = [];
dict_Articles = {}
list_MD_FILES = []

def InitGlobal():
    global Index_Articles, dict_Articles, list_MD_FILES,maxcap,maxp
    Index_Articles = []
    dict_Articles = {}
    list_MD_FILES = []
    maxcap = 17

def clean():
    if os.path.exists(Path_Out_Articles):
        shutil.rmtree(Path_Out_Articles)
    InitGlobal()

def load_md_files(folder):
    global list_MD_FILES
    for root, dirs, files in os.walk(folder):
        for f in files:
            if os.path.splitext(f)[1].lower() == '.md':
                list_MD_FILES.append(os.path.join(root,f)) 

def load_md_Index():
    global dict_Articles
    with codecs.open('index.json') as file:
        jsonCode = file.read()    
    dict_Articles = json.loads(jsonCode)
				
def scan_md():
    global Index_Articles, list_MD_FILES
    for mdfile in list_MD_FILES:
        file_base_name = os.path.splitext(os.path.basename(mdfile))[0]
        Index_Articles.append({'index':file_base_name, 'filepath':mdfile})

def check_need_render(article):
    global dict_Articles
    if article['index'] not in dict_Articles.keys():
        return True    
    last_modify_date = parse_time(os.path.getmtime(article['filepath']))
    index_modify_date = dict_Articles[article['index']].get('modify_date')
    if last_modify_date == index_modify_date:
        return False
    else:
        return True	
		
def gen_md_html():
    global dict_Articles
    for article in Index_Articles:
	    if check_need_render(article):
	        html = render_html(article)
	        save_html(dict_Articles[article['index']].get('savepath'), html)

def render_pages_html(num):
    global maxp, maxcap
    global dict_Articles
    Sindex = [];
    Eindex = [];
    urlstr = '/Pages/{0}.html'
    if maxp <= 17:    
        for i in range(1,num):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        for i in range(num+1,maxp+1):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
    elif num <= 9:
        for i in range(1,num):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        for i in range(num+1,maxcap - 3):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
        Eindex.append({'url': str.format(urlstr, num+5) ,'tags': '...' })
        for i in range(maxp-2,maxp+1):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
    elif num <= maxp-8:
        for i in range(1,4):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        Sindex.append({'url': str.format(urlstr, num-5) ,'tags': '...' })
        for i in range(num-4,num):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        for i in range(num+1,num+5):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
        Eindex.append({'url': str.format(urlstr, num+5) ,'tags': '...' })
        for i in range(maxp-2,maxp+1):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
    else:
        for i in range(1,4):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        Sindex.append({'url': str.format(urlstr, num-5) ,'tags': '...' })
        for i in range(maxp-maxcap + 5,num):
            url = str.format(urlstr,i)
            Sindex.append({'url': url ,'tags': i })
        for i in range(num+1,maxp+1):
            url = str.format(urlstr,i)
            Eindex.append({'url': url ,'tags': i })
    prepage = str.format(urlstr, num if num == 1 else num-1)
    nextpage= str.format(urlstr, num if num == maxp else num + 1)
    currentdata = []
    if num <= maxp:
        for lst in range((num-1)*10, min((num-1)*10 + 10, len(dict_Articles))):            
            currentdata.append(dict_Articles.items()[lst][1]);   
    template = env.get_template("articlelist_tem.html")
    html = template.render(Sindex = Sindex, current = num,Eindex = Eindex,PP = prepage, NP = nextpage, Content = currentdata)
    return html

def render_html(article):
    print article
    with codecs.open(article['filepath'], 'r', 'utf-8') as mdfile:
        mdtxt = mdfile.read()
        md = Markdown(
            extensions=[
                "fenced_code",
                "codehilite(css_class=highlight,linenums=None)",
                "meta",
                "admonition",
                "tables",
                "toc",
                "wikilinks",
            ],
        )
        md_html = md.convert(mdtxt)
        meta = md.Meta if hasattr(md, "Meta") else {}
        toc = md.toc if hasattr(md, "toc") else ""
        meta = md.Meta if hasattr(md, 'Meta') else {}
        create_index(article, meta)
        template = env.get_template("article_base.html")
        html = template.render(
            titlename = dict_Articles[article['index']].get("title"),
            txtcontent = md_html
            )
        return html

def create_index(article, meta):    
    title = meta.get('title',[''])[0]
    if title == "":
        title = article['index']
    publish_date = parse_time(os.path.getctime(article['filepath']))
    modify_date = parse_time(os.path.getmtime(article['filepath']))
    summary = meta.get('summary', [''])[0]
    dict_Articles[article['index']] = {
        'title'        : title,
        'publish_date' : publish_date,
		'modify_date'  : modify_date,
        'summary'      : summary,
        'filepath'     : article['filepath'],
        'url'          : str.format('/Articles/{0}.html',article['index']),
        'savepath'     : str.format('Articles/{0}.html',article['index']),
        "tags"         : meta.get("tags", [])
        }
 
def parse_time(timestamp, pattern="%Y-%m-%d %H:%M:%S"):
    return datetime.fromtimestamp(timestamp).strftime(pattern)           

def save_html(out_path, html):    
    base_folder = os.path.dirname(out_path)
    if not os.path.exists(base_folder) and base_folder != "":
        os.makedirs(base_folder)
    with codecs.open(out_path, "w+", "utf-8") as f:
        f.write(html)

def dump_index():
    global maxp
    jsoncode = json.dumps(dict_Articles);
    with codecs.open('index.json', 'w+') as f:
        f.write(jsoncode)    
    maxp = len(dict_Articles)/10 + 1

def gen_html_Pages():
    for i in range(1, maxp + 1):
        html = render_pages_html(i)
        save_html(Path_Out_Pages + str.format('{0}.html', i), html)

def gen_html_index():
    template = env.get_template("base.html")
    html = template.render()
    save_html('index.html',html)    

if __name__ == '__main__':
    clean()
    load_md_Index()
    load_md_files(Path_md)
    scan_md()
    gen_md_html()
    dump_index()
    gen_html_Pages()