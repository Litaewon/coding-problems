# 2072. 홀수만 더하기 
# list를 input으로 받을 때 & list를 조건에 의해 남기고 나머지 계산

T = int(input())

for test in range(1,T+1):
    list = map(int,input().split())
    result = 0
    for i in list:
        if i % 2 != 0:
            result += i
print("#"+str(test), str(result))
--------------------------------------------------------------------------------
# 2071. 평균값 구하기
# x 값들을 list로 받기 [int(x) for x in input().split()]
# 또는 list(map(int,input().split()))

T = int(input())

for t in range(1, T+1):
    mean = 0
    numbers = list(map(int,input().split()))
    for num in numbers:
        mean += num

    print(f'#{t} {round(mean/len(numbers))}')
----------------------------------------------------------------------------------
# 2070. 큰 놈, 작은 놈, 같은 놈
# a, b map(int,input().split()) 위치 1)앞에다가 쓰면 i 가 T번까지 반복
# 2) range 밑에다가 쓰면 a, b given으로 판단 그리고 i 값만 증가
# range 범위: i를 1 부터 시작할거냐 0부터 시작할거냐
T = int(input())

for i in range(1,T+1):
    a, b = map(int,input().split())
    if a>b:
        print(f'#{i} >')
    elif a==b:
        print(f'#{i} =')
    else:
        print(f'#{i} <')
------------------------------------------------------------------------------------
# 2068. 최대수 구하기

T = int(input())

for i in range(1,T+1):
    lists = map(int,input().split())
    print(f'#{i} {max(lists)}')
--------------------------------------------------------------------------------------
# 2063. 중간값 찾기 
# 중간값 - 크기수준으로 배열

N = int(input())
lists = list(map(int,input().split()))
lists.sort()
print(lists[N//2])
--------------------------------------------------------------------------------------
# 2058. 자릿수 더하기
# int(input()) -> error발생. int()는 len사용이 안됨.
# len(n): 자리수 갯수, 자리수별로 int()화 하고 더하기.

N = input()
result = 0
for i in range(len(N)):
    result += int(N[i])
print(result)
--------------------------------------------------------------------------------------
# 2056. 연월일 달력
# days[int(month)]에 받는 수들 정리 days.
T = int(input())

days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for i in range (1,T+1):
    date = str(input())
    year = date[0:4]
    month = date[4:6]
    day = date[6:8]

    result = ''
    if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
        result = year + '/' + month + '/' + day
    else:
        result += '-1'
    print("#" + str(i) + " " + result)
-----------------------------------------------------------------------------------------------
# 2050. 알파벳을 숫자로 변환
# "영단어 -> 숫자"에서 0부터 시작하니+1. 
# .index()함수 배열에서 위치

str = input()
data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in str:
    print(data.index(i)+1, end = " ")
-------------------------------------------------------------------------------------------------------------
# 2047. 신문 헤드라인

a = input()
print(a.upper())
------------------------------------------------------------------------------------------------------------
# 1859. 백만 장자 프로젝트
# for val in arr[::-1]: 배열 역순
# 현재 값이 최댓값보다 크거나 같다면. 최댓값 업데이트
# 아니라면 정답값에 가겨차이를 더한다. (현재 값에 구매해서 최대값에 판다)


N = int(input())
for i in range(1,N+1):
    m = int(input())
    result = 0
    arr = list(map(int,input().split()))
    sellprice = 0
    
    for val in arr[::-1]:
        if val >= sellprice:  # sellprice 가격 높은 val있으면 changed
            sellprice = val
        else:
            result += sellprice - val # 최종 sellprice에서 val값들 뺀거 result에 다 더해 
    print(f'#{i} {result}')