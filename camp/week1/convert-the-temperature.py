class Solution(object):
    def convertTemperature(self, celsius):
        f = celsius*1.80+32.00
        k = celsius+273.15

        return [k,f]
        