# Bubble Sort
def bubble(used_list) -> list:
    NUMBER = len(used_list)

    for i in range(NUMBER - 1):
        for j in range(NUMBER - 1):
            if used_list[j] > used_list[j + 1]:
                temp = used_list[j + 1]
                used_list[j + 1] = used_list[j]
                used_list[j] = temp

    return used_list
