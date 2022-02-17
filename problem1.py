# Name: Gabriella Laines
#

sec_input = int(input("How many seconds? "))

seconds = sec_input

minutes = sec_input // 60
seconds = sec_input % 60

hours = minutes // 60
minutes = minutes % 60

days = hours // 24
hours = hours % 24

print(f"In {sec_input} seconds, there are {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")