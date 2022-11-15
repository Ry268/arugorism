N = int(input())
output = ""

while (N >= 1):
    if N % 2 == 0:
        output = "0" + output
    if N % 2 == 1:
        output = "1" + output
    N = N // 2

print(output)