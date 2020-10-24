# corregirEjercicio43
This script evaluates Java exercises downloaded from student's repositories

Syntax:
py corregirEjercicio43.py csv_path
csv_path is a csv file where each line contains information for each student and with two columns, the first is the student's name and the second one is the repository URI

This script does the following tasks:
* Delete an exercise file if exists and create it
* Read the csv file
* For each student:
  * Get the name and repository
  * Clone the repository inside exercise folder in a folder with the student's name without spaces
  * Read the makefile if exists, delete it and replace it with my own
  * Search and read each Java file
  * Execute Java main
* Create a log file with information from all students
* Create a file with the student's name to later add comments and the score

# corregirEjercicio14
This script evaluates Java exercises downloaded from Blackboard

This script does the following tasks:
* Unzip the file with the exercises dowloaded from Blackboard
* For each student's exercise:
  * Get the email and save it in log.txt
  * Unzip/unrar the exercises in a folder with the email
  * Save a tree of the folder content in log.txt
  * Check the file structure for packages and class files
  * If the structure is correct:
    * Save the content of Principal.java
    * Save and execute the command to compile the Java classes
    * Save and execute the command to execute the programm
