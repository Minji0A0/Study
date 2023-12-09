
# 클래스 생성자

class Country:
    name = '국가명'
    population = '인구'
    capital = '수도'
    calling_code = '국가 전화번호'

    def __init__(self,name,population, capital):
        print("init class")
        self.name = name
        self.population = population
        self.capital = capital

    def show(self):
        print("국가명은 : %s 입니다."%self.name)
        print("인구는 : %s명 입니다."%self.population)
        print("수도는 : %s 입니다." %self.capital)
        print("국가 전화번호는 : %s 입니다." %self.calling_code)
    
#**생성자의 사용**
#생성자 parameter 개수를 맞추지 못할 경우--- 에러 발생!!!
korea = Country()

#생성자 parameter 규칙을 맞추며 클래스 객체화
korea = Country("대한민국",50000000,"서울")
korea.show()
korea.calling_code = 82
korea.show()

# 클래스 상속
#클래스 상속 및 정의
class Korea(Country):
    independence_fighter = []
  
    def add_independence_fighter(self, name):
        self.independence_fighter.append(name)

    def show_independence_fighter(self):
        print(self.independence_fighter)

    def show(self):     # 메서드 오버라이딩
        super().show()
        print("우리나라의 독립운동가 : ",self.independence_fighter)

        a = Korea("대한민국",50000000,"서울")
a.add_independence_fighter("유관순")
a.show()

#생성자 함수의 오버라이딩
class Korea(Country):
    independence_fighter = []
  
    def __init__(self):
        self.name = "대한민국"
        self.population = 50000000
        self.capital = "서울"

    
    def add_independence_fighter(self, name):
        self.independence_fighter.append(name)

    def show_independence_fighter(self):
        print(self.independence_fighter)

    def show(self):     # 메서드 오버라이딩
        super().show()
        print("우리나라의 독립운동가 : ",self.independence_fighter)


a = Korea()
a.add_independence_fighter("유관순")
a.add_independence_fighter("안중근")
a.show()

class USA(Country):
    state = []

    def __init__(self):
        self.name = "미국"
        self.population = 900000000
        self.capital = "Washington"

    def add_state(self, state):
        self.state.append(state)

    def show(self):
        super().show()

a = USA()
a.show()        
