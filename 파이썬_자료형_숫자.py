# -*- coding: utf-8 -*-
"""파이썬 - 자료형 - 숫자.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pDLTaZXGcNs960AlDVldm9u0kI9flYMa

정수
"""

print(12, 0o12,0x12) #12:십진수, 0o12:8진수, 0x12:16진수

print(type(12),type(0o12),type(0x12))

"""# 실수"""

print(3.14, 1.234e6) #3.14:부동 소수점 표기, 1.234e6:지수 표현

print(type(3.14),type(1.234e6))

"""# 수와 관계있는 연산"""

print("8+3 = ", 8+3)
print("8-3 = ", 8-3)
print("8*3 = ", 8*3)
print("8/3 = ", 8/3)

print("8//5=",8//5)#몫
print("8%5=",8%5) #나머지

i = 0
i = (i+1)%5
print(i)
i = (i+1)%5
print(i)
i = (i+1)%5
print(i)
i = (i+1)%5
print(i)
i = (i+1)%5
print(i)
i = (i+1)%5
print(i)
i = (i+1)%5
print(i)
i = (i+1)%5
print(i)
i = (i+1)%5
print(i)

"""# 복소수"""

print(2+3j)

cv = 2+3j
print("실수부:",cv.real, "허수부:",cv.imag)