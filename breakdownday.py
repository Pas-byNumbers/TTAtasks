day_hrs = 24
day_mins = 60 * day_hrs
day_secs = 60 * day_mins

num_of_days = int(input("Number of days you wish to calculate? "))

print(f"""
{num_of_days} day(s) is equal 
to {num_of_days * day_hrs} hours
or {num_of_days * day_mins} minutes
or {num_of_days * day_secs} seconds
""")
