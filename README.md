# correccion_practicas
This script evaluates Java exercises downloaded from Blackboard

This scrip does the following tasks:
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
