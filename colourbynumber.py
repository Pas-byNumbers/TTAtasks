list_colours = [
  "red", 
  "blue", 
  "yellow", 
  "green", 
  "orange", 
  "purple",
  "black",
  "white",
  "pink",
  "grey"
] 

num_range_low = 10
num_range_high = 10

while num_range_low > 4:
  num_range_low = int(input("Pick a number between 0 and 4: "))
while num_range_high < 5 or num_range_high > 9:
  num_range_high = int(input("Pick a number between 5 and 9: "))

print(list_colours[num_range_low:num_range_high+1])
