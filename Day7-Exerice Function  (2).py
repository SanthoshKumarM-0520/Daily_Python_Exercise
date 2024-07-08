import random



letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|']



letter_input=int(input("How many letters you want:"))
numbers_input=int(input("How many numbers you want:"))                 
symbols_input=int(input("How many symbols you want:"))
abc=letter_input+numbers_input+symbols_input


def first_result(a,a1):
    global abc
    
    while abc!=len(result1):
        
        result1=[]
        count=0
        for i in range (a+count):
            random1=str(random.choice(a1))
            if random1 in result1:
                count+=1
            else:           
                result1.append(random1)        
        return result1


ans1=first_result(a=letter_input,a1=letters)+first_result(a=numbers_input,a1=numbers)+first_result(a=symbols_input,a1=symbols)
random.shuffle(ans1)
print(''.join(ans1))
print(len(ans1))






    
    
