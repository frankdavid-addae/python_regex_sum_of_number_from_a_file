# Import the regex library
import re

filename = 'regex_sum_749543.txt'

# Open the file
fh = open(filename)

# Declares empty lists
# numbers = list()
intNumberList = list()


for line in fh:  # Read each line in the file
    # numbers += re.findall('[0-9]+', line)
    # Read each number in the list of strings returned
    for number in re.findall('[0-9]+', line):
        # Convert each string into an integer value and append them to the intNumberList
        intNumberList.append(int(number))
print(sum(intNumberList))  # Sum all the elements in the intNumberList and print the result
