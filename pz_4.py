tuple_of_num = (1, 22, 333, 333, 4444, 55555, 666666, 7777777)

result = {}

for num in tuple_of_num:
    length_of_num = len(str(num))
    
    if length_of_num in result:
        result[length_of_num] += 1
    else:
        result[length_of_num] = 1
        
        
for length, count in result.items():
    print(f"{length} цифра - {count} элемента")