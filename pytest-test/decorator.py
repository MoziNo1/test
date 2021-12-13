def print_msg():
    msg = "沃斯泥叠"
    name = "卢本伟"
    age = 18

    def printer():
        next_year_age = age + 1
        print(msg, next_year_age, name)

    return printer


closure = print_msg()
closure()
