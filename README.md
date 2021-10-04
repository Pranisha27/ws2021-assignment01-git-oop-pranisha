# Advanced Software Technology Assignment 01
This is the first assignment of the Advanced Software Technology course.

One of the most important aspects of working with other developers in a project is keeping track of the changes made in the code base. Git is a useful tool for this task, since it makes it easy to manage changes made to a code base over time. Through git, we can find information regarding changes, such as what changed, when did it change, and who changed it.

## Learning Objectives
The student
- knowns the basics workflow of GitHub Classroom.
- is aware of the structural frame for the assignments in the module Advanced Software Technology.
- is familiar with the assignment rules
- understands Core Git concepts like *commit*, *push*, *pull* and *merge*.
- knows Object Oriented Programming concepts and how to apply them using Python

## Task
### Outline
Consider that you are responsible for a large warehouse. After long years of operation the current [COBOL](https://en.wikipedia.org/wiki/COBOL) based oder management system should be replaced in order to make it capable of communicating with the python based robot automation platform that was bought a few months ago without taking the current system landscape into consideration. Since the management decided that a complete rework of the system is not required you are now tasked with rebuilding the old system in python based on a class diagram the admins found in some documentation of the old system.
### Instructions
The deliverable of this assignment is an implementation of the system described using a plantuml class diagramm as well as a small report written in Markdown. The report template is available in this repository under `./git/report.md` and the plantuml class diagramm can be found [here](./order_management_system/order_management_system.svg).
1. All group members should clone the repository to their local machine using `git clone`, after which all members should develop some parts of the system. You may assign which member will develop which part by using **any** criteria.
1. Create a new *feature branch* for every functionality of the order management system that you implement.
1. Please farmiliarize yourself with the **abc module** as well as the general concept of **Abstract Base Classes** in python and use them to implement the described system in an **Object Oriented** manner (please look at the [resources](#resources) attached below).
1. Every commit of changes should have a meaningful message, and be *pushed* to the respective branch on the remote repository.
1. After some functionality is considered to be completed, create a *Merge Request* in **GitHub** to merge the respective *feature branch* into the *master/main* branch of the project.
1. Using git commands, find asweres to the following questions:
   - Who modified/developed which part of the system?
   - When was which part completed?
   - What are merge commits? Identify them in your repository.
   - What is the *commit ID* of the *commit* that introduces the `Customer` abstract class?
   - What message did the commit include?
   - What are the differences between the last two commits pushed to the remote repository?
1. Make two team members modify the same line of code, commit their changes and *pull*/*push*. What happened? How did you resolve it? Write it on the report.
1. Include a screenshot of the output of the command `git log --oneline--graph --decorate --all` into the report and provide a **short describtion** of what it visualizes.

## Resources
- [PEP 3119 - Introducing Abstract Base Classes](https://www.python.org/dev/peps/pep-3119/)
- [abc module documentation](https://docs.python.org/3/library/abc.html)
- Example Usage of the `abc module` can be found in `./birdsnaeroplanes.py`