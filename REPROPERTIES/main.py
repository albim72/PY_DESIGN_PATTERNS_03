from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance
from bounded import BoundedResistance

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

print("_____________ Klasa VoltageResistance ______________")
r2 = VoltageResistance(1E2)
print(f'natężenie początkowe prądu wynosi: {r2.current} A')
r2.voltage = 322
print(f'opór eleketryczny: {r2.ohms} omów')
print(f'natężenie prądu: {r2.current} A')
print(f'napięcie prądu: {r2.voltage} V')


print("_____________ Klasa VoltageResistance ______________")

try:
      r3 = BoundedResistance(1.1E2)
      print(r3.ohms)
      r3.ohms = 33
      print(r3.ohms)
except ValueError as v:
      print(v)
