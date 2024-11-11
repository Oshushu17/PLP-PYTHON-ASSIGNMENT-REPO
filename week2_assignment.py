
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("Adding element using append method: ",my_list)


my_list.insert(1, 15)
print("Using insert method to insert element: ",my_list)


other_list = [50, 60, 70]

my_list.extend(other_list)
print("Extending list using extend method: ", my_list)

my_list.remove(70)
print("Using remove method to remove element: ",my_list)


print("sorted list",my_list.sort())

locate_index_30 = my_list.index(30)
print(locate_index_30)
