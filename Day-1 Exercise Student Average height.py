user=input("enter the heigth of the student with comma:")
Split_user=user.split(",")
int_user=[int(item) for item in Split_user]
add=0
numbers=0
for i in int_user:
    add+=i
    numbers+=1
final=add/numbers
print(final)

    
