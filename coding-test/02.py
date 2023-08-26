# 입력
돌의내구도 = [1, 2, 1, 4]
독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]

# 출력
# 생존자 : ['씨-독']

# 입력
# 돌의내구도 = [5, 3, 4, 1, 3, 8, 3]
# 독 = [{
#     "이름" : "루비독",
#     "나이" : "95년생",
#     "점프력" : "3",
#     "몸무게" : "4",
#     },{
#     "이름" : "피치독",
#     "나이" : "95년생",
#     "점프력" : "3",
#     "몸무게" : "3",
#     },{
#     "이름" : "씨-독",
#     "나이" : "72년생",
#     "점프력" : "2",
#     "몸무게" : "1",
#     },{
#     "이름" : "코볼독",
#     "나이" : "59년생",
#     "점프력" : "1",
#     "몸무게" : "1",
#     },
# ]

# 출력
# 생존자 : ['루비독', '씨-독']

def 징검다리를건너라1(돌의내구도, 독):
    answer = [독[i]['이름'] for i in range(len(독))]
    return answer

def 징검다리를건너라2(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    return answer

# print(징검다리를건너라1(돌의내구도, 독))
# print(징검다리를건너라2(돌의내구도, 독))

def 징검다리를건너라3(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    for i in 독:
        독의위치=0
        while 독의위치 < len(돌의내구도)-1:
            독의위치 += int(i['점프력'])
            돌의내구도[독의위치-1] -= int(i['몸무게'])
            if 돌의내구도[독의위치-1] < 0:
                answer[answer.index(i['이름'])] = 'fail'
                break
    return [i for i in answer if i != 'fail']

# print(징검다리를건너라3(돌의내구도.copy(), 독.copy()))

ll = [1,2,3,4,5]
# print(ll)
def change(l):
    l[0]=1000
change(ll)
# print(ll)

xx = 100
# print(xx)
def change(x):
    x += 1000
change(xx)
# print(xx)

# remove 0(N)
# del 0(1)

def 징검다리를건너라(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    for i in 독:
        독의위치=0
        while 독의위치 < len(돌의내구도)-1:
            독의위치 += int(i['점프력'])
            돌의내구도[독의위치-1] -= int(i['몸무게'])
            if 돌의내구도[독의위치-1] < 0:
                del answer[answer.index(i['이름'])]
                break
    return answer

# print(징검다리를건너라(돌의내구도.copy(), 독.copy()))

import json

JSON독 = json.dumps(독, ensure_ascii=False)

# print(JSON독)
# print(독)
# print(JSON독[0])
# print(JSON독[:10])

JSON독 = json.loads(JSON독)

print(JSON독)
print(JSON독[0])
