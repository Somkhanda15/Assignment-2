my_list = []
print(my_list)


my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

my_list = [10, 20, 30, 40]
my_list.insert(1, 15)  # Insert 15 at index 1 (second position)

print(my_list)


my_list= [10,15,20,30,40]
print(my_list)

x_list= [50,60,70]
print(x_list)

my_list.extend(x_list)
print("List after append:",my_list)

my_list=[10,15,20,30,40,50,60,70]
print(my_list)

del my_list[-1]
print(my_list)

my_list=[10,15,20,20,40,50,60]
my_list.sort()  # Sorts the list in ascending order
print(my_list)

my_list = [10,15,20,30,40,50,60]
index_of_30 = my_list.index(30)  # Find the index of 30

print(index_of_30)
