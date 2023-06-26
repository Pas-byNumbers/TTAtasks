import random

secret_number=random.randint(1,20)
num_of_guesses=5

while num_of_guesses != 0:
  user_guess=int(input(f"""
  You have {num_of_guesses} guess(es) left
  What number am I thinking of between 1 and 20: 
  """))
  num_of_guesses-=1
  if user_guess == secret_number:
    print(f"Well done! {secret_number} is the right number!")
    break
  elif user_guess > secret_number:
    print("You guessed too high, the number is lower")
  else:
    print("You guessed too low, the number is higher")
else:
  print(f"""
  You ran out of guesses, 
  The correct number is {secret_number}
  """)
