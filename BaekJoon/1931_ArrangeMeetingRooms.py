numOfMeetings = int(input())
start = []
end = []

for i in range(0,numOfMeetings):
    a,b = map(int,input().split())
    start.append(a)
    end.append(b)

nowMin = min(end)
id = end.index(min(end))
end[id] = -1

