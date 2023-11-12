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
