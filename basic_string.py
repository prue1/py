import math
import string

# 練習使用python api
formatter = string.Formatter() # 產生一個物件
print(formatter.format("These are ascii letters:{0}", string.ascii_letters))
print(math.ceil(123.6))

#####################

str = 'abc'
print(f'{str:5}end') # 字串向左靠
print(f'{str=}')
d = 10;
print(f'{d:5}end') # 數字向右靠
