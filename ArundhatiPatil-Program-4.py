numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

output = {}

for n in range(1, 10):   # 1 to 9
    count = 0
    for x in numbers:
        if x % n == 0:
            count += 1
    output[n] = count

print(output)

Input:

[1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]


Output:

{1:11, 2:8, 3:4, 4:4, 5:3, 6:2, 7:0, 8:1, 9:1}
