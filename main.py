import os
from time import sleep

def clear_screen():
 os.system('cls' if os.name == 'nt' else 'clear')
def CreateFile(RAM):
 File = (RAM)/20
 return File
def RAM_Space(File):
 RAM_space = File*20
 return RAM_space
 
print("#-------------- Welcome to Command My PC ----------------#")
print(" ")
select = str(input("Select programming language to start:"))
while select == 'Python 3' or select == 'python 3' or select == 'python3' \
 or select ==' Python 3' or select == ' python 3':
 print(">>> Programming Language Selected : ",select)
 print("Initializing ...")
 print("Starting in >>>")
 for x in range(1,4):
 print("%d"%(x),end=' ')
 sleep(1)
 break;
 sleep(1)
 clear_screen()
else :
 print(">>>Error.Programming Language Not Supported on this platform !!! \n"
 ">>>Return to START\n"
 ">>>Restart Application\n")
 sleep(5)
 clear_screen()
 exit()
print('\n')
print(">>>Command Menu<<<\n"
 "1.User Log In\n"
 "2.Information about system\n"
 "3.Exit\n")
choice = int(input(">>> Enter a choice :"))
if choice == 1 :
 name = str(input(">>>Please enter your name: "))
 proname = str(input(">>>Please enter your proname: "))
 user = str(input(">>>PC User : "))
 print("\n")
 login = str(input("~ Log in : Yes / No ? "))
 print("\n")
 if login == 'Yes' or login == 'yes' :
 print(">>> Command response ...")
 sleep(1)
 print(">>> Logged in successfully\n")
 sleep(1)
 print(">>> Please enter your PC model\n")
 pc = str(input(">>> PC model :"))
 if pc == 'dell' or pc == 'Dell' or pc == 'ASUS' \
 or pc == 'Asus' or pc == 'asus' or pc == 'Acer' \
 or pc == 'acer' or pc == 'Samsung' or pc == 'Toshiba' \
 or pc == ' dell' or pc == ' Dell' or pc == ' ASUS' \
 or pc == ' Asus' or pc == ' asus' or pc == ' Acer' \
 or pc == ' acer' or pc == ' Samsung' or pc == ' Toshiba':
 print(">>> Command response ...")
 sleep(1)
 print(">>>User",name,proname,",your PC is accepted to Hardware
Testing\n")
 print(">>>Please initialize CPU !")
 cpu = str(input(">>>Enter command : "))
 if cpu == 'F_CPU' :
 print(">>> Command response ...")
 sleep(1)
 print(">>> Feedback : Command entered ,", cpu,"\n")
 else :
 print(">>> Error , enter valid command to initialize CPU")
 exit()
 print(">>> Please, set frequency !")
 frequency = int(input(">>> Frequency [MHz] : "))
 if frequency >= 8000000 and frequency<=32000000 :
 print(">>> Command response ...")
 sleep(1)
 print(">>> Feedback : Frequency entered ,", frequency,"\n")
 print(">>> Final Command to initialize CPU
:",cpu,frequency,"UL")
 print("Initializing ...")
 print("Starting in >>>")
 for y in range(1, 4):
 print("%d" % (y), end=' ')
 sleep(1)
 print(">>>(System x64) CPU initialized successfully !\n")
 else :
 print(">>> Error , enter valid frequency !")
 exit()
 print(">>>Checking RAM & ROM Memory ...")
 sleep(3)
 RAM = int(input(">>>Introduce RAM size [GB] : "))
 ROM = int(input(">>>Introduce ROM size [GB]: "))
 if RAM>=8 and RAM<=32 :
 print(">>> RAM Memory accepted !")
 else :
 print(">>> Invalid RAM Memory !")
 exit()
 if ROM>=256 and ROM<=1024 :
 print(">>> ROM Memory accepted !\n")
 else :
 print(">>> Invalid ROM Memory !")
 exit()
 print(">>>Please initialize Registers using Assembly Language !")
 command = str(input(">>>Enter command : "))
 if command == 'ldaa':
 print(">>> Command response ...")
 sleep(1)
 print(">>> Feedback : Command entered ,", command, "\n")
 else:
 print(">>> Error , enter valid command to initialize registers")
 exit()
 print(">>> Please, set registers !")
 register = str(input(">>> register : "))
 if register == 'x[SCDR]':
 print(">>> Command response ...")
 sleep(1)
 print(">>> Feedback : Register set ,", register, "\n")
 print(">>> Final Command to initialize Registers from Memory :",
command, register)
 print("Initializing ...")
 print("Starting in >>>")
 for z in range(1, 4):
 print("%d" % (z), end=' ')
 sleep(1)
 print(">>>(System x64) Registers initialized successfully !\n")
 else:
 print(">>> Error , enter valid command !")
 exit()
 sleep(2)
 print(">>> Wait ...")
 sleep(3)
 print(">>> Create a file (.exe) !")
 filename = str(input(">>> File name : "))
 filesize = int(input(">>> File size [MB] : "))
 if filesize<=RAM :
 print(">>> File",filename,"created successfully !")
 print(">>> RAM Space required [MB]:",RAM_Space(filesize),"\n")
 print(">>> Process Finished Successfully !")
 else :
 print(">>> Error , file size > RAM size")
 exit()
 else :
 print(">>> Error , Enter valid PC type!")
 elif login == 'No' or login == 'no' :
 print(">>> Command response ...")
 sleep(1)
 print(">>> Not logged in !\n")
 exit()
 else:
 exit()
elif choice == 2:
 print(">>> System name : Command my PC")
 print(">>> OS : Windows 10 Pro")
 print(">>> Development Engineer : Bruma Mihai")
 print(">>> Programming Language : Python 3")
 print(">>> IDLE Python 3")
else :
 print(">>> Process exited !")
 exit()
#----------------------
