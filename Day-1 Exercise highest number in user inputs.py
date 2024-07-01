numbers_input = input("Enter numbers separated by space: ")
split=numbers_input.split(" ")
item=[int(item) for item in split]
add=0
for i in item:
    if i>add:
        add=i
print(add)        

    
    
