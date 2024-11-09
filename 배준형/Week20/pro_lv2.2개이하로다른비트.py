def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(find_num(number))
    return answer

# 비트가 1개 혹은 2개 다른 수들을 만들고 제일 작은 수를 반환해야 함
# 만약 111111111111 이 주어지면
# 그 다음수인 1000000000000 부터 십진수로 차례대로 순회하면
# 1개 혹은 2개 다른 수를 찾기까지 굉장히 오래 걸림
# 비트를 이동시켜서 찾아내야 함
# how?????????
def find_num(num):
    candis = []
    bin_num = "0" + bin(num)[2:]
    candis.extend(find_bigger_num(num))
    # print(candis)
    tmp = []
    for candi in candis:
        tmp.extend(find_bigger_num(candi))
    candis += tmp
    candis = sorted(list(set(candis)))
    # print(candis)
    return bin_search(num, candis, 0, len(candis)-1)

def bin_search(t, arr, s, e):
    if s == e:
        return arr[s]

    mid = (s+e)//2
    if arr[mid] > t:
        return bin_search(t, arr, s, mid)
    return bin_search(t, arr, mid+1, e)
    

def find_bigger_num(num):
    result = []
    # print(bin(num))
    bin_num = "0" + bin(num)[2:]
    
    for i in range(len(bin_num)):
        tmp = bin_num[i]
        if tmp == "0":
            tmp = "1"
        else:
            tmp = "0"
        
        b = int("0b" + bin_num[0:i] + tmp + bin_num[i+1:], 2)
        # if b > num:
        result.append(b)
        
    return result