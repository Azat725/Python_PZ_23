
first_tuple = (1, 2, 3, 4, 5, 6, 7, 8) # Явное 
print(first_tuple, type(first_tuple))
print()

sec_tuple = 1, 2, 4, 5, 6, 7 # Не явное сoздание картежа
print(sec_tuple, type(sec_tuple))
print()

third_tuple = tuple(range(1, 8))
print(third_tuple, type(third_tuple))
print()

print(5 in first_tuple)
print(5 not in first_tuple)
print()

fourth_tuple = (2, "Python is GAY language!?!??!?", [1, 2, 3, 4])
print(fourth_tuple, type(fourth_tuple))
print()

some_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(some_list.__sizeof__())
print(first_tuple.__sizeof__())

most_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in most_tuple:
    print(i)
    
print()