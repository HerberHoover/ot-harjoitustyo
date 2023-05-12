# Testing Documentation


### Unit and integration testing

The classes responsible for the application logic, such as User, Category, Transaction, and Balance were tested. In these tests, dependencies were mocked with fake repositories storing information in memory instead of a real database.


### Repository classes

The database interactions were tested ensuring that the application correctly stored and retrieved data.

Each of these test cases used the patch decorator to replace methods or functions with mock objects, and assertions were made to verify these methods are called with the expected arguments and return the expected results



### Testing Coverage

The testing coverage was 78 % 

{kuva}


### User Interface Testing 

The testing of the user interface of the application has been performed manually 

### Installation and configuration

The application has been dowloaded and tested as described on macOS, Linux and  Windows Subsystem for Linux.

### Functionalities

All the functionalities listed in the requirements specification document and user manual have been gone thorugh also with inappropriate inputs, like empty fields, ensuring comprehensive validation.
