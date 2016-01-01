# Create your views here.
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import MySQLdb

import  datetime
def hello(request):
    return HttpResponse("hello mysite")

def homepage(request):
    return HttpResponse("This is default home page")

def systime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def optionpricemain(request):
    #return render_to_response('PriceMainPage.html', {'AgPrice': '2000'})
    db = MySQLdb.connect(user= 'root', db= 'vol', passwd = '223223', host = '127.0.0.1')
    cursor = db.cursor()
    cursor.execute('select Price from InstrumentVol')
    price = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('PriceMainPage.html', {'AgPrice': price[0]})

    #o = get_template('PriceMainPage.html')
    #html = o.render(Context({'Ag1606Price': price}))
    #return HttpResponse(html)
