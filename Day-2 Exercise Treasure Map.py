line_1=['⬜️','⬜️','⬜️']

'''Treasure Hunt Game Simulation
This Python program allows users to play a simple treasure hunt game.
Players input coordinates (e.g., A3) to mark their guesses on a 3x3 grid. The program updates the grid with an "❌" to indicate the guessed location.
Players can visually track their progress on the grid until they find the hidden treasure.'''


line_2=['⬜️','⬜️','⬜️']

line_3=['⬜️','⬜️','⬜️']
line_1_2_3=line_1,line_2,line_3
print("enter where you want to hide the treasure (eg: A3)")
print("   1  2  3\nA ⬜️ ⬜️ ⬜️\nB ⬜️ ⬜️ ⬜️\nC ⬜️ ⬜️ ⬜️")  
inputuser=input("enter the ques:")
first=inputuser[0]
second=inputuser[1]
lower_first=first.lower()
sam=0
if lower_first=="a":
    sam=0
elif lower_first=="b":
    sam=1
elif lower_first=="c":
    sam=2
ram=0
if second=="1":
    ram=0
elif second=="2":
    ram=1
elif second=="3":
    ram=2
line_1_2_3[sam][ram]=("❌")


sring_line_1=""
sring_line_2=""
sring_line_3=""
for i in line_1:
    sring_line_1+=(" ")+i+(" ")
for j in line_2:
    sring_line_2+=(" ")+j+(" ")
for k in line_3:
    sring_line_3+=(" ")+k+(" ")
print(f"   1   2   3\nA{sring_line_1}\nB{sring_line_2}\nC{sring_line_3}")
    
    
