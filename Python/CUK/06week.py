#**정상 혈압 **    

#**딕셔너리 형태로 변수 선언**

bloodPressure={}

#**나이 입력 받기**

print("당신의 나이를 입력하세요")   # 나이 입력
bloodPressure['age'] = int(input())

#**성별 입력**
print("당신의 성별을 입력하세요 : 예: 남성- M, 여성-F")   # 성별 입력
bloodPressure['sex'] = input()

#**최고 혈압입력**
print("최고 혈압을 입력하세요 : ")   # 최고 혈압 입력
bloodPressure['maxBP'] = int(input())

#**최저 혈압 입력**
print("최저 혈압을 입력하세요 : ")   # 최저 혈압 입력
bloodPressure['minBP'] = int(input())

#**입력된 데이터 확인**
print(bloodPressure)

#**정상 혈압 판별**  
(10살 이하 나이에 대해서는 예외처리)

if (bloodPressure['age'] >= 10 and bloodPressure['age'] < 20):  # 10대 
    if(bloodPressure['sex'] == 'M'):
        if(bloodpressure['maxBP']<102 and bloodpressure['minBP']<64):
            print("정상 혈압입니다.")
        else:
            print("비정상 혈압입니다. 정밀 검사가 필요합니다")
    elif (bloodPressure['sex'] == 'F'):
        if(bloodpressure['maxBP']<98 and bloodpressure['minBP']<62):
            print("정상 혈압입니다.")
        else:
            print("비정상 혈압입니다. 정밀 검사가 필요합니다")
    else:
        print("성별을 잘못 입력하였습니다.")    # 성별에 대한 예외 처리

elif (bloodPressure['age'] >= 20  ): # 20대 이상

    if(bloodPressure['sex'] == 'M'):
        if(bloodPressure['maxBP']<120 and bloodPressure['minBP']<80):
            print("정상 혈압입니다.")
        else:
            print("비정상 혈압입니다. 정밀 검사가 필요합니다")
    elif (bloodPressure['sex'] == 'F'):
        if(bloodpressure['maxBP']<115 and bloodpressure['minBP']<75):
            print("정상 혈압입니다.")
        else:
            print("비정상 혈압입니다. 정밀 검사가 필요합니다")
    else:
        print("성별을 잘못 입력하였습니다.")   # 나이에 대한 예외 처리
else:
    print( "나이를 잘못 입력하였습니다.")       # 나이에 대한 예외 처리


age = -20
if(age >=20 ):
    print("주류 판매가 가능합니다.")
elif(age < 20):
    print("주류 판매가 불가능합니다.")
else:
    print("나이를 잘못 입력했습니다.")

    
