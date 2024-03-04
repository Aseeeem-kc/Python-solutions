// 1. Point Class
// Define a class Point with constructor setting coordinates (x, y). Create an instance, print its coordinates.

class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

// Example Usage:
let point1 = new Point(3, 4);
console.log(point1.x, point1.y); // Output: 3 4



// 2. Person Class
// Create Person class with constructor setting name, age. Make instance, print details.

class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

// Example Usage:
let person1 = new Person("John", 30);
console.log(person1.name, person1.age); // Output: John 30




// 3. Set Student Name
// Create a class named Student with a method set_name to set the student's name

class Student {
    set_name(name) {
        this.name = name;
    }
}

// Example Usage:
let student1 = new Student();
student1.set_name("Alice");
console.log(student1.name); // Output: Alice



// 4. Set Rectangle Height and Width
// Define a class called Rectangle with methods set_width and set_height to set the dimensions of the rectangle.

class Rectangle {
    set_width(width) {
        this.width = width;
    }

    set_height(height) {
        this.height = height;
    }
}

// Example Usage:
let rectangle1 = new Rectangle();
rectangle1.set_width(5);
rectangle1.set_height(10);
console.log(rectangle1.width, rectangle1.height); // Output: 5 10





// 5. Add Numbers in Calculator Class
// Create a class named Calculator with a method add to add two numbers.

class Calculator {
    add(num1, num2) {
        return num1 + num2;
    }
}

// Example Usage:
let calculator1 = new Calculator();
let result = calculator1.add(3, 5);
console.log(result); // Output: 8





// 6. Bank Account Class
// Define a class called BankAccount with methods set_balance and deposit to manage a bank account's balance.

class BankAccount {
    set_balance(balance) {
        this.balance = balance;
    }

    deposit(amount) {
        this.balance += amount;
    }
}

// Example Usage:
let account1 = new BankAccount();
account1.set_balance(1000);
account1.deposit(500);
console.log(account1.balance); // Output: 1500





// 7. Student Class with Method
// Create a Student class with constructor initializing name and age. Implement a method display_info() to print student details. Create an instance, call the method.

class Student {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    display_info() {
        console.log("Name:", this.name);
        console.log("Age:", this.age);
    }
}

let student2 = new Student("Alice", 20);
student1.display_info();
// Output:
// Name: Alice
// Age: 20




// 8. Bank Account Class with Methods
// Define a BankAccount class with constructor setting account balance. Implement methods deposit() and withdraw() to modify balance. Create an instance, deposit some money, withdraw some money, and print the final balance.

class BankAccount {
    constructor(balance = 0) {
        this.balance = balance;
    }

    deposit(amount) {
        this.balance += amount;
    }

    withdraw(amount) {
        this.balance -= amount;
    }
}

let account2 = new BankAccount(1000);
account1.deposit(500);
account1.withdraw(200);
console.log("Final Balance:", account1.balance); // Output: Final Balance: 1300




// 9. Temperature Converter Class with Methods
// Create a TemperatureConverter class with constructor setting temperature in Celsius. Implement methods to_fahrenheit() and to_kelvin() to convert temperature. Create an instance, convert the temperature to Fahrenheit and Kelvin, and print the results.

class TemperatureConverter {
    constructor(celsius) {
        this.celsius = celsius;
    }

    to_fahrenheit() {
        return (this.celsius * 9/5) + 32;
    }

    to_kelvin() {
        return this.celsius + 273.15;
    }
}

let temp = new TemperatureConverter(25);
console.log("Temperature in Fahrenheit:", temp.to_fahrenheit()); // Output: Temperature in Fahrenheit: 77
console.log("Temperature in Kelvin:", temp.to_kelvin());         // Output: Temperature in Kelvin: 298.15




// 10. Employee Class with Salary Calculation Method
// Define an Employee class with constructor setting employee's name and hourly rate. Implement a method calculate_salary(hours) to calculate the employee's salary based on hours worked. Create an instance, calculate the salary for 40 hours worked, and print the result.

class Employee {
    constructor(name, hourlyRate) {
        this.name = name;
        this.hourlyRate = hourlyRate;
    }

    calculateSalary(hours) {
        return this.hourlyRate * hours;
    }
}

let employee1 = new Employee("John", 20);
let salary = employee1.calculateSalary(40);
console.log("Salary for 40 hours worked:", salary); // Output: Salary for 40 hours worked: 800
