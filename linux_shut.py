import os

c = input(print("Do you want to shutdown your pc(yes/no)\n"))

if c=='no':

   print("Exiting the program\n")
   exit()
else:   
    os.system('systemctl poweroff') 
