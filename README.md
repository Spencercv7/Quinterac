# Quinterac
Simple banking system application created for CISC 327 - Software Quality Assurance
Created with a focus of using an AGILE approach to test-driven software development

The repository contains the source files for this project and will be added to throughout the development process

## Table of Contents
- [Deploying Application](#deploying-application)
- [Folder Structure](#folder-structure)
- [Testing](#testing)
- [Front-End Implementation](#front-end-implementation)
- [Back-End Implementation](#back-end-implementation)
- [Naming Convention](#naming-conventions)
- [Authors](#authors)

## Deploying Application

These instructions will get you a copy of the application running on your local machine

### Prerequisites
The following will need to be installed on your local environment
- [Bash](https://www.windowscentral.com/how-install-bash-shell-command-line-windows-10)
- [Python](https://www.python.org/downloads/)

### Installing
(documentation to come)

## Folder Structure
The basic structure is:
```
├── Front_End_Designs.pdf               // contains information about the design and implemenation of the front end 
│                              
├── Test_Plan_Document.pdf              // contains an overview of the testing process and information on every test case                  
│  
│  
├── testing   
│     │                
│     ├─ back_end 
│     │    ├─ master_account_file       //contain pdfs outline the test cases regarding the files the folders are
│     │    ├─ merge_transaction_file    //named after, will also contain the test scripts for these test cases
│     │    ├─ transaction_summary_file
│     │    └─ valid_account_file 
│     │
│     └─ front_end 
│          ├─ create_account            //contain pdfs outline the test cases regarding the functionalities the folders
│          ├─ delete_account            //are named after, will also contain the test scripts for these test cases
│          ├─ deposit
│          ├─ withdraw
│          ├─ transfer
│          ├─ login
│          └─ logout
│
└─ front_end     //contains bash script frontend.sh that is run to start the application
      │          //holds transaction_summary.txt and valid_account_file.txt to track bank information and transactions
      │                
      └─ objects //contains specialized objects that contain groupings of useful methods to be used in the front_end

```

## Testing
Since we wanted to do test-driven development we wrote out all the test cases before writing any code. The tests were then documented in .pdf files that are organized into folders nested in the testing folder. We will then write out test scripts for each described test case in these pdfs. 

### Running the Tests
(documentation to come)

## Front-End Implementation
Our solution uses an object oriented approach with specialized objects that contain groupings of useful methods. 
The are four objects used by the frontend Python script. 
- SessionHandler object tracks the state of the session and handles the users input and the flow of the frontend.
- InputValidation object holds methods that check if given account numbers, names and monetary amounts are in a valid format.
- TransactionSummary object contains a reference to the transaction summary text file and methods that write transactions in the correct format to the file.
- ValidAccounts object takes in a valid account file and stores the accounts in the file in a dictionary that it adds and deletes accounts from. 

## Back-End Implementation
(documentation to come)

## Naming Conventions
Used Standard Python Naming Conventions
![alt text](https://i.stack.imgur.com/Ty2F3.png)

## Authors
- Ben Lammers (ben.lammers@queensu.ca)
- Spencer Venable (16scpv@queensu.ca)
