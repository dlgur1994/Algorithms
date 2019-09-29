def check(meeting):
    count = 0
    baseTime = 0
    for time in meeting:
        if(time[1]>=baseTime):
            count += 1
            baseTime = time[0]
    return count

if __name__ == "__main__":
    numOfMeetings = int(input())
    meeting = []

    for i in range(0,numOfMeetings):
        start,end = map(int,input().split())
        meeting.append((end,start))

    meeting = sorted(meeting)
    print(check(meeting))
