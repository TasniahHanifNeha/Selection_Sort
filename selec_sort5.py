


def selec(data_list):
    n = len(data_list)
    for i in range(n-1):
        min_val = i

        for j in range(i+1, n):
            if data_list[j] < data_list[min_val]:
                min_val = j

        # swapping
        if min_val != i:
            temp = data_list[i]
            data_list[i] = data_list[min_val]
            data_list = temp


    return data_list

data_list = [100, 20, 100, 50, 30]

print(selec(data_list))




















