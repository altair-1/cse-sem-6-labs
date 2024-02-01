list = ['physics', 'chemistry', 1997, 2000];
list.append('maths')
print(list)

#To delete an element in a list
del list[2] #will remove 1997 record from the list.
print(list)
#To check a data in a list,
print('physics' in list) #will return ‘True’
print('english' in list) #will return ‘False’
print(len(list)) #will return total items in list
print(list.count('physics'))

#list.pop (), will remove and return the last item from the list.
list = ['physics', 'chemistry', 1997, 2000];
list.pop()
print(list)

#list.insert() , will insert an item in the specified index
list = ['physics', 'chemistry', 1997, 2000];
list.insert (2, 'maths')
print(list)

list = ['physics', 'chemistry', 1997, 2000];
list.remove('chemistry') #will remove the item specified.
print(list)

list = ['physics', 'chemistry', 1997, 2000];
list.reverse() #will reverse the objects of the list in place.
print(list)
