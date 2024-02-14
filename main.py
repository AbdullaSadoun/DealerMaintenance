"""
Car Maintenance software that estimates the cost for a car's maintenance based 
on the car's model, age and mileage. Then it schedules a maintenance appointment
for the mechanic, it would show what his schedule looks like for the day.

The software should have the following features:
- The software should ask the user whether they are an admin, a mechanic or a car owner
- If the user is an admin, they should be able to add, update or delete car models and their tables
- If the user is a mechanic, they should be able to view the list of car models
- If the user is a car owner, they should be able to enter the car's model, year and mileage
- The software should then estimate the cost for the car's maintenance based on the car's model, age and mileage
- The software should display the estimated cost to the user
- The software should schedule a maintenance appointment for the car depending on the estimated time to maintain
- The software should display the maintenance appointment to the user

Available Maintenance Services:
- Oil Change and Lubrication Service
- Tire Services
- Brake Services
- Battery Inspection and Replacement
- Engine Diagnostic and Performance
- These will be the deafult options, the admin should be able to add, update or delete these services

The software should have the following tables:
- Car Models
- Maintenance Services
- Maintenance Schedule
- The tables should be stored in a database
- The software should be able to create the database if it does not exist
- The software should be able to connect to the database
- The software should be able to create the tables if they do not exist
- The software should be able to insert, update or delete records in the tables
- The software should be able to select records from the tables
- The software should be able to drop the tables
- The software should be able to drop the database
- The software should be able to close the connection to the database


"""
# Your code here

print("Welcome to the Car Maintenance software!") # welcome message

# Ask the user whether they are an admin, a mechanic or a car owner
user_type = input("Are you an car owner(1), a mechanic(2) or an admin(3)? ")

# If the user is an admin, they should be able to add, update or delete car models

if user_type == 3: # user is an admin
    print("You are an admin!!")
    print("What would you like to do?")
    print("1. Add car model")
    print("2. Update car model")
    print("3. Delete car model")
    admin_choice = input("Enter your choice: ")
    if admin_choice == "1":
        print("You chose to add a car model.")
        # Add car model
    elif admin_choice == "2":
        print("You chose to update a car model.")
        # Update car model
    elif admin_choice == "3":
        print("You chose to delete a car model.")
        # Delete car model
    else:
        print("Invalid choice.")
elif user_type == 2 #user is a mechanic
    print("You are a mechanic!!")
    #prompt to enter the day they wanna see the schedule for
    print("What day would you like to see the schedule for?")
    print("1. Monday")
    print("2. Tuesday")
    print("3. Wednesday")
    print("4. Thursday")
    print("5. Friday")
    mechanic_choice = input("Enter your choice: ")
    if mechanic_choice == "1":
        print("You chose to see the schedule for Monday.")
        #display the schedule for that day
    elif mechanic_choice == "2":
        print("You chose to see the schedule for Tuesday.")
        #display the schedule for that day
    elif mechanic_choice == "3":
        print("You chose to see the schedule for Wednesday.")
        #display the schedule for that day
    #display the schedule for that day
    


