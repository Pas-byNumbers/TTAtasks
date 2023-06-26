import random
username = ""
new_password = ""
pass_req_eachcount = 0
pass_req_count_remainder = 0

symbol_array= [
  '!','@', '#', '%', '?', '&', '£', '$', '*'
  ]
number_array = [
  '1', '2', '3', '4', '5', '6', '7', '8', '9'
]
alphabet_array = [
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

character_categories = [symbol_array, number_array, alphabet_array]

def new_pass_gen():
  global new_password
  password_characters = []
  
  for type in character_categories:
    for i in range(pass_req_eachcount):
      if type == alphabet_array:
        password_characters.append(random.choice(type).upper())
        password_characters.append(random.choice(type))
      else:
        password_characters.append(random.choice(type))
  for i in range(pass_req_count_remainder):
    random_character_array = random.choice(character_categories)
    password_characters.append(random.choice(random_character_array))
    
  random.shuffle(password_characters)
  new_password = "".join(password_characters)

def user_password_length():
  global pass_req_eachcount
  global pass_req_count_remainder
  chosen_pass_length = 0
  print("\nBefore a new password can be generated...")
  while chosen_pass_length < 12 or chosen_pass_length > 24:
    chosen_pass_length = int(input(
    '''
    How many characters would 
    you like in your password?
    Choose between 12 and 24
    '''
    ))
  pass_req_eachcount = int(chosen_pass_length / 4)
  pass_req_count_remainder = chosen_pass_length % 4

def ask_username():
  global username
  username = input("Type in a new Username: ")

def confirm_credentials():
  global username
  global new_password
  confirm_choice = ""
  print(f"\nYour new username is {username}")
  print(f"Your new password is {new_password}")
  while confirm_choice != "N" and confirm_choice != "Y":
    confirm_choice = input("\nAre you happy with this? Y or N: ").upper()
  if confirm_choice == 'Y':
    print("Thank you for using my random password generator")
  else:
    run()

def run():
  ask_username()
  user_password_length()
  new_pass_gen()
  confirm_credentials()
  
run()
  
