import math
from calcutility import *


class pyoptioncalculator:
    riskfreerate = 0.01
    rate = 0.04
    optiondays = 65.0
    yeardays = 365.0
    ratedays = 90.0
    yeartradedays = 245.0
    vol = 0.2 #  14%
    underlyingprice = 3330.0
    def __init__(self):
        pass

    @classmethod
    def GBSMandGreeksBasic(self, longshort, callput,strikeprice):
        print "basic form"
        return pyoptioncalculator.GBSMandGreeks(longshort, callput, strikeprice,self.underlyingprice, self.vol,
                                                self.riskfreerate, self.optiondays, self.yeartradedays, self.ratedays, self.yeardays)

    @classmethod
    def GBSMandGreeks(self, longshort, callput, strikeprice,underlyingprice,  Sigma,
                      DivRf, optiondays, tradedays, ratedays, yeardays):
        S = utility.getLastPrice()
        X = strikeprice
        T1 = 90/245.0
        r = self.rate
        T2 = optiondays / yeardays
        sig = Sigma  #vol need larger than 0.0001
        q = DivRf
        rf = DivRf
        b = 0.0

        d1 = (math.log(S / X) + b * T1 + sig * sig / 2* T2) / (sig * math.sqrt(T2))
        d2 = d1 - sig * math.sqrt(T2)

        if callput == 'call':
            optprice = S * math.exp((b - r) * T1) * utility.normcdf(d1) - X * math.exp(-r * T1) * utility.normcdf(d2)
            return optprice
        elif callput == 'put':
            optprice = X * math.exp((-r) * T1) * utility.normcdf(-d2) - S * math.exp((b - r) * T1) * utility.normcdf(-d1)
            return optprice

    @classmethod
    def GBSMtest(self):
        return 999











