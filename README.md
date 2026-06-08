# MScBath_FlightManagement

Implementation of a Flight Management Database that holds relevant data and enables staff members to easily interact with it.  

Operation:
- Run the FlightManagementDB_CLI.py script to execute the Command Line Interface and follow the instructions displayed
- FlightManagementDB_queries.py contains all the queries to the underlying database.  Do not run this script.
- FlightManagementDB.db is the database produced by main.sql.  Do not run/adjust any of these files.  

Unit Testing:
- All actions that make changes to the database have an equivalent Unit Test (pytest) in test_unittests.py file.  This includes:
    - Adding a New Flight
    - Changing the Status of a Flight
    - Changing the Assignment of a Pilot
- The Unit Tests can be run by typing 'pytest -q' in the Terminal

Limitations:
- There is no single command to exit back to the Main Menu.  So user needs to follow through each option before being passed back to the Main Menu. 

