"""
FizzBuzz using for , while and and generalised versions with and without list comprehensions
"""
locale_fizz = "Fizz"
locale_buzz = "Buzz"

def makeFizzBuzz(i):
        current_result = ""
        if i % 3 == 0 and i % 5 == 0:
            current_result = locale_fizz+locale_buzz
        elif i % 3 == 0 :
            current_result = locale_fizz
        elif i % 5 == 0 :
            current_result = locale_buzz
        else:
            current_result = str(i)

        return current_result

def forFizzBuzz(up_to):
    result = ""
    for i in range(up_to):
        result += "For {} say {}. \n".format(str(i),makeFizzBuzz(i))
    print(result)

def whileFizzBuzz(up_to):
    result = ""
    i = 0
    while i < up_to:
      result += "For {} say {}. \n".format(str(i),makeFizzBuzz(i))
      i+=1

    print(result)

def fizzBuzz(fizz_on, buzz_on, i):
    if i % fizz_on == 0 and i % buzz_on == 0:
        current_result = locale_fizz+locale_buzz
    elif i % fizz_on == 0 :
        current_result = locale_fizz
    elif i % buzz_on == 0 :
        current_result = locale_buzz
    else:
        current_result = str(i)
    return (i,current_result)

def genericFizzBuzz(fizz_on, buzz_on, up_to):
    result = []
    for i in range(up_to):
        result += [fizzBuzz(fizz_on,buzz_on,i)]
    return result

def genericFizzBuzz_ListComprehension(fizz_on, buzz_on, up_to):
    return [(i,fizzBuzz(fizz_on,buzz_on,i)) for i in range(up_to)]

if __name__ == "__main__":
    print("Testing my Fizzbuzzes\n")

    print("For FizzBuzz")
    forFizzBuzz(30)

    print("\n While FizzBuzz")
    whileFizzBuzz(30)

    print("\n Generic FizzBuzz")
    result = genericFizzBuzz(2,6,30)
    for fb in result:
        print(f'For {fb[0]} say {fb[1]}')

    print("\n Generic FizzBuzz, using list comprehension. ")
    result = genericFizzBuzz_ListComprehension(3,5,30)
    for fb in result:
        print(f'For {fb[0]} say {fb[1]}')



