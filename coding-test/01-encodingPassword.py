# 배열
text=['   + -- + - + -   ',
'   + --- + - +   ',
'   + -- + - + -   ',
'   + - + - + - +   ']

# default
for i in text:
    print(i)

print()

# strip : 앞뒤 공백 제거 / rstrip / lstrip
for i in text:
    print(i.strip())

print()

# replace : 변환
for i in text:
    print(i.strip().replace(' ',''))

print()

for i in text:
    print(i.strip().replace(' ','').replace('+','1').replace('-','0'))

print()

# 10진법 변환
for i in text:
    print(int(i.strip().replace(' ','').replace('+','1').replace('-','0')))

print()

# 10진법 > 2진법 변환
for i in text:
    print(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2))

print()

# ord() : 문자 > 숫자
# chr() : 숫자 > 문자
for i in text:
    print(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)))

print()

# 문자를 배열로 합
l=[]
for i in text:
    l.append(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)))
print(l)

print()

# 배열 > 문자열
print(''.join(l))

print()

# 한줄로. 리스트 컴프리헨션
print(text)
print([i for i in text])
print([chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)) for i in text])
print(''.join([chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)) for i in text]))

print()

# 리스트 컴프리헨션 연습
print([i for i in range(10)])
print([i for i in range(10) if i % 2 == 0])

print()

print([f'{i} X {j} = {i*j}' for i in range(2,10) for j in range(1,10)])

print()

# replace
print('011011011'.replace('0','!').replace('!','+').replace('+','~'))

print()

# zfill, 해당 숫자만큼 자리수 맞춤. 무슨 숫자로 채우느냐
print('111'.zfill(10))

print()

# function
sample = [i.strip().replace(' ','').replace('+','1').replace('-','0') for i in text]
print(sample)

print()

# map(function, sample)
# function > int형으로 바꿔주고, 문자열로 바꿔주는 거로 세팅
# define 으로 풀거나 (def) 람다로 풀거나.

# 1. 람다.
# lambda x : chr() : x 가 들어오면 문자열로
# lambda x : chr(int(x,2)) : x 가 들어오면 int형 2진법으로, 문자열로
# 주소값만 나옴.
print(map(lambda x : chr(int(x,2)),sample))

print()

# list로 변환
print(list(map(lambda x : chr(int(x,2)),sample)))

print()

# 문자열로 변환
print(''.join(list(map(lambda x : chr(int(x,2)),sample))))

print()

# 2.def.
def f(x):
    return chr(int(x,2))

print(list(map(f,sample)))

print()

# 문자열로 변환
print(''.join(list(map(f,sample))))

# zip


