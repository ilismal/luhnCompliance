# Luhn algorithm check
# From https://en.wikipedia.org/wiki/Luhn_algorithm
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

# There's no do-while in python, lazy workaround
while True:
    # Get the first value
    # Check that's a number with 16 digits
    try:
        firstValue=int(raw_input('First PAN in range: '))
        if (len(str(firstValue)) != 16):
            print "PAN must be 16 chars long"
        else:
            break
    except ValueError:
        print("Not a number")
# Same process for the second number
# TODO: This should be a function
while True:
    try:
        lastValue = int(raw_input(('Last PAN in range: ')))
        if (len(str(lastValue)) != 16):
            print "PAN must be 16 chars long"
        else:
            break
    except ValueError:
        print("Not a number")

# Swap variables if the first value is higher than the last
if (firstValue > lastValue):
    firstValue,lastValue = lastValue,firstValue

print "Valid card numbers in range {0}/{1}".format(firstValue,lastValue)
totalValid = 0
# Check if the values in the range are luhn compliant
for ccc in range(firstValue,lastValue):
    if is_luhn_valid(ccc):
        print "\t" + str(ccc)
        totalValid += 1
print "Total: {0} valid cards in range".format(totalValid)
