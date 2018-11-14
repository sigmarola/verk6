import bottle
from bottle import *
import datetime
from sys import argv
items=['s1','s2','s3','s4','s5','s6']
vorur=['','','']
v1 = ''
v2 = ''
v3 = ''
@route('/')
def index():

    ts = datetime.datetime.now() + datetime.timedelta(days=365)

    if request.query.item in items:
        global vorur
        vara = request.query.item
        a=1
        vorur.insert(0,vara)
        #vorur.append(vara)
        vorur=vorur[0:3]
        response.set_cookie("vara1", vorur[0],expires=ts)
        if vorur[1] != '':
            response.set_cookie("vara2", vorur[1],expires=ts)
            if vorur[2] != '':
                response.set_cookie("vara3", vorur[2],expires=ts)
        print(vorur)
        return redirect('/val')
    else:
        return template('index.tpl',v1='',v2='',v3='')

@route('/val')
def val():
    v1 = request.get_cookie("vara1")
    v2 = request.get_cookie("vara2")
    v3 = request.get_cookie("vara3")
    valin_vara = request.get_cookie("vara")
    return template('index.tpl',v1=v1,v2=v2,v3=v3)
@route('/static/<skra:path>')
def static_skra(skra):
    return static_file(skra, root='./public/')
vorur.reverse()
bottle.run(host='0.0.0.0', port=argv[1])
