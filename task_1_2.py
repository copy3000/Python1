s = []
for nam in range(1, 1000, 2):
    s.append(nam ** 3)
#num = int(input (s))
final_amount = 0
for num in s:
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_amount += num
print(final_amount)
final_amount = 0
for num in s:
    num += 17
    check_sum = 0
    for check_num in str(num):
        check_sum += int(check_num)
    if check_sum % 7 == 0:
        final_amount += num
print(final_amount)