def add_two_numbers() -> int:
    user_input=input()
    res=[int(x) for x in user_input.split(",")]
    return sum(res)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
