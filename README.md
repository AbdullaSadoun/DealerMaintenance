This is our Project #1 for ENGM4620 (Intro to Python for Engineers)

## Introduction and Purpose: 
The main purpose of this software is to aid and automate the process of maintenance and service for dealerships and garages. The software will help administrators, mechanics and customers swiftly book appointments and check compatibility, estimated time and pricing for the required services. Mechanics should be able to view their schedules for the day, admins can edit and update records of available services and “maintainable” vehicles. Car owners can input their vehicle model, make and pick the service they need and would receive a “receipt” or invoice with the cost estimate and time.

## Objectives
- Demonstrate knowledge in using python to complete projects
- Demonstrate knowledge in various concepts introduced with the language, this includes but is not limited to
  - Basic Syntax and features
  - Use of basic concepts like looping, comparison etc.
  - Funcitons and increasing code readability
  - File Handling
  - Object Oriented Programming
  - Creating Classes and Methods
  - Inheritance
  - Data Structures
  - Creating Databases

## Requirements
-Python3 installed
-All required .txt files
	-“availserv.txt”
	-“Vehicle_table.txt”
-PrettyTable python Library
-Models.py and main.py should be in the same directory

## How to use
After ensuring that you have all the required programs, files and libraries installed and put in the same directory, you will start by running the software by navigating to the directory in your computer where you have stored all the required files. This can be done by using cd “path_to_your_directory” then hit enter. To check if you are in the correct directory, type in “ls” in your terminal and then you should see the following files:
“main.py”, “model.py”, “availserv.txt”, “vehicle_table.txt”.
Once you have navigated to the correct directory, use: “python3 main.py” to run your code, if you are using an IDE, then there should just be run button to automate this process for you. 
Once you have completed this, you should be ready to use the software, note that most of the navigation done within the software only involves the use of the keyboard (mainly numbers) to navigate and the rest of the characters to enter information. 

## Design
For the design of the software we have included a figure0 (format taken from System Analysis). The figure 0 mainly highlights the different processes, stores and terminators that are used by the software. It highlights the different systems and how they interact with each other to come up with the intended solution and features.

Figure 0: Software Flowchart (included in project directory)

## Implementation
The features we had in mind were successfully implemented. In an ideal scenario, the program has proven useful in saving cost and time for the dealership. 
Some of the features we missed out on include: creating a more friendly user interface, writing to an actual database or searching through binary files to save space and memory usage so we do not have to load the entire tables on memory when not used. This would also decrease complexity and compiling time. Since the files would be in binary too, they would save more space than text files that we are using right now.
We also met most of the objectives listed in the objectives part. Connecting to an actual database with query language would’ve been ideal but the learning curve was a bit too steep for the duration of time we had at hand.


## Testing
### Test 1: Inputting new records
Purpose/Objective: The purpose of this test is to see whether the program saves the new records added to the vehicle table and the available services table between runs. 
Test Configuration: I have run the program and went into admin mode, I then will add a new record to the vehicle table (new car that can be serviced) and I will also add a new service that the dealership can now do. The software will “remember” my new records for future runs
Expected Results: The software should have no problems saving the new record to the table and then using them again when I rerun the program.
Actual Results: The program passed the test and successfully added and remember the records between runs
Pass/Fail: Pass
### Test 2: Deleting Previous Records
Purpose/Objective: The purpose of this test is to see if the deleting records functionality of the system works properly and deleted records are permanently removed from the system even between runs.
Test Configuration: I will run the program in admin mode, try deleting a record from the vehicle table and a record from the services table, once done, I’ll view the tables making sure they are deleted from the programs memory then I will rerun the program, go to admin mode and check the tables to see that the record specified are still deleted.
Expected Results: The program should be able to delete the records and remember the new updated tables.
Actual Results: The program successfully got rid of the deleted records and managed to remember the lists after the update.
Pass/Fail: Pass
### Test 3: Trying to overbook mechanic
Purpose/Objective: The purpose of this test is to check whether the functionality of finding an available time slot for the mechanic works.
Test Configuration: I will try to book 2 different appointments on the same day and then I’ll check the schedule to see if they are assigned at different times.
Expected Results: I think this part of the code did not work properly during the implementation and might fail the test
Actual Results: The program failed to assign different times for the service appointments and overbooked the mechanic
Pass/Fail: Fail
### Test 4: Customer entering car that’s not in list
Purpose/Objective: This main objective of this test is to see how the program reacts when the user enters a car that is not in the table and can’t be serviced in the dealership
Test Configuration: I will run the software as a car owner, I will then try to input a car model that is not in the list, I will also conduct the test with having a car whose make is on the list but its model is not.
Expected Results: I expect the program to print the “sorry car not available message” for both cases.
Actual Results: The program passed both tests, it did as expected printing: “Sorry, we do not have any services available for your car.” for both cases
Pass/Fail: Pass

## Comparison to a Similar Solution
The team decided to conduct a comparative analysis of our project in relation to ARI, an online auto repair shop software.
 ARI offers an array of features designed to assist mechanic shops and technicians in efficiently managing maintenance logs, estimating costs, and tracking recalls for automobiles through cloud-based databases.
The project shares several features with ARI such as:
Ability to generate cost estimates for services provided
Maintenance of a list of supported car models, editable by administrators
Creation of maintenance schedules for individual clients and their vehicles
Contrary to the similarities, ARI offers a more extensive list of features which give it an advantage on our project, some examples of those differences are:
Our project does not involve uploading or accessing cloud-based maintenance logs.
Currently, our project lacks a polished front end and offers fewer features.
Unlike ARI, we do not provide repair and maintenance video guides or additional tools for mechanics.
All the points made in the comparison between our project and ARI highlight the shared image between the two products, with ARI serving as an inspiration to what our project is capable of achieving with further development efforts and increased development times. ARI’s features offer ideas that can improve our product, and help guide the future trajectory of the project's development. 

## Contribution
The group initially planned on devising the tasks between both members with respect to their skills, with one group member focusing on the algorithms and the majority of coding, and the other member would work on integration mainly. After a few brainstorming sessions the group had in-person, it was decided that in-person collaborative approach suited the group better. 
The group therefore switched to in-person coding sessions using a single machine, which resulted in  a more dynamic work environment. Real time adjustments to the code, with debugging and improvements were faster, and both students were able to express ideas and suggest solutions in a more efficient way during the sessions. The group’s approach also limited the delays that may occur due to outdated cloud files or desync. 
Both students worked on the documentation and video recording, with real-time feedback communicated through the meetings. The responsibilities in drafting the project report and coding are shared equally between both students and we think that the approach we implemented worked perfectly for our small group.

## Conclusion and Reflections
In conclusion, this project was successful, but due to shortage of time and high course load, we were not able to implement all the features we originally planned on having in the project. We also couldn't optimize the code and make it more readable. This can be overcome next time with better planning, and with utilization methods like agile scrum. 
Future development of the project may be done if the group members decided on exploring the potential of this idea, and a plethora of features was originally intended to make it to the final project still on the roadmap . Although in the meantime, no future development is confirmed and the group will halt development after the project submission.

## References 
Solution Used for Comparison: https://ari.app/demo/
