def printBMI(h, w):
    bmi = w / ((h/100)**2)
    if(bmi > 23):
        result = "過重"
    elif(bmi < 18):
        result = "過輕"
    else:
        result = "正常"
    print("身高: %.1f 體重: %.1f BMI: %.2f (%s)" % (h, w, bmi, result))

printBMI(170.5, 60.3)