#convert any decimal to some base "k"

# stores the output
output = ""

def converter2(decimal_number, base):
    # finds the maximum power for the base
    power = 0
    global output
    while decimal_number > base ** power:
        power += 1
    power -=1
    # stores the rest
    rest = decimal_number
    while power >= 0:
        # for each power to zero, the loop first finds how many times
        # that the rest is divisible by the power
        integer = int(rest / base ** power)
        # then it calculates the modulo and stores it as the rest
        rest = rest % base ** power
        # adds the the integer to the output
        output += str(integer)
        power -=1
    print(output)
    # resets the output
    output = ""

# number of conversions to make
test_cases = int(input())

for x in range(test_cases):
    # gets the input in a format of "decimal_number base" or ex: "10 2"
    case = input()
    # then it is split at the space
    a = case.split()
    # and used as input for the function
    converter2(int(a[0]), int(a[1]))