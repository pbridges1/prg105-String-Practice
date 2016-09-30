# Print the first letter of the following string

school = "McHenry County College"
mcc = school[0]
print mcc


# print the length of the school string
mcc = len(school)
print mcc


# Use a while loop to print each character (including spaces) in the school variable
index = 0
while index < len(school):
    mcc = school[index]
    print mcc
    index = (index + 1)

# Slice school into three variables, print the variables
print school[0:7]
print school[8:14]
print school[15:22]


# use a while statement to search for the letter "e" in the contents of the school variable


def find(words, letters):
    school1 = "Mchenry County College"
    indexes = 0
    while indexes < len(school1):
        if words[indexes] == letters:
            print ("The letter " + str(letters) + " is found in column " + str(indexes))
        indexes = (indexes + 1)

find(school, "e")
# print the index of every location with the letter "e"
# remember, you should not use the same variable twice in the same program
# so if you used the variable index, use something else


# Write the code to count the number of times the letter y appears in the school variable
# print the total
count = 0
for index in range(1, len(school), 1):
    if school[index] == "y":
        count = (count + 1)
print count

# create a variable named college and store the upper case version of the variable school in it
college = school.upper()
print college

# check to see if Count is in the school variable


def in_both(word):
        if "Count" in word:
            return "True"
        else:
            return "False"


print in_both(school)
# check to see if count is in the school variable


def in_both(word):
        if "count" in word:
            return "True"
        else:
            return "False"


print in_both(school)
