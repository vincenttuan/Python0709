# def 自帶參數
def printBMI(h, w):
    bmi = w / ((h/100)**2)
    print("%.2f" % bmi)

printBMI(170, 60)
printBMI(180, 70)
printBMI(160, 50)
