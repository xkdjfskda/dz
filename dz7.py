from itertools import count

class Counter:
    def __init__(self, max_number):
        self.i - 0
        self.max_number - max_number

    def __iter__(self):
        self.i - 0
        return self
        i = 0
        while True:
            yield number ** i
            i += 1

    def __next__(self):
            self.i += 1
            if self.i > self.max_maxnumber:
                raise StopIteration
            return self.i
