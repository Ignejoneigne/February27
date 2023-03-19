#AUDIT SYSTEM

import os
import datetime
from datetime import date


#Adding personal info and current date, including time when info was entered.

name = input("Enter your name: ")
surname = input("Enter your surname: ")
id = input("Enter your personam ID number:  ")
id = int(id)


current_date = date.today().strftime("%Y-%m-%d")
current_time = datetime.datetime.now().strftime("%c")


lines = [name, surname, id]


#Creating new file/directory named as YYYY-MM-DD

folder_path = ("/home/sgtuser/python_environment/February27/audit_system/")
path = os.path.join(folder_path + str(current_date))


if not os.path.exists(path):
    os.mkdir(path)


#Creating text file named as ID number and date

txt_name = f"{id}.txt"
txt_path = os.path.join(path, txt_name)


#Adding content to the .txt file and reading created .txt

with open(txt_path, "a+") as f:
    f.write(f"\n{name}")
    f.write(f"\n{surname}")
    f.write(f"\n{id}")
    f.write(f"\n{current_time}")
    f.seek(0)




#Calling the close

with open(txt_path) as f:
    contents = f.readlines()


#Printing added user info
print("Your name, surname and personal ID number was saved successfully. Please check if everything is correct:", "\nNAME: ", str(name), "\nSURNAME: ", str(surname), "\nPERSONAL ID NUMBER: ", str(id))
print("Information was saved: ", current_time, "\n", txt_path)

confirmation = input("If everything is correct please enter OK. Otherwise start over: ")
if confirmation.upper() == "OK":
    print("Thank you for your time!")










