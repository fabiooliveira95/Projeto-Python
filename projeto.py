import sys
import os

try:
    # Open 'temp.txt' in write mode
    with open('temp.txt', 'w') as temp:
        for i in range(100):
            temp.write(f'{i:03d}\n')
except IOError as e:
    sys.stderr.write(f"Error writing to 'temp.txt': {e}\n")

try:
    # Open 'temp.txt' in read mode and output its content to stdout
    with open('temp.txt', 'r') as temp:
        for x in temp:
            sys.stdout.write(x)
except IOError as e:
    sys.stderr.write(f"Error reading 'temp.txt': {e}\n")

# Prompt for filename
fn = input('Enter filename (default is temp.txt): ').strip() or 'temp.txt'
if not os.path.exists(fn):
    print('File does not exist. Try again...')
    sys.exit()

# Number the lines
try:
    with open(fn, 'r') as file:
        for i, s in enumerate(file):
            print(i + 1, s.strip())
except IOError as e:
    sys.stderr.write(f"Error reading file {fn}: {e}\n")

# Print a list containing lines of the file
try:
    with open(fn, 'r') as file:
        lines = file.readlines()
        print(lines)
except IOError as e:
    sys.stderr.write(f"Error reading file {fn}: {e}\n")