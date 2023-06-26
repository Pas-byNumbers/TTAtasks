num_of_invitees = int(input("How many people will you invite? "))

if num_of_invitees < 10:
  invited_names = []
  print("What are their names? ")
  for name_index in range(num_of_invitees):
    invited_names.append(input(f"Person #{name_index + 1} is "))
    print(invited_names[name_index] + " has been invited")
  print(f"""
  Full List of Invitees:
  {invited_names}
  """)
else:
  print("Too many people")
