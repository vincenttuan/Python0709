def getBMI(h, w):
    bmi = w / ((h/100)**2)
    if(bmi > 23):
        result = "過重"
    elif(bmi < 18):
        result = "過輕"
    else:
        result = "正常"
    return bmi, result, h, w

bmi, result, h, w = getBMI(170.5, 60.5)
print("身高: %.1f 體重: %.1f BMI: %.2f (%s)" % (h, w, bmi, result))
