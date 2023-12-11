# 변수 및 데이터 타입

#문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"  #형변환
num_int = int(num_str)
print(num_int+1, type(num_int))

#정수 100을 문자열 '100'으로 변환해보세요.
num = 100
result = str(num)
print(result, type(result))

#문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
data = "15.79"
data = float(data)
print(data, type(data))

#letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'

lang = 'python'
print(lang[0], lang[2])

#자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
 license_plate = "24가 2210"

 
license_plate = "24가 2210"
실행 예: 2210
 

license_plate = "24가 2210"
print(license_plate[-4:])
#변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.



```
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

이름: 김민수 나이: 10
이름: 이철희 나이: 13
```


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))


#2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
 
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
#다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)



```
nums = [1, 2, 3, 4, 5, 6, 7]
실행 예:
max:  7
min:  1
```


nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))
다음 리스트의 평균을 출력하라.



```
nums = [1, 2, 3, 4, 5]
실행 예:
3.0
```


nums = [1, 2, 3, 4, 5]

average = sum(nums) / len(nums)
print(average)

sum = 0
n = 0
for i in nums:
    sum += i
    n +=1

print(sum,n)


#회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.



```
string = "삼성전자/LG전자/Naver"
실행 예시
>> print(interest)
['삼성전자', 'LG전자', 'Naver']
```


string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)
#아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.

inventory = {"메로나": [300, 20], 
             "비비빅": [400, 3], 
             "죠스바": [250, 100]}
print(inventory)
#inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.



```
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

실행 예시:
20 개        
```


print(inventory["메로나"][1], "개")
inventory 딕셔너리에서 죠스바의 가격을 화면에 출력하라.


print(inventory["죠스바"][0], "원")
#  분기문 및 반복문
사용자로부터 입력받은 문자열을 두 번 출력하라. 아래는 사용자가 "안녕하세요"를 입력한 경우의 출력 결과이다.



```
>> 안녕하세요
안녕하세요안녕하세요
```


user = input("입력:")
print(user * 2)
사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.



```
>> 30
짝수
```


user = input("")
if int(user) % 2 == 0:
    print("짝수")
else:
    print("홀수")
#우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.



```
>> 우편번호: 01400
도봉구
```



우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")
#주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라.

![Cap 2021-05-16 18-40-24-272.jpg](data:image/jpeg;base64,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)
주민번호 = input("주민등록번호: ")
뒷자리 = 주민번호.split("-")[1]
if 0 <= int(뒷자리[1:3]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")
#아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.



```
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
```


#btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.


 
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
#리스트에는 동물이름이 문자열로 저장돼 있다.
리스트 = ['dog', 'cat', 'parrot']



```
dog 3
cat 3
parrot 6
```


리스트 = ['dog', 'cat', 'parrot']
for 이름 in 리스트:
  print(이름, len(이름))
#리스트에서 대문자만 화면에 출력하라.



```
리스트 = ["A", "b", "c", "D"]
A
D
```



```
>> 변수 = "A"
>> 변수.isupper()
True
>> 변수 = "a"
>> 변수.isupper()
False

```


리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트:
  if 변수.isupper():
    print(변수)
#1부터 30까지의 숫자 중 3의 배수를 출력하라.
 
for num in range(3, 31, 3):
    print (num)
#리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.



```
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
```


volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])
#함수 관련
#하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.



```
print_even ([1, 3, 2, 10, 12, 11, 15])
2
10
12
```


def print_even (my_list) :
    for v in my_list :
        if v % 2 == 0 :
            print(v)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})



```
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

이름
나이
성별
```


def print_keys(dic):
    for keys in dic.keys():
        print(keys)
#문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.



```
make_url("naver")
www.naver.com
```


def make_url(string) :
    url = "www." + string + ".com"
    return url
def make_url(string) :
    return "www." + string + ".com"
#문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.



```
make_list("abcd")
['a', 'b', 'c', 'd']
```


def make_list (string) :
    my_list = []
    for 변수 in string :
        my_list.append(변수)
    return my_list
def make_list (string) :
    return list(string)
#숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.




```
pickup_even([3, 4, 5, 6, 7, 8])
[4, 6, 8]
``

def pickup_even(items):
    result = []
    for item in items:
        if item % 2 == 0:
            result.append(item)
    return result
