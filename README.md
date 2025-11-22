# EmployeeManagement
Basic CRUD project to save/handle employee name and generate a random ID.


Made using VSCode version 1.106.1 for mac on apple sillicon.

<H1>EMPLOYEE MANAGEMENT SYSTEM</H1>


Overview:
 This project is a simple employee management system using the Pandas library for the csv/data retention and updating part on a locally stored csv file.

 Features:
  Has an admin panel to edit/remove employee ids.
  Saves the data to a local CSV file in realtime so that it can be shared if needed.
  Easy to understand UI
  Makes sure no single ID is assigned to two employees

Tools used:
  Pandas library to read and write to employees.csv
  random library so that each employee gets a random ID
  OS library to access file from local disk and clear screen when needed.

Steps to install & run:
  Go to the top middle under code and save the repo as a zip, then extract the zip file and run untitled12.py
  or clone this repository and run untitled 12.py in your python interpreter.
  Made in python version 3.14.0

Instructions for testing/use:
  Run the python file.
  Some example employees are added to the csv file, so that you can view list of employees by pressing 3 in the main menu (if you want).
  add employee by pressing 1.Add Employee in the main Manager Menu
  after inputting the name as a string, it should look like this:
  <img width="896" height="328" alt="image" src="https://github.com/user-attachments/assets/62c05689-1049-43b4-8946-45092b80f449" />
  The employee ID generated will be so results will not be the same as shown.
  You can manage employee name by pressing enter, and then 2. Update Employee in the Manager Menu.
  after inputting the password (default is: admin) you will get displayed list of employees and their ID.
  select the ID you want to change the name for.
  <img width="1256" height="470" alt="image" src="https://github.com/user-attachments/assets/7af1ac27-3fad-40eb-a2d6-c7f4976899c5" />
  The employee name will change to the new name in the local csv file and after you view the list again.
  <img width="916" height="442" alt="image" src="https://github.com/user-attachments/assets/560696cc-9d1c-4965-b9f8-c419ab75e082" />
  (As shown, Name1 became Name2)




  

