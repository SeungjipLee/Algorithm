# 호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다. 
# 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.
# 예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때, 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.

def solution(book_time):
    # 시간을 분으로 바꾸는 함수
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes
    # 입실 시간 기준으로 정렬 한번 하고
    # 시간을 분단위로 변경
    # 입장시간 리스트와 퇴장시간 리스트 만들기
    # 순회를 하여 퇴장시간보다 크거나 같으면 해당 인덱스교체
    time_line = sorted(book_time, key=lambda x: x[0])  # 시작순서에 맞게 정렬
    st = []
    en = []
    use_room = [0]

    for start, end in time_line:  # 시작시간과 종료시간을 분으로 전환
        st.append(time_to_minutes(start))
        en.append(time_to_minutes(end)+10)
    
    for i in range(len(time_line)):  # 모든 예약을 순회
        for j in range(len(use_room)):  # 지금 사용하고있는 방의 종료시간을 체크, 시작시간이 해당 종료시간보다 크거나 같으면 교체 작으면 추가
            if st[i] >= use_room[j]:
                use_room[j] = en[i]
                break
            elif j == len(use_room) - 1:
                use_room.append(en[i])
    answer = len(use_room)
    return answer