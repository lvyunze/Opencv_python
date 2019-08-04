sent = "hua, I love you"

for one in sent.split():
    allChar = []
    for y in range(12, -12, -1):
        # 存取一次这两个就置为原始的样子，就相当于一个中转站
        char_one = []
        char_con = ''
        for x in range(-30, 30):
            formula = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
            if formula <= 0:
                char_con += one[x % len(one)]
            else:
                char_con += ''
        char_one.append(char_con)
        allChar += char_one
    print('\n'.join(allChar))
