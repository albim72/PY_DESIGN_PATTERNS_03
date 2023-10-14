from oldresistor import OldResistor
from resistor import Resistor

print("_____________ Klasa OldResistor ______________")
r0 = OldResistor(10.2E3)
print(r0)
print(r0.get_ohms())
r0.set_ohms(2.88E2)
print(r0.get_ohms())

print("_____________ Klasa Resistor ______________")
r1 = Resistor(50E3)
r1.ohms = 11.1E3
print(f'układ elektryczny:\noporność: {r1.ohms} omów\nnapięcie prądu: {r1.voltage} V\n'
      f'natężenie prądu: {r1.current} A')
