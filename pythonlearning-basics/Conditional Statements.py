is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not (is_tall):
    print("The person is short male")
elif not (is_male) and not (is_tall):
    print("The person is short male")
else:
    print("You are neither male nor tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
        # print("Number 1 is greatest of all")
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))
