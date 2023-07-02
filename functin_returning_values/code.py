# As default function return "none"
# Assign a return value
def add(x, y):
    return x + y


add(4, 7)
print(add(4, 7))


# When functions find a return they finish executing. Different returns can be added through conditionals
# Usually is not recommended to conditionally return two different types of data

def division(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return 0


print(division(5, 5))
