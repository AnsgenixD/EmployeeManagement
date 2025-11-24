

Problem statment:

  Making a scalable database of employee names and assign them IDs randomely.
  1. Making it efficient.
  2. Making sure no ID is conflicting with another employee.
  3. Only admins are allowed to edit employee details.
  4. Make it efficient.

Scope of the project:
  This project uses python to perform CRUD operations on employee data.
  The scope is:
    1. It stores data locally so that it can be accessed even after execution.
    2. It creates unique IDs for each employee, ensuring no ID is shared between two employees.
    3. Managing/changing employee data requires a password which keeps the data safe.
  Furthermore the scope can be broadened to include a GUI, along with more employee data, like logging hours, etc.
  
Target Users:

  Small business managers: who need an efficient free of cost way to log employees.
  Team Managers: Who need to maintain a list of team members and their IDs.
  

High-level features:
  CLI interface: A clean-clear and easy to understand CLI-interface that allows users to navigate between Add, Update, and View modes easily.
  Duplicate checking: Makes sure the generated random ID between 1000-9999 does not exist already.
  Secure Update: an Admin password required to change employee details.
  Real time data processing: Updates information in real time and stores it on a persistant csv file which ensures no issues occur.
