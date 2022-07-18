## 확장자를 바꿔주는 코드입니다.

import glob
import os
import time

    
#while True:

files = glob.glob("../project/picam/accel/*.acc")   # acc파일 저장된 디렉터리 (*부분 앞에만 변경) //뒷부분은 .acc확장자를
for name in files:
    if not os.path.isdir(name):
        src = os.path.splitext(name)
        os.rename(name,src[0]+'.csv')   # 바꿀 확장자(csv로 바꿈.)
time.sleep(30)   # 30초마다 병경 실행하기    