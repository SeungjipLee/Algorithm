import math

# 시간 차이(분)를 구하는 함수
def time_difference(time1, time2):
    minute1 = int(time1[:2]) * 60 + int(time1[3:])
    minute2 = int(time2[:2]) * 60 + int(time2[3:])
    
    return abs(minute1-minute2)


def solution(fees, records):
    my_dict = {}
    for record in records:
        parsed_record = record.split()
        time = parsed_record[0]
        num = parsed_record[1]
        IN_OUT = parsed_record[2]
        if my_dict.get(num) == None:
            my_dict[num] = [time, 0, IN_OUT, 0]
        else:
            if IN_OUT == 'IN':
                my_dict[num][0] = time
                my_dict[num][2] = IN_OUT
            else:
                parking_time = time_difference(my_dict[num][0], time)
                my_dict[num][0] = time
                my_dict[num][2] = IN_OUT
                my_dict[num][3] += parking_time


    # IN 상태인 것들 시간 누적
    for key, value in my_dict.items():
        if value[2] == 'IN':
            parking_time = time_difference('23:59', value[0])
            my_dict[key][3] += parking_time
    
    # 요금 계산
    for key, value in my_dict.items():
        if value[3] <= fees[0]:
            cost = fees[1]
        else:
            cost = fees[1] + math.ceil((value[3]-fees[0]) / fees[2]) * fees[3]
        my_dict[key][1] += cost

    sorted_keys = sorted(my_dict.keys(), key=lambda k: int(k))
    sorted_dict = {key: my_dict[key] for key in sorted_keys}
    answer = [value[1] for value in sorted_dict.values() ]
    return answer
