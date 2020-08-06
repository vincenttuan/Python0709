# 撰寫一個 BMI 系統
# 可以輸入人名, 身高cm, 體重kg
# 系統會算出 BMI 的結果與是否是正常, 過低, 過高
# 資料呈現 : 小明的身高是 170cm 體重是 60 kg BMI 計算結果為 20.76 (正常)
# 資料呈現 : ___的身高是 ___cm 體重是 __ kg BMI 計算結果為 __.__ (____)
print('BMI 系統')
name = input('請輸入姓名: ')
h = float(input('請輸入身高(cm): '))
w = float(input('請輸入體重(kg): '))
bmi = w / ((h/100)**2)
result = '正常' if 18 < bmi <= 23 else '過高' if bmi > 23 else '過低'
print('%s的身高是 %5.1f cm 體重是 %5.1f kg BMI 計算結果為 %5.2f (%s)' %
      (name, h, w, bmi, result))



