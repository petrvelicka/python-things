number = int(input())

previous = 1
current = 1

for i in range(number - 2):
    next = previous + current
    previous = current
    current = next

print(current)