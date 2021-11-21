# De esta forma podemos eliminar los duplicacos de una lista, pero podemos hacerlocon sets
# De una forma aún más fácil
def run():

    # De esta forma convertimos automáticamente la lista en un set, es decir, sin duplicados
    my_list = [13, 23, 11, 23, 13, 54, 43, 54, 13, 23, 11, 65, 34, 23]
    my_list_without_duplicates = set(my_list)


    # for element in my_list:
    #     if element not in my_list_without_duplicates:
    #         my_list_without_duplicates.append(element)
    print(list(my_list_without_duplicates))

if __name__ == '__main__':
    run()