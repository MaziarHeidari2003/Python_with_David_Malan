students = [
  {"name":"Harry","house": "Gryffindor", "patronus": "Stag"},
  {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
  {"name":"Ron", "house": "Gryffindor","patronus": "Jack Russell terior"},
  {"name": "Draco", "house": "Slytherin", "patronus": "None"}
]

for student in students:
  print(student["name"],student["house"],student["patronus"], sep =", ")