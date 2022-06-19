
def older_than_two(number1, number2):
    if number1 > number2:
        return number1
    return number2

def older_than_three(number1, number2, number3):
    olderThanTwo1 = older_than_two(number1, number2)
    olderThanTwo2 = older_than_two(olderThanTwo1, number3)
    
    return olderThanTwo2


olderThanThree = older_than_three()
print(olderThanThree)
