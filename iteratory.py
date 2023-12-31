from dataclasses import dataclass
from collections.abc import Iterable
from typing import List

@dataclass
class Simple:
    field1:str
    field2:int

sm = Simple("Jacek",55)
print(sm.field2)
print(sm)

# for x in sm:
#     print(x)

print(isinstance(sm,Iterable))
print(isinstance([3,2,5,7],Iterable))

print("_"*40)

@dataclass
class Employee:
    fisrtname:str
    lastname:str
    accepted:bool = False


@dataclass
class Company:
    name:str

    def __post_init__(self):
        self._employees:List[Employee] = []

    def hire_employee(self,employee:Employee):
        self._employees.append(employee)

    def fire_employee(self,employee:Employee):
        self._employees.remove(employee)

    def __iter__(self):
        return iter(filter(lambda x:x.accepted, self._employees))

first_employee = Employee('Paweł','Kot',True)
second_employee = Employee('Olga','Nowak',True)
third_employee = Employee('Olaf','Kowal')


company = Company('ABC')
company.hire_employee(first_employee)
company.hire_employee(second_employee)
company.hire_employee(third_employee)

for emp in company:
    print(emp)


company.fire_employee(first_employee)

print("usunięcie rekordu...")

for emp in company:
    print(emp)
