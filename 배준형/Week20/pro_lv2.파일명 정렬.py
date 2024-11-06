def solution(files):
    answer = []
    arr = []
    
    for file in files:
        tmp = ""
        digit = False
        tmp_item = [file]
        for s in file+"a":
            # print(s)
            if not digit:
                if s.isdigit():
                    tmp_item.append(tmp)
                    tmp = s.lower()
                    digit = True
                else:
                    tmp += s.lower()
            else:
                if s.isdigit():
                    tmp += s.lower()
                else:
                    tmp_item.append(tmp)
                    tmp = s.lower()
                    digit = False
        arr.append(tmp_item)
    arr.sort(key=lambda x: (x[1], int(x[2]))) 
    # print(arr)
    answer = [i[0] for i in arr]
    return answer

# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))