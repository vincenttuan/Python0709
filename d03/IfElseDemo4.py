a = True
b = False
c = True
print(a and b, a and c, a or b, b or c)

score = 70
print(score >= 60 and score % 2 == 0)
print(score >= 60 and score % 2 == 1)
print(score >= 60 or score % 2 == 1)
print(score >= 60 or score % 2 == 1 and score % 2 == 0)
print(score >= 60 and score % 2 == 1 or score % 2 == 0)

x = True
y = False
z = False
if y and x or x:
    print("Yes")
else:
    print("no")
