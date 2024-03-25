auto_tuple = ("BMW", "Mercedes-Benz", "AUDI", "Bentley", "Rols-Roys", "Porshe")

new_auto = input("Enter a new avto name -> ")
replace_auto = input("Enter avto name for replacement -> ")

updated_tuple = tuple(new_auto if auto == replace_auto else auto for auto in auto_tuple)

print(f"Auto tuple -> {auto_tuple}")
print(f"Updated auto tuple -> {updated_tuple}")