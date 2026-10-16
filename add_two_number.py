class AddNumbers:
    def __init__(self, fnum, snum):
        self.fnum = fnum
        self.snum = snum

    def add_number(self):
        return self.fnum + self.snum


add_nums = AddNumbers(4, 5)

result = add_nums.add_number()
print(result)
