import datetime

class SampleClass:

    def __init__(self):
        self.val = None
        # print('This is the INIT of sample class')

    def method1(self, userinput):
        self.val = userinput
        return self.val


# s1 = SampleClass()
# x = s1.method1(13)
#
# print(x)
# print(s1.val)
# ===========================
# x = SampleClass().method1(14)
# print(x)
#
# print(SampleClass().val)
# ==================================


if __name__ == '__main__':

    s1 = SampleClass()
    x = s1.method1(13)

    print(x)
    print(s1.val)