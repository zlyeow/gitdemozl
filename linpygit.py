from email import message
import os\

file1 = open('git.txt', 'r')
every_lines = file1.readlines()

count = 0
# Strips the newline character
for each_line in every_lines:
    os.system(f"{each_line.strip()}")
message = input("Please key your commit message here: ")
os.system(f"git commit -m {message}")
os.system(f"git push")