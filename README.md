# acme-challenge
## ACME Employee Pay Calculator
This repository contains a Python solution for calculating the total payment to ACME employees based on their shift hours and a rates dictionary. This project is part of a coding challenge for a position as a data engineer on ioet. The constraint for this challenge was the use of pure Python. The use of libraries installed through PIP was not allowed.

### Overview
The approach to solving this challenge was the creation of two files:
pay_calculator.py: that contains the PayCalculator class. This class provides methods for calculating the payment based on an employee's work schedule received as a text file. 
main.py: that is the main script that reads the employee schedules,  calculates the payment using the PayCalculator class, and prints the results.

### Architecture
- The PayCalculator class is responsible for parsing input data and calculating the payment for each employee. It takes a dictionary of rates for each day of the week and time window as an argument during initialization.
- The calculate_pay method calculates the payment for an employee based on their name and schedule. It uses helper methods to parse time ranges, calculate the number of worked hours, and determine the correct rate for each shift.
- The main.py script reads the employee schedules from a text file named employee_schedule.txt. It initializes the PayCalculator class with the rates and uses it to calculate the payment for each employee. The results are printed to the console.

### How to Run the Program Locally
**Prerequisites**
- Python 3.6 or higher

**Running the program**

1. Clone this repository:

``` git clone ```

2. Change to the repository directory:

``` cd ```

3. Run the main.py script:

``` python main.py ```

The output will display the amount to pay each employee, as shown in the example below:

``` The amount to pay RENE is: 215 USD ```

``` The amount to pay ASTRID is: 85 USD ```
