number = int(input("Please insert the number: "))
mylist = list(range(1, number + 1))
def ownfil(num_list):
    evenlist = []
    oddlist = []
    for i in num_list:
        if (i % 3 == 0):
            if (i % 2 == 0):
                evenlist.append(i)
            else:
                oddlist.append(i)
    return evenlist, oddlist
output = ownfil(mylist)
print("List of numbers:", mylist)
print("List of Even numbers, which are multiples of 5 are:", output[0])
print("List of Odd numbers, which are multiples of 5 are:", output[1])
