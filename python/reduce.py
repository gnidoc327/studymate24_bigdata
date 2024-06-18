# 리스트 전체 합 구하기 : Reduce
import time
from functools import reduce


def add(_data):
    _result = 0
    for i in _data:
        _result += i
    return _result

data = [1, 2, 3, 4, 5]

##########################
start_time = time.process_time_ns()
result = add(data)
print(result)  # 15 출력
end_time = time.process_time_ns()
print('result = ', result)
print('duration time(ns) = ', end_time - start_time)

##########################

start_time = time.process_time_ns()
result = reduce(lambda x, y: x + y, data)
print(result)  # 15 출력
end_time = time.process_time_ns()
print('result = ', result)
print('duration time(ns) = ', end_time - start_time)
