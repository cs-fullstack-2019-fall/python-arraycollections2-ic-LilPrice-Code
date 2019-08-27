def main():
    # pro1()
    pro2()
    # pro4()
    # chal()



# Problem 1:
#
# Create code and define the variable below outside of any function. After you create the list variable write a function called process_number_list that takes an array as a parameter, and performs the functions listed below in the instructions.
#
# person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
# a) Print the 2nd element of the person_array
#
# b) Print the first and last elements of the person_array
#
# c) Take out the 2nd element (Kevin) from the list
#
def pro1():
    person_array = ["Kenn", "Kevin", "Erin", "Autumn"]

    def funtime(N):
        print(N[1])
        print(f"{N[0]} {N[-1]}")
        N.remove("Kevin")
        print(N)

    funtime(person_array)


# Problem 2:
#
# Ask the User for a starting and ending number
# Write a function that takes the 2 numbers as parameters and builds a list/array of numbers with the values from start to end parameters and return the array to the caller
# Print the sum of the numbers in the list using an 'f' string (ex. The sum of the numbers from 5 to 100 is5050```)
def pro2():
    def nums():
        user = int(input("Enter a number.\n"))
        return user

    def bigmath(n1, n2):
        array= []
        if n1 > n2:
            x = range(n2,n1+1)
            for n in x:
                array.append(n)
        elif n2 > n1:
            x = range(n1,n2+1)
            for n in x:
                array.append(n)
        elif n1 == n2:
            array.append(n1)
            array.append(n2)
        return array

    ray = bigmath(nums(),nums())
    num = 0
    for x in ray:
        num +=x
    print(f"The sum of the numbers from {ray[0]} to {ray[int(len(ray))-1]} is {num}!")


# Problem 4:
#
# Use the following list of 5 numbers. score_list = [21,14,6,8,28,42,21]
#
# Write the code to find the element where the score is equal to 6

def pro4():
    score_list = [21,14,6,8,28,42,21]
    for x in score_list:
        if x == 6:
            print("Found it!!")

#
# Challenge:
#
# Using the same list from Problem 4, write a program that removes the smallest and the largest value from the list and adds them to a newly created list. Your code should work regardless of the numbers in the list.

def chal():
    list = [21,14,6,8,28,42,31]
    list2 = []
    print(list)
    list2.append(max(list))
    list2.append(min(list))
    list.remove(max(list))
    list.remove(min(list))
    print(list)
    print(list2)



main()
