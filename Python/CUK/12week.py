# 모듈

#**현재 파일을 쓰는 디렉토리 위치 확인!**

!pwd

!cat mod2.py


#**모듈 불러오기**

import mod2

print(mod2.add(1,2))
print(mod2.sub(2,1))

#**from 구문을 이용한 모듈 이름 생략**

from mod2 import add, sub
print(add(1,2))
print(sub(2,1))

#**class가 포함된 모듈 불러오기**
from mod3 import Math

a = Math()

print(a.solv(2))

#**모듈을 저장한 디렉터리 사용하기**
import sys
sys.path

#**구글 드라이브 마운트**
from google.colab import drive
drive.mount('/gdrive')

with open('/gdrive/My Drive/foo.txt', 'w') as f:
  f.write('Hello Google Drive!')
!cat '/gdrive/My Drive/foo.txt'


sys.path.append("/gdrive/My Drive/")

sys.path

from mod4 import mul

print(mul(5,6))

# 패키지

!pip list

!pip install rsa3

import numpy, pyrsa
data = pyrsa.data.Dataset(numpy.random.rand(10, 5))
rdms = pyrsa.rdm.calc_rdm(data)
pyrsa.vis.show_rdm(rdms)
