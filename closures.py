# def make_repeater_of(n: int) -> str:
#     def repeater(word: str):
#         assert type(word) == str, 'You have to type a string
#         return n * word
#     return repeater


# def run():
#     repeat = make_repeater_of(5)
#     print(repeat('Pedro'))
#     repeat10 = make_repeater_of(10)
#     print(repeat10('Logan'))


# if __name__ == '__main__':
#     run()

#############################################################################
#Crea un closure que retorne la división de x entre n

def make_division_by(n: int): 
    def division(x: int):
        assert type(x) == int, 'You have to type an int number'
        return x/n
    return division


def run():
    division_by_3 = make_division_by(3)
    print(int(division_by_3(18)))

    division_by_5 = make_division_by(5)
    print(int(division_by_5(100)))

    division_by_18 = make_division_by(18)
    print(int(division_by_18(54)))


if __name__ == '__main__':
    run()