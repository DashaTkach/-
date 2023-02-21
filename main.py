from pprint import pprint

with open('recipe.txt', 'rt', encoding='UTF-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredients_count = int(f.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ing = f.readline().strip()
            ingredient_name, quantity, measure = ing.split('|')
            ingredients.append(
                {'ingredient_name': ingredient_name,
                 'quantity': quantity,
                 'measure': measure}
            )
        cook_book[dish_name] = ingredients
        f.readline()
    pprint(cook_book)


    def get_shop_list_by_dishes(dishes, person_count):
        concept_of_dishes = {}
        for dish in dishes:
            if dish in list(cook_book.keys()):
                for ings in cook_book.values():
                    if cook_book[dish] == ings:
                        for ingredient in ings:
                            if ingredient['ingredient_name'] not in concept_of_dishes:

                                concept_of_dishes[ingredient['ingredient_name']] = {
                                    'measure': ingredient['measure'],
                                    'quantity': int(ingredient['quantity']) * person_count
                                }
                            else:
                                mq = concept_of_dishes.get(ingredient['ingredient_name'])
                                mq['quantity'] = int(mq['quantity']) * person_count
        return concept_of_dishes


    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

with open('1.txt', 'rt', encoding='UTF-8') as f1, open('2.txt', 'rt', encoding='UTF-8') as f2, open('3.txt', 'rt',
                                                                                                    encoding='UTF-8') as f3, open(
    '4.txt', 'x', encoding='UTF-8') as f4:
    file1 = f1.readlines()
    file2 = f2.readlines()
    file3 = f3.readlines()
    if len(file1) > len(file2) > len(file3):
        f4.write(
            f'{f3.name} /n{len(file3)} /n{file3} /n{f2.name} /n{len(file2)} /n{file2} /n{f1.name} /n{len(file1)} /n{file1}')
    elif len(file1) > len(file3) > len(file2):
        f4.write(
            f'{f2.name} /n{len(file2)} /n{file2} /n{f3.name} /n{len(file3)} /n{file3} /n{f1.name} /n{len(file1)} /n{file1}')
    elif len(file2) > len(file1) > len(file3):
        f4.write(
            f'{f3.name} /n{len(file3)} /n{file3} /n{f1.name} /n{len(file1)} /n{file1} /n{f2.name} /n{len(file2)} /n{file2}')
    elif len(file2) > len(file3) > len(file1):
        f4.write(
            f'{f1.name} /n{len(file1)} /n{file1} /n{f3.name} /n{len(file3)} /n{file3} /n{f2.name} /n{len(file2)} /n{file2}')
    elif len(file3) > len(file1) > len(file2):
        f4.write(
            f'{f2.name} /n{len(file2)} /n{file2} /n{f1.name} /n{len(file1)} /n{file1} /n{f3.name} /n{len(file3)} /n{file3}')
    else:
        f4.write(
            f'{f1.name} /n{len(file1)} /n{file1} /n{f2.name} /n{len(file2)} /n{file2} /n{f3.name} /n{len(file3)} /n{file3}')

# доработать вывод текста по столбцам и логику короче