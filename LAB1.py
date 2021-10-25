class Person:
    moods = ("happy", "tired", "lazy")

    def __init__(self, money=0, mood=moods[0], healthRate=0, name="Samy"):
        self.name = name
        self.money = money
        self.mood = mood
        self.set_healthRate(healthRate)

    def set_healthRate(self, health):
        if not (health >= 0 and health <= 100):
            raise ValueError("Health Rate is unvalid")
        self._healthRate = health

    def get_healthRate(self):
        return self._healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours > 7:
            self.mood = "Lazy"
        else:
            self.mood = "tired"

    def eat(self, meals):
        if meals == 3:
            self._healthRate = 100
        elif meals == 2:
            self._healthRate = 75
        else:
            self._healthRate = 50

    def buy(self, items):
        self.money -= items * 10


class Car:
    def __init__(self, fuelRate=0, velocity=0, name="fiat 128"):
        self.name = name
        self.set_fuelRate(fuelRate)
        self.set_velocity(velocity)

    def set_fuelRate(self, fuel):
        if not (fuel >= 0 and fuel <= 100):
            raise ValueError("The Fuel Rate is unvalid")
        self._fuelRate = fuel

    def get_fuelRate(self):
        return self._fuelRate

    def set_velocity(self, velocity):
        if not (velocity >= 0 and velocity <= 200):
            raise ValueError("The velocity is unvalid")
        self._velocity = velocity

    def get_velocity(self):
        return self._velocity

    def stop(self, d):
        self._velocity = 0
        if d == 0:
            return 1
        else:
            return 0

    def run(self, veloctiy, distance):
        var = distance // 10
        i = 0
        while i < var:
            self._fuelRate -= 0.1 * self._fuelRate
            distance -= 10
            i += 1
        self._velocity = veloctiy
        if self._fuelRate <= 0:
            self.stop(distance)
        else:
            self.stop(0)


class Employee(Person):
    def __init__(self, id, salary, car: Car,
                 distanceToWork=20, email="samy@mail.com", *args):
        super().__init__(*args)
        self.id = id
        self.car = Car()
        self.set_email(email)
        self.distanceToWork = distanceToWork
        self.set_salary(salary)

    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError("Salary must be between 0 to 100")
        self._salary = salary

    def get_salary(self):
        return self._salary

    def set_email(self, email):
        if not email[email.find("@"):] == "@mail.com":
            raise ValueError("Email Not Valid")
        self._email = email

    def get_email(self):
        return self._email

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "Lazy"

    def send_email(self, to, subject, msg, receiver_name):
        with open("email.txt", "a") as email:
            email.write("From: {}".format(self.get_email()))
            email.write("\nTo: {}@mail.com\n".format(to))
            email.write("\nHi, {}\n{}\n".format(receiver_name, msg))
            email.write(subject + "\n\n")

    def drive(self, distance):
        obj = Car()
        obj.run(obj._velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.set_fuelRate(self.car.get_fuelRate() + gasAmount)
        if self.car.get_fuelRate() > 100:
            self.car.set_fuelRate(100)


class Office:

    employeesNum = 0

    def __init__(self, employees: Employee = {}, name="ITI Smart Village"):
        self.name = name
        self.employees = employees
        Office.employeesNum += len(employees)

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empid):
        return self.employees[empid]

    def hire(self, employee):
        obj = Employee(0, 1000, "fiat")
        obj.id = employee.id
        self.employees[employee.id] = obj
        obj.set_salary(employee._salary)
        obj.car = employee.car
        obj.distanceToWork = employee.distanceToWork
        obj.set_email(employee._email)
        obj.money = employee.money
        obj.mood = employee.mood
        obj.name = employee.name
        obj.set_healthRate(employee._healthRate)
        Office.employeesNum += 1

    def fire(self, empid):
        del self.employees[empid]
        Office.employeesNum -= 1

    def deduct(self, empid, deduction):
        self.get_employee(empid)._salary -= deduction

    def reward(self, empid, reward):
        self.get_employee(empid)._salary += reward

    @ staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        obj = Car()
        obj.run(velocity, distance)

    def check_lateness(self, empid, moveHour):
        distance = self.get_employee(empid).distanceToWork
        targetHour = 9
        time = targetHour - moveHour
        velocity = distance / time
        var = Office.calculate_lateness(
            targetHour, moveHour, distance, velocity)
        if var:
            self.reward(empid, 10)
        else:
            self.deduct(empid, 10)

    @ classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num


obj = Employee(1222, 1500, "fiat", 20, "samy@mail.com", 1000, "happy", 100)
obj1 = Employee(1522, 1500, "fiat", 20, "samy@mail.com", 1000, "happy", 100)
obj2 = Employee(1622, 5000, "fiat", 20, "samy@mail.com", 1600, "happy", 100)
obj3 = Employee(1322, 1500, "fiat", 20, "samy@mail.com", 1000, "happy", 100)
obj4 = Employee(1722, 1500, "fiat", 20, "samy@mail.com", 1000, "happy", 100)
obj5 = Employee(1822, 1500, "fiat", 20, "samy@mail.com",
                1000, "happy", 100, "MOhammed")
obj6 = Employee(1922, 1500, "fiat", 20, "samy@mail.com", 1000, "happy", 100)
office = Office()
office.hire(obj)
office.hire(obj1)
office.hire(obj2)
office.hire(obj3)
office.hire(obj4)
office.hire(obj5)
office.hire(obj6)
office.fire(1922)
obj2.refuel()
print(obj1.car.get_fuelRate())
print(office.get_employee(1622).get_salary())
office.check_lateness(1622, 8.55)
print(office.get_employee(1622).get_salary())
