import random

choice = 0
user_answer = 0
correct_answer = 0

def addition_choice():
  global user_answer
  global correct_answer
  add_criteria = []
  n = 2
  while n != 0:
    add_criteria.append(random.randint(5,20))
    n-=1
  correct_answer = add_criteria[0] + add_criteria[1]
  user_answer = int(input(
    f"Please add {add_criteria[0]} to {add_criteria[1]}: "
  ))
  print(f"""
  Your answer is {user_answer} and
  the correct answer is {correct_answer}
  """)

def subtraction_choice():
  global user_answer
  global correct_answer
  sub_criteria = []

  sub_criteria.append(random.randint(25, 50))
  sub_criteria.append(random.randint(1, 25))
  correct_answer = sub_criteria[0] - sub_criteria[1]
  user_answer = int(input(
    f"Please subtract {sub_criteria[0]} from {sub_criteria[1]}: "
  ))
  print(f"""
  Your answer is {user_answer} and
  the correct answer is {correct_answer}
  """)

def check_answer():
  if correct_answer == user_answer:
    print("Correct!")
  else:
    print("Incorrect!")

def make_choice():
  global choice
  print("\n1) Addition \n2) Subtraction")
  try:
    choice = int(input("Enter 1 or 2: "))
  except ValueError:
    print("Only input numbers please")

def run():
  global choice
  while choice != 1 and choice != 2:
    make_choice()
    if choice == 1:
      addition_choice()
    elif choice == 2:
      subtraction_choice()
    else:
      print("You haven't picked a valid menu option, try again...")
  check_answer()

run()
