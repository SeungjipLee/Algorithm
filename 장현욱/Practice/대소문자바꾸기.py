# 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 
# 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서
# 출력하는 코드를 작성해 보세요.

str = input()
str2 = ''

for i in str:
  if i.isupper() == True:
    str2 += i.lower()
  elif i.islower() == True:
    str2 += i.upper()
print(str2)

print(str.swapcase())