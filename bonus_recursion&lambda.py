def FizzBuzz():
    for i in range(1,101):
       if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
       elif i % 3==0:
          print("Fizz")
       elif i % 5==0:
           print("Buzz")
       
       else:
         print(i)


def FizzBuzz_w():
    i=1
    while i<=100:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)   
        i += 1

print(" - using For ")
FizzBuzz()

print(" - using While  ")
FizzBuzz_w()    