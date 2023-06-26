x = 0
while x<=50:
  user_num=int(input("Type a number to calculate a new total: "))
  x+=user_num
  if(x>50):
    print(f"""
    The total is now {x} and has exceeded 
    the maximum value of 50
    """)
  else:
    print(f"The total is... {x}")
  
