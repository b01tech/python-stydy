def check_sum(num):
    splited_num = split_num(num)
    add_num = sum(splited_num)
    if add_num == 21:
        print(num)


def check_num(user_num):
    MIN_NUM = 1000
    MAX_NUM = 1500
    for num in range(MIN_NUM, MAX_NUM):
        sp_num = split_num(num)
        is_pass = True
        for x in sp_num:
            if x == user_num:
                is_pass = False
        if is_pass:
            pass_num = num
            check_sum(pass_num)


def split_num(num):
    a, b, c, d = str(num)
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    num_splited = [a, b, c, d]
    return num_splited


check_num(3)
