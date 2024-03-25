fruit = input("Enter a fruit name -> ")
fruits = (
    "apple", 
    "apple", 
    "banana", 
    "banana", 
    "banana", 
    "mango", 
    "chery", 
    "banana", 
    "apple", 
    "bananamango", 
    "mango", 
    "strawberry-banana"
    )

count_fruit = fruits.count(fruit)
print(f"Your fruit in fruits tuple -> {count_fruit}")

# fruit_part = sum()

count = 0

for i in fruits:
    if fruit in i:
        count += 1
        
print(f"Your fruit in fruits tuple -> {count}")