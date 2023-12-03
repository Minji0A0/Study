#**튜플 자료형의 정의**
t1 = ()
t2 = (1.)
t3 = (1, 2, 3)
t4 = 1, 2, 3
print(t1,t2,t3,t4)


#**튜플 데이터 삭제를 시도한다면?**
t1 = (1,2,'a','b')
del t1[0]   # 에러 발생!

#**튜플 값에 변경을 시도한다면?**
t1 = (1,2,'a','b')
t1[0] = 'c'

#**인덱싱 다루기**
t1 = (1,2,'a','b')
t1[0]

#**슬라이싱 하기**
t1 = (1,2,'a','b')
t1[1:]

#**튜플 더하기와 곱하기**
t2 = (3, 4)
t1+t2

#**튜플 길이 구하기**
t1 = (1,2,'a','b')
len(t1)

#**튜플을 적용하여 온라인 거래 명세서 만들기**
transaction1001 = ("파이썬 코딩 길잡이", "데이터베이스론", "JAVA")
print("3월 1일 주문 송장 : ", transaction1001)

transaction1002 = ("요리비법", "영화평론", "헤리포터")
print("3월 15일 주문 송장 : ", transaction1002)


# 딕셔너리

#**딕셔너리의 선언**
dic = {'name':'pey', 'age':'25','birth':'0328'}
print(dic)
a = {1:'hi'}
print(a)
b = {'a':[1,2,3]}
print(b)

#**딕셔너리 쌍 추가하기**
a = {1: 'a'}
a['a'] = 'b'
print(a)

a['name'] = 'pey'
print(a)


#**딕셔너리 key 값이 1인것을 찾아 삭제**
del a[1]
print(a)


#**딕셔너리에서 key 를 사용해 value 얻기**
score = {'pey': 40, 'juliet': 99, 'tom': 70}
print(score['pey'])
print(score['tom'])


#**딕셔너리 관련 함수**
a = {'name': 'pey', 'phone': '01022223333', 'birth':'1118'}     # key 만을 모아서 dict_keys 객체로 반환
print(a.keys())

list(a.keys())  # key를 모아서 리스트로 변환

a.values()    # value 만을 모아서 dict_value 객체로 반환

a.items()     # key와 value 쌍을 튜플로 묶은 값을 모아서 idc_items 객체로 반환환

a.clear()     # 딕셔너리 요소를 모두 삭제.clear()     # 딕셔너리 요소를 모두 삭제
print(a)


# <strong> key 가 딕셔너리 안에 있는지 조사  
# key가 딕셔너리 안에 존재하면 True, 존재하지 않으면 False를 반환 </strong>
a = {'name': 'pey', 'phone': '01022223333', 'birth':'1118'}   
print('name' in a)
print('email' in a)
print('email' not in a)


#**key 에 대응되는 value를 반환**
print(a.get('name'))
print(a.get('phone'))


# 집합 자료형

#**집합의 선언**
s1 = set([1,2,3])
s1

#**문자열을 입력하여 집합 선언**
(s2 = set("apple")
s2

#**집합 자료형의 연산**
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)   # 교집합
print(s1 | s2)   # 합집합
print(s1 - s2)   # 차집합

#**집합 관련 함수**
s1 = set([1, 2, 3])

s1.add(4)     # set 자료형에 요소 추가
print(s1)
s1.remove(2) # set 자료형에 요소 삭제
print(s1)
s1.update([5,6,7])   # set 자료형에 여러 요소 추가
print(s1)   

# 불 자료형
 a = True
 b = False

print(type(a))
print(type(b))

#**불 자료형은 데이터가 비어있는 변수에 0을 반환, 값이 있으면 1을 반환함**
print(bool("python"))
print(bool(""))

# 실습예제

#문자열 합치기
addr1_str="서울시 서울특별시 seoul"
addr2_str="서울 Seoul 서울-특별시"
addr3_str= "서울 서울-시"
 
addr_str = addr1_str +" "+ addr2_str + " " + addr3_str

print(addr_str)   # 합친 문자 확인
addr_str=addr_str.lower()
print(addr_str)


addr_list=addr_str.split()
print(addr_list)

len(addr_list)

print(set(addr_list))
