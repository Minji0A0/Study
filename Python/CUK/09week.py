#**함수의 정의**
def add(a,b):        # a, b는 매개 변수
    return a+b

#**함수의 호출**
c = add(3,4)      # 위에서 정의한 add 함수의 호출    3,4 는 인수

print(c)

#**입력값이 없는 함수**
def say():
    return 'HI'

a = say()    # 함수를 정의할때 입력값이 없으므로, say() 함수 호출시에도 인수를 넣지 않아야 함

print(a)

#**결과값이 없는 함수**
def add(a,b):
    print("%d, %d의 합은 %d입니다."%(a,b,a+b))    # return 이 없다

add(3,4)

#**입력값도 결과값도 없는 함수**
def say():
    print('HI')

say()

#**함수의 초깃값을 미리 설정**

def say_myself(name,old,man=True):
    print("나의 이름은 %s 입니다."%name)
    print("나의 나이는 %d 입니다."%old)
    if man:
        print("남자 입니다.")
    else:
        print("성별을 알 수없습니다.") 

say_myself("박응용",27)      # 세번째 인자에 값을 넣지 않으면 초기값으로 설정된 True가 man에 들어감
 
say_myself("박응용",27,False)  # 세번째 인자에 값을 넣지 않으면 초기값으로 설정된 True가 man에 들어감

#**지역 변수**
a = 1
def vartest(a):
    a = a + 1

vartest(a)         # 함수를 호출해서 a 값을 전달했고, 분명 함수 안에서 a 에 1을 더했는데.......
print(a)          # a의 값을 살펴보면 1이 출력된다.    이것은 함수 안의 a는 함수 안에서만 사용하는 지역변수 a 이기 때문이다.

#**그렇다면 위의 코드에 a에 1이 더해진 결과를 얻기 위해서는 어떻게 해야 할까?**
a = 1
def vartest(a):
    return a+1

a=  vartest(a)
print(a)          # a의 값을 살펴보면 2가 출력된다. 인자 값으로 전달된 1에서 1을 더한뒤 결과를 반환하기 때문이다.

#**lambda 함수의 사용**
add = lambda a, b: a+b     # 람다 함수의 정의

print(add(3,4))

#**input() 함수의 사용**
a = int(input())

print("%d를 입력하셨습니다."%a)

#**print() 함수의 사용**
 a = 123
 print(a)     # 숫자 출력하기

a = "python"  # 문자 출력하기    
print(a)

a = [1,2,3]
print(a)     # 리스트 출력하기


print("life", "is", "too short")   #문자열 띄어쓰기 : 콤마(,) 사용

print("life" "is" "too short")     #문자열 연결하기 : 큰따옴표("") 사용

print("life"+"is"+"too short")    #문자열 연결하기 : + 사용



#**파일 생성하기**
f = open("python.txt", 'w')
f.close()


#**생성한 파일 확인하기**
!ls


#**파일 열어 값 쓰기**
f = open("python.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


#**파일의 값 확인해 보기**
!cat python.txt

#**readline() 함수 이용하기**
# readline_test.py
f = open("python.txt", 'r')
line = f.readline()      # readline 함수는 한 줄만 읽는다.
print(line)
f.close()

#**반복문을 이용해 모든 값 읽어오기**

f = open("python.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


#**readlines 함수 사용하기**
f = open("python.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()


#**read 함수 사용하기**
f = open("python.txt", 'r')
data = f.read()
print(data)
f.close()


#**파일에 새로운 내용 추가하기**
f = open("python.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#**파일의 값 확인해 보기**
!cat python.txt

#**with 문과 함께 사용하기**
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

#**파일의 값 확인하기**
!ls
!cat foo.txt

