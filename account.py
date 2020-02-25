# Adds every account line to the list
accountlines=[]
with open("messages.txt") as allmessages:
    for line in allmessages:
        if line.startswith("Signed"):
          accountlines.append(line)

# Prints every email:password combo and adds it to output.txt
for line in accountlines:
    a = line.split("`")
    output = open("output.txt", "a")
    output.write(f"{a[1]}:{a[3]}\n")
    output.close()
print('----------------------------------------------------------')

# Prints a specific email password combo
b = accountlines[0] # Change [0] to whichever line number (minus 1) that you would like to print, so for line 10, put [9].
c = line.split("`")
email = c[1]
password = c[3]
print(f"{email}:{password}\n----------------------------------------------------------")