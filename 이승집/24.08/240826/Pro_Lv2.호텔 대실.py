from heapq import heappush, heappop

book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]

book_time = [[int(i[0][:2]) * 60 + int(i[0][3:5]), int(i[1][:2]) * 60 + int(i[1][3:5])] for i in book_time]
book_time.sort(key=lambda x: x[0])
print(book_time)
rooms = []

for start, end in book_time:
    if rooms and rooms[0] <= start:
        heappop(rooms)

    heappush(rooms, end + 10)

print(len(rooms))