
# TODO: What's the shape of input?

used_list = [3, 4, 2, 1, 5]
NUMBER = len(used_list)

for i in range(NUMBER-1):
    for j in range(NUMBER-1):
        if used_list[j] > used_list[j+1]:
            temp = used_list[j+1]
            used_list[j+1] = used_list[j]
            used_list[j] = temp

print(used_list)
