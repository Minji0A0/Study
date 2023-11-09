# python은 아래와 같이 계산이 가능함
print(1+2)

# a와 b라는 변수를 지정해주면 계산가능함
a=4
b=5
print(a+b)

# c를 포함하여 위의 있는 값또한 연산가능함
c=20
print(a+b+c)

# 문자 출력
print('Hello World')

# 배열을 통한 if문 활용
#존재하지 않을경우
languages = ['python', 'perl', 'c++', 'java']
if 'assembly' in languages :
    print("It`s difficult to learn")

#존재할경우
languages = ['python', 'perl', 'c++', 'java']
if 'c++' in languages :
    print("It`s difficult to learn")
    print("but It`s fast")

#존재하지 않을경우 elif 사용하여 찾
languages = ['python', 'perl', 'c++', 'java']
if 'assembly' in languages :
    print("It`s difficult to learn") 
elif 'python' in languages :
    print("It`s easy to learn")
