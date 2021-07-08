

def selec(data_list):
    n = len(data_list)
    for i in range(n-1):
        min_value = i

        for j in range(i+1, n):
            if data_list[j] < data_list[min_value]:
                min_value = j

        #s wapping
        if min_value != i:
            temp = data_list[i]
            data_list[i] = data_list[min_value]
            data_list[min_value] = temp

    return data_list

data_list = [40, 20, 90, 50, 30]

print(selec(data_list))




























