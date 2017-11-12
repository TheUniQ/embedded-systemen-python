def get_temp(s):
    print(s)
    s = str(s.hex())
    print(s)
    r = [s[i:i + 2] for i in range(0, len(s), 2)]
    r = r[::-1]
    print(r)
    binary = ''
    for i in r:
        x = i
        trip = bin(int(x, 16))[2:].zfill(8)
        binary += str(trip)
    man_list = []
    negative = ''
    if binary[0] == '1':
        negative += '-'
    man_list.append(binary[0])
    man_list.append(binary[1:9])
    man_list.append(binary[9:])
    x =int(man_list[1], 2) - 127
    man_last = [1]
    j = 1
    check = True
    for i in man_list[2]:
        man_last.append(i)
        if j == x:
            man_last.append('.')
            check = False
        j += 1
    if check == True:
        man_last[0] = '1.'

    man_string = ''
    for i in man_last:
        man_string += str(i)

    before_comma, after_comma = man_string.split('.')
    j = 1
    temp = 0
    for i in after_comma:
        if i == '1':
            temp += (1 / (2 ** j))
        j += 1

    return str(int(before_comma, 2) + temp)
