from collections import deque
a={"a":"","b":""}
li=deque(a.items())
b=li.popleft()

print(b)
