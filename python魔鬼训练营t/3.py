# def getInput():
# #     try:
# #         one=input("请输入整数:")
# #         while eval(one)!=int(one):
# #             one=input("请输入整数:")
# #         if eval(one) ==int(one):
# #             print(one)
# #     except:
# #         return getInput()
# # print(getInput())

from eve import Eve

app = Eve()

if __name__ == '__main__':
    app.run()
