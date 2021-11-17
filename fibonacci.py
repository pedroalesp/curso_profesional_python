import time

class FibonacciIterator():

    def __init__(self, max=30):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        while self.counter < self.max:
            if self.counter == 0:
                self.counter +=1
                return self.n1, self.counter
            elif self.counter == 1:
                self.counter +=1
                return self.n2, self.counter
            else:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                self.counter +=1
                return self.aux, self.counter
        raise StopIteration


def run():
    fibonacci = FibonacciIterator()
    for num, i in fibonacci:
        print(num, 'vuelta: ', i)
        time.sleep(0.5)

if __name__ == '__main__':
    run()