import util.MyCalc
import util.MyCalc as m
from util.MyCalc import bmi
if __name__ == '__main__':
    a = 10
    b = 20
    w = 60
    h = 170
    print(util.MyCalc.sub(a, b))
    print(m.add(a, b))
    print(bmi(h, w))