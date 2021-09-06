import heapq
def solution(jobs):
    jobs.sort(key = lambda x : x[0])

    answer = len(jobs)
    current_time, total_time = 0,0
    heap = []

    while jobs or heap :
        cnt = 0
        for job in jobs :
            if current_time >= job[0] :
                heapq.heappush(heap, [job[1], job[0]])
                cnt += 1
            else :
                break
        for i in range(cnt) :
            jobs.pop(0)
        if not heap :
            current_time += 1
            continue
        job = heapq.heappop(heap)
        total_time += current_time - job[1] + job[0]
        current_time += job[0]
    return total_time // answer

print("정답 : ",solution([[0, 3], [1, 9], [2, 6]]))