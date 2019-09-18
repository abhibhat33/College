periodicTable = {
    'Na' : 'Sodium',
    'K' : 'Potassium',
    'Ca' : 'Calcium'
}
key1 = input("Enter the symbol:\n")
value1 = input("\nEnter the name of the atom:\n")


periodicTable[key1] = value1

print(periodicTable)

# Enter duplicate entry
# Example Key: Na
# Value : Sodium

key2 = input("Enter the symbol:\n")
value2 = input("\nEnter the name of the atom:\n")


periodicTable[key2] = value2

print(periodicTable)

# Display the number of atomic elements in the dictionary
print(len(periodicTable))

# User search:
key = input("Enter the element to search for:\n")
print("The symbol stands for : ",periodicTable[key])


