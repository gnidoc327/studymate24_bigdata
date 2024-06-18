import time


def add_1(n):
    return n + 1


target = [1, 2, 3, 4, 5]
result = []

######################
start_time = time.process_time_ns()
for value in target:
    result.append(add_1(value))
end_time = time.process_time_ns()
print('result = ', result)
print('duration time(ns) = ', end_time - start_time)

########################
start_time = time.process_time_ns()
result = map(add_1, target)
end_time = time.process_time_ns()
print('result = ', result)
print('duration time(ns) = ', end_time - start_time)
