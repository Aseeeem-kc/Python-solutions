// 1. Point Class
// Define a class Point with constructor setting coordinates (x, y). Create an instance, print its coordinates.

public class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public static void main(String[] args) {
        Point point1 = new Point(3, 4);
        System.out.println(point1.x + " " + point1.y);  // Output: 3 4
    }
}



// 2. Person Class
// Create Person class with constructor setting name, age. Make instance, print details.

public class Person {
    String name;
    int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public static void main(String[] args) {
        Person person1 = new Person("John", 30);
        System.out.println(person1.name + " " + person1.age);  // Output: John 30
    }
}



// 3. Set Student Name
// Create a class named Student with a method set_name to set the student's name

public class Student {
    String name;

    public void set_name(String name) {
        this.name = name;
    }

    public static void main(String[] args) {
        Student student1 = new Student();
        student1.set_name("Alice");
        System.out.println(student1.name);  // Output: Alice
    }
}





// 4. Set Rectangle Height and Width
// Define a class called Rectangle with methods set_width and set_height to set the dimensions of the rectangle.

public class Rectangle {
    int width;
    int height;

    public void set_width(int width) {
        this.width = width;
    }

    public void set_height(int height) {
        this.height = height;
    }

    public static void main(String[] args) {
        Rectangle rectangle1 = new Rectangle();
        rectangle1.set_width(5);
        rectangle1.set_height(10);
        System.out.println(rectangle1.width + " " + rectangle1.height);  // Output: 5 10
    }
}



// 5. Add Numbers in Calculator Class
// Create a class named Calculator with a method add to add two numbers.

public class Calculator {
    public int add(int num1, int num2) {
        return num1 + num2;
    }

    public static void main(String[] args) {
        Calculator calculator1 = new Calculator();
        int result = calculator1.add(3, 5);
        System.out.println(result);  // Output: 8
    }
}




// 6. Bank Account Class
// Define a class called BankAccount with methods set_balance and deposit to manage a bank account's balance.

public class BankAccount {
    int balance;

    public void set_balance(int balance) {
        this.balance = balance;
    }

    public void deposit(int amount) {
        this.balance += amount;
    }

    public static void main(String[] args) {
        BankAccount account1 = new BankAccount();
        account1.set_balance(1000);
        account1.deposit(500);
        System.out.println(account1.balance);  // Output: 1500
    }
}



// 7. Student Class with Method
// Create a Student class with constructor initializing name and age. Implement a method display_info() to print student details. Create an instance, call the method.

public class Student {
    String name;
    int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void display_info() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    public static void main(String[] args) {
        Student student1 = new Student("Alice", 20);
        student1.display_info();  
        // Output:
        // Name: Alice
        // Age: 20
    }
}





// 8. BankAccount Class with Methods
// Define a BankAccount class with constructor setting account balance. Implement methods deposit() and withdraw() to modify balance. Create an instance, deposit some money, withdraw some money, and print the final balance.

public class BankAccount {
    int balance;

    public BankAccount(int balance) {
        this.balance = balance;
    }

    public void deposit(int amount) {
        this.balance += amount;
    }

    public void withdraw(int amount) {
        this.balance -= amount;
    }

    public static void main(String[] args) {
        BankAccount account1 = new BankAccount(1000);
        account1.deposit(500);
        account1.withdraw(200);
        System.out.println("Final Balance: " + account1.balance);  // Output: Final Balance: 1300
    }
}





// 9. Temperature Converter Class
// Create a TemperatureConverter class with constructor setting temperature in Celsius. Implement methods to_fahrenheit() and to_kelvin() to convert temperature. Create an instance, convert the temperature to Fahrenheit and Kelvin, and print the results.

public class TemperatureConverter {
    double celsius;

    public TemperatureConverter(double celsius) {
        this.celsius = celsius;
    }

    public double to_fahrenheit() {
        return (this.celsius * 9/5) + 32;
    }

    public double to_kelvin() {
        return this.celsius + 273.15;
    }

    public static void main(String[] args) {
        TemperatureConverter temp = new TemperatureConverter(25);
        System.out.println("Temperature in Fahrenheit: " + temp.to_fahrenheit());  // Output: Temperature in Fahrenheit: 77.0
        System.out.println("Temperature in Kelvin: " + temp.to_kelvin());          // Output: Temperature in Kelvin: 298.15
    }
}



// 10. Employee Class with Salary Calculation Method
// Define an Employee class with constructor setting employee's name and hourly rate. Implement a method calculate_salary(hours) to calculate the employee's salary based on hours worked. Create an instance, calculate the salary for 40 hours worked, and print the result.

public class Employee {
    String name;
    int hourlyRate;

    public Employee(String name, int hourlyRate) {
        this.name = name;
        this.hourlyRate = hourlyRate;
    }

    public int calculate_salary(int hours) {
        return this.hourlyRate * hours;
    }

    public static void main(String[] args) {
        Employee employee1 = new Employee("John", 20);
        int salary = employee1.calculate_salary(40);
        System.out.println("Salary for 40 hours worked: " + salary);  // Output: Salary for 40 hours worked: 800
    }
}
