import time

sentence = "Dear, I love you forever!"

for char in sentence.split():
    allChar = []
    # 从y轴的上半轴12开始到y轴的下半轴12，步长逐渐减1
    for y in range(12, -12, -1):
        lst = []
        lst_con = ''
        for x in range(-50, 50):
            formula = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
            if formula <= 0:
                # char[x % len(char)]按照索引取字符串
                lst_con += char[x % len(char)]

            else:
                lst_con += " "
        lst.append(lst_con)
        allChar += lst
    print('\n'.join(allChar))
    time.sleep(1)
