# 숫자형 Data Type


#**정수형 데이터 타입**
a = 1    
print("a = ",a)
print(type(a))     # a의 data type을 확인해 보면, int type이라는 것을 확인할 수 있음
b = -178
print("b = ",b) 
print(type(b))     # b의 data type을 확인해 보면, int type이라는 것을 확인할 수 있음


#**실수형 데이터 타입**
a = 1.2
print("a = ",a)       
print(type(a))           # a의 data type을 확인해 보면, float type이라는 것을 확인할 수 있음

b = 4.24E10
print("b = ",b)
print(type(b))          # b의 data type을 확인해 보면, float type이라는 것을 확인할 수 있음

#**8진수(octal)**
a= 0x177            # a를 8진수로 입력
print(a)            # a를 10진수로 출력

b = 0x8ff          # b를 16진수로 입력
print(b)           # b를 10진수로 출력


#**사칙 연산이 포함된 숫자**
a = 3
b = 4

print ("a+b = ",a+b)           # 더하기 연산
print ("a*b = ",a*b)           # 곱하기 연산
print ("a/b = ",a/b)           # 나누기 연산
print ("a**b = ",a**b)         # 누승 연산
print ("a//b = ",a//b)
print ("a%b = ",a%b)


# 문자열 자료형
# 문자열 자료형의 다양한 표현 방법
print("Hello Wolrd")       # " " 큰 따옴표로 감싸는 문자열
print('Hello Wolrd')       # ' ' 작은 따옴표로 감싸는 문자열
print("""
      python is fun       
      """ )                # """ 큰 따옴표 3개로 감싸는 문자열
print('''
      Life is too short, You need python       
      ''' )                # ''' 작은 따옴표 3개로 감싸는 문자열


#**문자열에서 줄바꿈을 표현하는 방법**

multiline = "Life is too short\n You need python"     # \n 기호는 줄바꿈을 의미한다.
print(multiline)
multiline = """
Life is too short
You need python
"""                                 # """ 기호는 문자열의 줄바꿈을 인식하여 데이터를 저장
print(multiline)
multiline = '''
Life is too short
You need python
'''                                 # ''' 기호는 문자열의 줄바꿈을 인식하여 데이터를 저장
print(multiline)


#**문자열 연산**

head = "python"
tail = " is fun"
print(head + tail)    # 문자열 연결하기
print(head * 3)      # 문자열 곱하기
a = "life is too short"
len(a)                    # 문자열 길이 구하기


#**문자열 인덱싱**
a = "Life is tooshort, You need python"
print(a[0],a[1],a[2],a[3],a[4])  # 문자열의 인덱싱 접근
print(a[-1],a[-2])    # 문자열 인덱싱을 -1로 접근
print(a[0:4])    # 문자열 슬라이싱

a = "20010331Rainy"
print(a[:8])    #  처음부터 8 전까지의 문자열을 뽑아냄
print(a[8:])    #  8부터 끝까지의 문자열을 뽑아냄


#**문자열 formatting**

print("I eat %d apples"%3)    # %d는 10진수를 나타냄, 문자열 뒤에 숫자형 %3이 %d에 대치되어 표현
number = 3
print("I eat %d apples"%number)  # %d는 decimal을 의미한다. 문자열 뒤에 %number 숫자형 변수를 %d에 대입해 문자열에 숫자로 나타낼 때 쓰인다.
str_five = "five"
print("I eat %s apples"%str_five)   # %s 는 string을 의미한다. 문자열 뒤에 %str_five 문자열 변수를 넣어 문자열 안에 %s 에 대입되도록 한다.

num = 10
day = "three"
print("I ate %d apples, so I was sick for %s days."%(num,day))

print("I have %c apples" %'2')
print("rate is %f" % 3.21)



#**정렬과 공백**
# %s를 숫자와 함께 사용하면, 공백과 정렬 표현 가능

print("%10s"%"hi")
print("%-10sjane"%"hi")

# 소수점 표현하기 
print("%0.4f"% 3.42134234)      # 소수점 4자리까지 표현

name = '홍길동'
age = 30
print(f'나의 이름은 {name} 입니다. 나이는 {age+1} 입니다.')    # f 문자열 formatting

# **문자열 자료형 관련 함수**
a = 'hobby'     
a.count('b')    # count 함수

a = ','.join('1231414214513414a')   # join 함수수
print(a)

a = "python is best choice"

print(a.find('b'))       # b 의 위치를 반환
print(a.find('k'))       # k 의 위치를 반환, k가  없으므로 -1이 반환됨됨


a = 'hi'
print(a.upper())   # 소문자를 대문자로 변환
b = 'HI'
print(b.lower())   # 대문자를 소문자로 변환


a = "Life is too short"
a.replace("Life","Your leg")   # replace() 함수를 이용하여 특정 값을 다른 값으로 치환하기기

a = "Life is too short"
print(a.split())    # 공백을 기준으로 문자열을 나눔


b = "a:b:c:d"
print(b.split(':')) # :기호를 기준으로 문자열을 나눔


# 리스트 자료형
#**리스트 자료형의 정의**

# 리스트 안에 어떠한 자료형도 포함 가능
a = []
b = [1,2,3,4]
c = ['Life','is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1,2,['Life', 'is']]

e [2]      # 리스트는 인덱스를 통해 접근 가능함
d[-1]     # 인덱스 -1은 마지막 요솟값을 가르킴
b[0] + b[2]     # 리스트 요솟값 간의 덧셈셈

b[0] = 100    # 리스트 요소값을 수정하기
print(b)

del b[3]     # del 키워드로 리스트 요소 삭제하기기


b.append(50)   # append 내장함수로 리스트 맨 마지막에 50을 추가
b

b.index(50)    # 요소를 검색하여 위치를 반환

b.sort()      # 리스트의 요소를 순서대로 정렬.sort()      # 리스트의 요소를 순서대로 정렬
b

b.reverse()     # 리스트를 역순으로 뒤집어줌
b

b.insert(1,4)      # 리스트에 요소 삽입,   인덱스 1 자리에 4를 삽입
b

b.remove(100)   # 리스트에서 첫번째로 나오는 데이터를 삭제
b

b.extend([5,6,7,8,])   # 리스트 확장하기
b
