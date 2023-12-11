# read lines
with open('day1input.txt', 'r') as file:
    lines = file.readlines()

total = 0

for line in lines:
    digits = ''.join(filter(str.isdigit, line))
    if digits:
        current_digits = int(digits[0] + digits[-1])
        total += current_digits

print("The sum of all calibration values is:", total)

"""
for each line
    get digits
    if digits
        concatenate together first and last
        add to sum
"""