from oldresistor import OldResistor

print("_____________ Klasa OldResistor ______________")
r0 = OldResistor(10.2E3)
print(r0)
print(r0.get_ohms())
r0.set_ohms(2.88E2)
print(r0.get_ohms())
