# while 문

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d 번 찍었습니다."% treeHit)
    if treeHit == 10:
        print("나무 넘어 갑니다.")

#**break 사용하기**
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee  -1
    print("남은 커피양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break

#**continue 사용하기**
a= 0
while a <10:
    a = a+1
    if a % 2 ==0:
        continue
    print(a)


# for 문
#**리스트를 이용한 for 반복문**
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#**range() 함수의 사용**
a = range(10)
a
    

a = range(1,11)
a

#**튜플을 이용한 for 문**
a = (1,2,3)

for i in a:
    print(i)


#**문자열을 이용한 for 문**
word = "I love python"

for i in word:
    print(i)

#**이중 for 문**
for i in range(2,10):        # ①번 for문
    for j in range(1, 10):   # ②번 for문
        print(i*j, end=" ") 
    print('')

#**내포 리스트**


# 학생들의 성적 처리 하기
score = [[23,90,20,90],[25,50,20,10],[15,60,5,70],[0,30,20,20],[0,10,0,30],[5,70,5,100]]

grade = []

for i in score:

    sum = 0
    for j in i:
        sum +=j
    grade.append(sum)

print(grade)
