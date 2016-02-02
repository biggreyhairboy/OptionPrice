import math

class pyoptioncalculator:
    riskfreerate = 0.01
    hodiday = 245
    days = 90
    vol = 0.2 #  14%
    def __init__(self):
        pass


    def GBSMandGreeks(self, underlyingprice, longshort, callput, stikeprice, vol,
                      voldays, rate, ratedays):
        if callput == 'call':
            optprice = 999
            return optprice
        elif callput == 'put':
            optprice = 888


    @classmethod
    def GBSMtest(self):
        return 999











