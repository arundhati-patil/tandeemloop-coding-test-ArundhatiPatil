a = int(input("Enter a number: "))

# If even → use a-1, if odd → use a
count = a if a % 2 != 0 else a - 1

result = []
for i in range(1, 2 * count, 2):
    result.append(i)

print(result)
