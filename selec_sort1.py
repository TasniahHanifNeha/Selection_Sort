
            
def selectionSort(data_list):
    n = len(data_list)
    for i in range(n-1):       # i = 0|1...
        min_Value = i               # min_Value = 40|20...

        for j in range(i+1, n):   #(1|2... to 4)
            # j = i+1 ==> j = 0+1 = 1|2 
            # 20<40|20<20
            if data_list[j] < data_list[min_Value] :
                min_Value = j     # min_value = 20|20...


        # 20 != 40|20=20|...
        if min_Value != i:         
            temp = data_list[i] #temp=40..
            data_list[i] = data_list[min_Value] #40=20..
            data_list[min_Value] = temp #20=temp...


    return data_list

#data_list =  0   1   2   3   4
data_list = [40, 20, 10, 50, 30]

print(selectionSort(data_list))





















