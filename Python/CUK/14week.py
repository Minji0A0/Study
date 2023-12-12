
# 클래스 실습
#은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.



```
은행이름: SC은행
계좌번호: 111-11-111111
```


import random

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'

        self.account_number = num1 + '-' + num2 + '-' + num3

kim = Account("김덕수",100)
print("계좌 이름 =",kim.name)
print("계좌 잔액 =",kim.balance)
print("은행 이름 =",kim.bank)
print("계좌 번호 =",kim.account_number)
#클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.
import random

class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count +=1

kim = Account("김덕수",100)
hong = Account("홍길동",200)
lee = Account("이사일",200)

print("생성된 계좌의 개수: ", Account.account_count)
#Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.


import random

class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count +=1

    def get_account_num(self):
        print(Account.account_count)

kim = Account("김덕수",100)
hong = Account("홍길동",200)
lee = Account("이사일",200)

kim.get_account_num()

#입금 메서드  Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.
import random

class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count +=1

    def get_account_num(self):
        print(Account.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
        else:
            print("1원 이상을 입금해야 합니다.")

kim = Account("김덕수",100)
kim.deposit(200)

print(kim.balance)

#출금 메서드 Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.
import random

class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count +=1

    def get_account_num(self):
        print(Account.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
        else:
            print("1원 이상을 입금해야 합니다.")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("계좌에 돈이 모자랍니다.")

kim = Account("김덕수",100)

kim.withdraw(50)
print(kim.balance)
#Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.



```
은행이름: SC은행
예금주: 파이썬
계좌번호: 111-11-111111
잔고: 10,000원
```


import random

class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "sc은행"

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count +=1

    def get_account_num(self):
        print(Account.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
        else:
            print("1원 이상을 입금해야 합니다.")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("계좌에 돈이 모자랍니다.")

    def display_inf(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", "{:,}".format(self.balance),"원")

kim = Account("김덕수",10000000)
kim.display_inf()
#이자 지급하기  입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.
import random

class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "sc은행"
        self.deposit_count = 0

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count +=1

    def get_account_num(self):
        print(Account.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
        else:
            print("1원 이상을 입금해야 합니다.")

        self.deposit_count +=1
        if self.deposit_count % 5 == 0:
            self.balance = self.balance * 1.01

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("계좌에 돈이 모자랍니다.")

    def display_inf(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", "{:,}".format(self.balance),"원")

kim = Account("김덕수",10000000)

kim.deposit(10000000)
kim.deposit(10000000)
kim.deposit(10000000)
kim.deposit(10000000)
kim.deposit(10000000)
kim.deposit(10000000)

print(kim.balance)

#Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.
import random

class Account:
    account_count = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "sc은행"
        self.deposit_count = 0

        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'

        self.account_number = num1 + '-' + num2 + '-' + num3
        Account.account_count +=1

    def get_account_num(self):
        print(Account.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
        else:
            print("1원 이상을 입금해야 합니다.")

        self.deposit_count +=1
        if self.deposit_count % 5 == 0:
            self.balance = self.balance * 1.01

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("계좌에 돈이 모자랍니다.")

    def display_inf(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", "{:,}".format(self.balance),"원")

kim = Account("김덕수",100)
hong = Account("홍길동",200)
lee = Account("이사일",200)

account_data = []
account_data.append(kim)
account_data.append(hong)
account_data.append(lee)

print(account_data)

for i in account_data:
    i.display_inf()
#반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.
#입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.
# 모듈 및 패키지 실습
## pandas 패키지 이해하기 출처: 나무위키(https://namu.wiki/w/pandas)
### **Pandas란?**<br>

#판다스(pandas)는 파이썬 언어로 작성된 데이터를 분석 및 조작하기 위한 소프트웨어 라이브러리이다. 판다스는 수치형 테이블과 시계열 데이터를 조작하고 운영하기 위한 데이터를 제공하는데, 3조항 BSD 라이선스 조건 하에서 무료로 사용 가능하다. 판다스의 이름은 계량 경제학에서 사용되는 용어인 'PANel DAta'의 앞 글자를 따서 지어졌다. 당연히 실제 동물인 판다와는 아무런 관련이 없지만, 이름이 이름이니만큼 각종 개발 관련 사이트에서 판다 이미지를 활용하여 판다스를 소개하곤 한다.

#판다스는 R에서 사용되던 data.frame 구조를 본뜬 DataFrame이라는 구조를 사용하기 때문에, R의 data.frame에서 사용하던 기능 상당수를 무리없이 사용할 수 있도록 만들었다. 더욱이 파이썬이라는 접근성이 좋은 언어 기반으로 동작하기 때문에 데이터 분석을 파이썬으로 입문하는 사람들이 필수적으로 사용하는 라이브러리가 되었다.


### 판다스 특성
'''
- 통합 인덱싱을 활용한 데이터 조작을 가능하게 하는 데이터프레임(DataFrame) 오브젝트
- 인메모리(in-memory) 데이터 구조와 다양한 파일 포맷들 간의 데이터 읽기/쓰기 환경 지원
- 데이터 결측치의 정렬 및 처리
- 데이터셋의 재구조화 및 피보팅
- 레이블 기반의 슬라이싱, 잘 지원된 인덱싱, 대용량 데이터셋에 대한 서브셋 지원
- 데이터 구조의 칼럼 추가 및 삭제
- 데이터셋의 분할-적용-병합을 통한 GroupBy 엔진 지원
- 데이터셋 병합(merging) 및 조인(joining) 지원
- 저차원 데이터에서의 고차원 데이터 처리를 위한 계층적 축 인덱싱 지원
- date range, 빈도 변환, 이동 창 통계, 이동 창 선형회귀, 날짜 이동 등의 시계열 작업 지원
- 데이터 필터 지원

판다스 라이브러리의 주요 코드는 Python이나 C로 작성되었으며, 퍼포먼스에 최적화되어있다.
'''
### 판다스 dataframe 의 예
import pandas as pd

df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]

df.head(10)


## 증권 데이터 분석하기
#특정 회사명으로 종목 코드 얻는 함수 작성
df = df[['회사명','종목코드']]

display(df.head())

display(df[df['회사명']== '삼성전자'])

# pandas 내부에서 제공하는 query 함수를 이용한 데이터 추출
df.query('회사명 == "SK"')
**회사의 재무 정보 가져오기**
import urllib.request
from bs4 import BeautifulSoup

def get_code(df, company_name):
    code = df[df['회사명']== company_name]['종목코드']
    code = code.to_string(index=False)
    code = code.replace(" ","")
    code = code.zfill(6)
    
    return code

company = ['삼성전자','카카오','LG전자']

stock = {'종목코드':[],'회사명':[],'PER':[],'EPS':[]}
stock_info = pd.DataFrame(stock,columns=['종목코드','회사명','PER','EPS'])

for c in company:
    code =  get_code(df, c)
    url = "http://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?pGB=1&gicode=A"+ code + "&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701"
    f = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(f, 'html.parser')

    # PER 정보 얻기

    per = soup.find('tr', {'id': "p_grid1_9"}).find_all('td')
    per= per[-2]
    per = per.string
    print(c+"의 PER:", per)

    # EPS 정보 엳기
    eps_info = soup.find('tr', {'id': "p_grid1_1"}).find_all('td')
    eps = eps_info[-2]
    eps = eps.string
    print(c+"의 EPS :",eps)
    eps=eps.replace(",","")


    stock['종목코드'] = code
    stock['회사명'] = c
    stock['PER'] = per
    stock['EPS'] = int(eps)

    print(stock)
 
    stock_info = stock_info.append(stock, ignore_index=True)

display(stock_info)

#**최저 PER 종목 찾기**
#PER 가 낮은 종목부터 오름차순으로 정렬하기
sorted_stock_info= stock_info.sort_values(by=['PER','EPS','종목코드','회사명'],ascending=[True, False, False, False])
display(sorted_stock_info)
display(sorted_sotock_info)
