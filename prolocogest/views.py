from pyramid.view import view_config
import prolocogest.rapporto
import subprocess
import sys
from prolocogest.connect import Connect
import pymysql.cursors
from prolocogest.classPdf import Pdf
con = pymysql.connect(host='carlozanieri.net', user='root',password='trex39', db='prolocogest', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
cur = con.cursor()
cur.execute("SELECT * FROM menu where attivo = 1 and livello = 2")

menus = cur.fetchall()

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'prolocogest'}
@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {'project': 'ProlocoGest', 'menus': menus}

@view_config(route_name='compose', renderer='templates/compose.jinja2')
def compose(request):
    return {'project': 'ProlocoGest', 'menus': menus}

@view_config(route_name='Rapporto')
def Rapporto(request):
    return subprocess.Popen([sys.executable, 'prolocogest/rapporto-class.py'])
