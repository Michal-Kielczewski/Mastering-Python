
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for letter in word:
    print(letter)

# Write a while loop that does the same thing!
idx = 0
while idx < len(word):
    print(word[idx])
    idx += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
num = 100
while num < 142:
    print(num)
    num += 2

# Write a for loop that does the same thing (with range())
for num in range(100, 142, 2):
    print(num)
print(num)
#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
passphrase = input('Please enter the passphrase: "sillygoose" ')
while passphrase != "sillygoose":
    passphrase = input('Please enter the passphrase: "sillygoose" ')