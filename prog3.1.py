def myreduce(num):
    mylist = list(range(1, number + 1))
    elemsum = 0
    for i in mylist:
        elemsum += i
    return mylist, elemsum
number = int(input("insert the number :"))
output = myreduce(number)
print("first natural numbers are:", output[0])
print("Sum of List are :", output[1])