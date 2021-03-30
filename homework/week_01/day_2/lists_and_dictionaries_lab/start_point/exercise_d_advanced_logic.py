# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

print([number for number in numbers if number % 2 == 0])

# 2. Print the difference between the largest and smallest value:

print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.

for num in range(len(numbers)):
    if numbers[num] == 2 and num < len(numbers):
        if numbers[num + 1] == 2:
            print(True)
            break

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


count_flag = True
list_sum = 0

for num in numbers:
    if count_flag:
        if num == 6:
            count_flag = False
            continue
        else: 
            list_sum += num
    else:
        if num == 7:
            count_flag = True

print(list_sum)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
# edge cases
# numbers = [13, 1, 11, 82, 13, 44, 7, 6] # should be 106
# numbers = [1, 1, 13, 13, 13, 13, 28] # should be 2

list_sum = 0

for num in range(len(numbers)):
    if num > 0:
        if numbers[num] == 13 or numbers[num-1] == 13:
            continue
    else:
        if numbers[num] == 13:
            continue
    
    list_sum += numbers[num]
    
print(list_sum)



        
        





