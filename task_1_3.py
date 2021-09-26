for s in range(100):
    new_str=str(s + 1)
    my_list = list(new_str)
    if int(my_list[-1]) == 1 and s + 1 !=11:
        print('{} процент'.format(s + 1))
    elif int(my_list[-1])> 1 and int(my_list[-1])<= 4:
        if  s + 1 > 10 and s + 1 <= 14:
            print('{} процентов'.format(s + 1))
        else:
            print('{} процента'.format(s + 1))
    else:
        print('{} процентов'.format(s + 1))