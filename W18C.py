def fizzbuzz(num):
    if(num%3==0 and num%5==0):
        print("FIZZBUZZ")
    elif (num%3==0):
        print("FIZZ")
    elif (num%5==0):
        print("BUZZ")

numbers = [2,3,5,6,7,8,10,12,15,17,20,21,22,25,27,30,33,36,32,48,60]

for num in numbers:
    print(num)
    fizzbuzz(num)


