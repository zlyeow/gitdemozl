import os\

file1 = open('git.txt', 'r')
every_lines = file1.readlines()

count = 0
# Strips the newline character
for each_line in every_lines:
    os.system(f"{each_line.strip()}")
    print("Done")