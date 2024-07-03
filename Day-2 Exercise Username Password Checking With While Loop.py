'''This program prompts the user to enter a username and password,
allowing three attempts each for correct input verification,
upon successful authentication, it prints "Login successful!",
otherwise issuing warnings and terminating after four unsuccessful attempts.'''

password="san4565@prem"
username="santhosh_steve"
username_input=input("Enter your user name:")
password_input=input("Enter your password:")
username_attempt=0
password_attempt=0
while username_input!=username:
    username_attempt+=1
    if username_attempt==3:
        print("........Last chance for correct username........")
    if username_attempt>=4:
        print("........Your chance is our...Bye............")
        break
    else:
        print("Your username is Wrong Re-enter it")
        username_input=input("Enter correct user name:")        
while password_input!=password:
    password_attempt+=1
    if password_attempt==3:
        print("..........Last chance for password...........")
    if password_attempt>=4:
        print("..........Your chance is our...Bye..........")
        break
    else:
        print("Your password is Wrong Re-enter it")
        password_input=input("Enter correct password:")
if password==password_input:
    if username==username_input:
        print("Login successful!")
    
    
        
