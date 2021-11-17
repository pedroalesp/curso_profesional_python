def is_primal(num: int) -> bool:
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    if counter > 2:
        return False
    else:
        return True


def run():
    print(is_primal('10'))


if __name__ == '__main__':
    run()