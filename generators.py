import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    limit = int(input("""Set a limit for the Fibonacci Succecsion: """))

    while counter < limit:
        if counter == 0:
            counter +=1
            yield n1
        elif counter == 1:
            counter +=1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter +=1
            yield aux
    raise StopIteration


if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)