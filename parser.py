from colorama import Fore, Back, Style
import os
accountlines=[]
with open("messages.txt") as allmessages:
    os.remove("output.txt")
    for line in allmessages:
        if line.startswith("Signed"):
          accountlines.append(line)
for line in accountlines:
    a = line.split("`")
    output = open("output.txt", "a")
    output.write(f"{a[1]}:{a[3]}\n")
    output.close()
count = 0
with open("output.txt", 'r') as alllines:
    for line in alllines:
        count += 1
filepath = os.path.dirname(os.path.abspath("output.txt"))
fullpathtotxt = str(filepath + "\output.txt")
print(f"Successfully printed {count} accounts to {fullpathtotxt}")
a = line.split("`")
x = int(input('What specific account would you like to print? [INPUT A NUMBER]'))
actual = x-1
c = accountlines[actual].split("`")
email = c[1]
password = c[3]
print(f"----------------------------------------------------------\n{email}:{password}\n----------------------------------------------------------")