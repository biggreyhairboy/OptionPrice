import math
from math import atan, exp
import MySQLdb

class utility:
    def __init__(self):
        pass
    @classmethod
    def normcdf(self, d):
        if d > 10:
            return 1.0
        elif d < -10:
            return 0.0
        return self.boole(-10.0, d, 240)
    @classmethod
    def normpdf(self, d):
        pi = 4.0 * atan(1.0)
        val = exp(-d * d * 0.5) / math.sqrt(2 * pi)
        return val
    @classmethod
    def boole(self, startpoint, endpoint, n):
        sum = 0
        delta_x = (endpoint - startpoint) / (n * 1.0)
        x = []
        y = []
        for i in range(n): #todo: i need start from 0
            tempx = startpoint + i * delta_x
            x.append(tempx)
            y.append(self.normpdf(tempx))

        t = 0
        for t in range((n-1)/4):
            ind = 4*t
            sum += (1 / 45.0) * (14 * y[ind] + 64 * y[ind+1] + 24 * y[ind+2] + 64 * y[ind+3] + 14 * y[ind+4]*delta_x)
        return sum


    @classmethod
    def getTradeDayCount(self):
        pass

    def getDayCount(self):
        pass

    def getRate(self):
        pass

    @classmethod
    def getLastPrice(self):
        db = MySQLdb.connect(user= 'root', db='vol', passwd='223223', host = '127.0.0.1')
        cursor = db.cursor()
        cursor.execute('select Price from InstrumentVol')
        price = [row[0] for row in cursor.fetchall()]
        lasprice = price[0]
        return lasprice



    #todo: calculate greenks