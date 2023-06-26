first_name = input("What is your first name? ")

if len(first_name) < 5:
  surname = input("What is your surname? ")
  full_name = first_name + " " + surname
  print(full_name.upper())
else:
  print(first_name.lower())
