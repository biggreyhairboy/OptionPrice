# Create your views here.
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from OptionEngine.optionengine import *
import MySQLdb
import datetime


def hello(request):
    return HttpResponse("hello mysite")


def homepage(request):
    return HttpResponse("This is default home page")
    #return render_to_response('calculator.html')


def systime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def calc(request):
    if(request.method == 'GET'):
        underlying = request.GET['underlying']
        strikeprice = float(request.GET['strikeprice'])
        callput = request.GET['callput']
        longshort = request.GET['longshort']
        quantity = request.GET['quantity']
        res = pyoptioncalculator.GBSMandGreeksBasic(longshort, callput, strikeprice)
        #res = pyoptioncalculator.GBSMtest()

        optionprice =float(quantity) *  res
    #   return render_to_response("calc.html", {'underlying':underlying, 'stikeprice':strikeprice, 'callput':callput,
    #                                          'longshort':longshort, 'quantity':quantity, 'optionprice':optionprice})
        return render_to_response("calc.html", {'optionprice':optionprice})

def optionpricecalculator(request):
    return render_to_response("Calculator.html")


def optionpricemain(request):
    #return render_to_response('PriceMainPage.html', {'AgPrice': '2000'})
    db = MySQLdb.connect(user= 'root', db='vol', passwd='223223', host = '127.0.0.1')
    cursor = db.cursor()
    cursor.execute('select Price from InstrumentVol')
    price = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('PriceMainPage.html', {'AgPrice': price[0]})

    #o = get_template('PriceMainPage.html')
    #html = o.render(Context({'Ag1606Price': price}))
    #return HttpResponse(html)


def ajaxtest(request):
    db = MySQLdb.connect(user= 'root', db='vol', passwd='223223', host = '127.0.0.1')
    cursor = db.cursor()
    cursor.execute('select Price from InstrumentVol')
    price = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('AjaxTestPrice.html', {'ajaxprice': price[0]})