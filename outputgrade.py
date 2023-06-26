grade = int(input("Please input the student's grade from 60 to 100 "))

if 90 <= grade <= 100 :
  print("Grade A*")
elif 80 <= grade < 90 :
  print("Grade A")
elif 70 <= grade < 80 :
  print("Grade B")
elif 60 <= grade < 70 :
  print("Grade C")
else :
  print("Have another go!")
