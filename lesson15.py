# Домашнее задание
# Задача 1
import json                                                 # импортирую json

my_dict_product = {}                                        # создаю пустой словарь для последующего его заполнения
while True:                                                 # запускаю цикл с условием
    my_product = input('Введите название вашего товара. Для завершения покупок введите слово "стоп": ')
    if my_product == 'стоп':                                # если пользователь ввел слово "стоп"
        break                                               # то цикл останавливается
    product_cost = float(input('Введите стоимость выбранного товара: '))
    my_dict_product.setdefault(my_product, product_cost)    # добавляю в словарь название товара и его стоимость,
                                                            # как ключ и значение
with open('products.json', 'w', encoding='UTF-8') as file:  # открываю файл products.json на запись
    json.dump(my_dict_product, file, ensure_ascii=False)    # записываю полученный словарь в json-файл

# Задача 2
import json                                                   # импортирую json
with open('products.json', 'r', encoding='UTF-8') as file2:   # открываю файл products.json на чтение
    products = json.load(file2)                               # считываю json-файл
print(sum(products.values()))                                 # вывожу на экран общую стоимость выбранных товаров
