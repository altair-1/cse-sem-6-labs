def bubbleSort(list):   
    for i in range (0, len(list)-1):  
        for j in range(len(list)-1):  
            if(list[j]>list[j+1]):  
                temp = list[j]  
                list[j] = list[j+1]  
                list[j+1] = temp  
    return list 
  
list = [97, 26, 54, 99, 12, 61]  
print(list)  
print("sorted list is: ", bubbleSort(list))