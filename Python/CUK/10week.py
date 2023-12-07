#**클래스의 정의**

class Cookie:
    pass

#**객체의 생성**
a = Cookie()
b = Cookie()

#**클래스의 구성요소**
class Stock:
    market = "kospi"
    def transaction(self,name):
        self.name = name
        print("사용자의 이름은 %s 입니다."%self.name)

#**객체의 생성 및 메서드의 사용**
a = Stock()

a.transaction("김이박")

#**메서드와 일반 함수의 비교**
def transaction(name):
    my_name = name
    print("사용자의 이름은 %s 입니다."%my_name)

transaction("김이박")

#**클래스 변수와 인스턴스 변수의 개념**
class Stock:
    market = "kospi"
    composite_stock_price = 2000
    def check_market(self):
        print(self.market)
        Stock.composite_stock_price += 1

s1 = Stock()
s2 = Stock()

s1.market = "kosdaq"

s1.check_market()
s2.check_market()

Stock.market = "DowJones"
s1.check_market()
s2.check_market()

#**클래스 변수는 객체간 값이 공유가 가능하다**
print("s1의 종합주가지수 :",s1.composite_stock_price)
print("s2의 종합주가지수 :",s2.composite_stock_price)

#**계산기 클래스 만들기**
class FourCal:
    num = 0
    def setdata(self, first, second):
        FourCal.num += 1
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)

print("a.add() = ",a.add())
print("a.mul() = ",a.mul())
print("a.sub() = ",a.sub())
print("a.div() = ",a.div())
print("b.add() = ",b.add())
print("b.mul() = ",b.mul())
print("b.sub() = ",b.sub())
print("b.div() = ",b.div())
