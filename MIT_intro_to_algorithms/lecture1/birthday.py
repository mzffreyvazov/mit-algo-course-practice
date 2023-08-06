import timeit

def birthday_match_list(students):

  n = len(students)
  
  record = [None] * n 
  
  for k in range(n):
    name1, bday1 = students[k]

    for i in range(k):
      name2, bday2 = record[i]
      if bday1 == bday2:
        return (name1, name2)

    record[k] = (name1, bday1)

  return None

def birthday_match_dict(students):

  birthdays = {}

  for student in students:
    name, birthday = student

    if birthday in birthdays:
      match_name = birthdays[birthday]
      return (match_name, name)

    birthdays[birthday] = name

  return None

students = [(f"Student {i}", i) for i in range(1000)]

time_list = timeit.timeit(
  "birthday_match_list(students)", 
  globals=globals(),
  number=100  
)
time_dict = timeit.timeit(
  "birthday_match_dict(students)", 
  globals=globals(),
  number=100  
)

print(f"Birthday match (list) took {time_list:.5f} seconds") 
print(f"Birthday match (dict) took {time_dict:.5f} seconds") 

"""

Output:

Birthday match (list) took 4.57722 seconds
Birthday match (dict) took 0.01517 seconds


"""