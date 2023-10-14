from homework import Homework
from exam_grade import Egzamin
from weak_egzam import EgzaminR

print(" _____________ Homework _______________")
g = Homework()
g.grade = 95
assert g.grade == 95
print(f'ocena za projekt: {g.grade}')

print(" _____________ Egzamin _______________")
e1 = Egzamin()
e1.first_part = 45
e1.second_part = 33
e1.third_part = 23

print(f'egzamin: 1 -> {e1.first_part}, 2 -> {e1.second_part}, 3 ->  {e1.third_part}')

e2 = Egzamin()
e2.first_part = 70
e2.second_part = 11
e2.third_part = 67

print(f'egzamin poprawkowy: 1 -> {e2.first_part}, 2 -> {e2.second_part}, 3 ->  {e2.third_part}')
print("dane gzaminu z archiwum: e1")

print(f'egzamin: 1 -> {e1.first_part}, 2 -> {e1.second_part}, 3 ->  {e1.third_part}')

print(" _____________ EgzaminR _______________")
e1 = EgzaminR()
e1.first_part = 34
e1.second_part = 21
e1.third_part = 7

print(f'egzamin: 1 -> {e1.first_part}, 2 -> {e1.second_part}, 3 ->  {e1.third_part}')

e2 = EgzaminR()
e2.first_part = 78
e2.second_part = 55
e2.third_part = 90

print(f'egzamin poprawkowy: 1 -> {e2.first_part}, 2 -> {e2.second_part}, 3 ->  {e2.third_part}')
print("dane gzaminu z archiwum: e1")

print(f'egzamin: 1 -> {e1.first_part}, 2 -> {e1.second_part}, 3 ->  {e1.third_part}')
