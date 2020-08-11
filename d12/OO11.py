class Celsius: # 攝氏
    def __get__(self, instance, owner):
        return 5 * (instance.fahrenheit - 32) / 9
    def __set__(self, instance, value):
        instance.fahrenheit = 32 + 9 * value / 5

class Temperature: # 溫度
    celsius = Celsius()  # 內部類別
    def __init__(self, initial_f):
        self.fahrenheit = initial_f # fahrenheit = 華氏

if __name__ == '__main__':
    t = Temperature(212)
    print(t.celsius) # 呼叫 __get__
    t.celsius = 0    # 呼叫 __set__
    print(t.fahrenheit)