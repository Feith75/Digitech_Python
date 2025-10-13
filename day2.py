my_list = [1,2,3,4]
print(my_list)

my_list.append(5)
print(my_list)

my_list.extend([6,7,8])
print(my_list)

my_list.insert(2,9)
print(my_list)

my_list.remove(9)
print(my_list)

my_list.pop(5)
print(my_list)

popping = my_list.pop(5)
print(my_list,"removed element is:",popping)

new_dict = {"name":"lenox","Country":"kenya"}
setdefaulting = new_dict.setdefault("ethnicity","giriama")
print(setdefaulting)
c
updating = my_dict.update(new_dict)
update(my_list)