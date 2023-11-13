a = 10
b = "python"
c = 1.34

print("a: %d  b: %s c:%.2f" %(a,b,c))

# 변수의 데이터 타입 확인
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))



#1apple = 200     #변수의 첫 문자로는 숫자가 올 수 없다.
#if = 10      # 파이썬의 키워드를 변수명으로 사용할 수 없다.

Apple = 10    # 변수명의 첫문자로 대문자가 올 수는 있으나, 권장하지는 않는다.
print(Apple)


a = 10
b = 3

c = a+b                      # 더하기 연산
print("a+b : c =%d "%c)

c = a-b                      # 빼기 연산
print("a-b : c =%d "%c)

c = a*b                      # 곱하기 연산
print("a*b : c =%d "%c)

c = a/b                      # 나누기 연산
print("a/b : c =%f "%c)     

c = a//b                    # 정수 몫
print("a//b : c =%d "%c)

c = a//b                    # 나머지 연산
print("a%%b : c =%d "%c)

c = a**b                      # 누승 연산
print("a**b : c =%d "%c)



# **산술 연산자의 적용**

cola = 2000    # 콜라 하나의 가격 
nCola = 2         # 콜라 구매 개수
hamburger = 1000    #햄버거 하나의 가격
nHamburger = 1      #햄버거 구매 개수
discount = 0.1     # 통신사 할인율
total = (cola*nCola+hamburger*nHamburger)*(1-discount)
print("total = %d"%total)


nCola = 2000         #콜라 재고 개수
nEvent = nCola // 3    # 2+1 이벤트 가능한 횟수
print("이벤트 가능한 횟수 : %d "%nEvent)
N_lack_cola = 3-(nCola % 3)    #  2+1 이벤트를 하기 위해 채워야 하는 콜라 개수
print("이벤트를 하기위해 채워야 하는 개수: %d "%N_lack_cola)



# **관계 연산자**

age = 10
print("주류 판매가 가능한가요?",20<=age)    # False
age = 20
print("주류 판매가 가능한가요?",20<=age)    # True


# **논리 연산자**
year_of_birth = 77
end_number = year_of_birth % 10 
end_number == 2  or end_number == 7          # True


# 복합대입 연산자
a+=10

# 편의점에서의 바코드 스캐닝을 통한 누적 금액 계산
total = 0
cola = 1000
hamburger = 2000
milk = 1500

## 바코드 스캐닝 시작
total += cola
total += hamburger
total += milk                      # total = total+cola+hamburger+milk

total



# 연산자 우선 순위

# 햄버거 2개, 콜라 1개 – 10% 할인 적용
scola = 2000    #햄버거 하나의 가격
nCola = 2         #햄버거 구매 개수
hamburger = 1000    # 콜라 하나의 가격
nHamburger = 1        # 콜라 구매 개수
discount = 0.1     # 통신사 할인율
total = (cola*nCola+hamburger*nHamburger)*(1-discount)
print("total = %d"%total)
