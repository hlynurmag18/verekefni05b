n = int(input("Enter the length of the sequence: ")) # Do not change this line

number_1 = 1
number_2 = 2
number_3 = 3

print(number_1) 
print(number_2)
print(number_3)
for x in range(3, n):
    number_4 = number_1 + number_2 + number_3
    print(number_4)
    number_1 = number_2
    number_2 = number_3
    number_3 = number_4