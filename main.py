gl = "аАеЕёЁиИоОуУыЫэЭюЮяЯ" #Переменная для гласных
sogl = "бБвВгГдДжЖзЗйЙкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩъЪьЬ" #Переменная для гласных
k = str(input("Введите строку: ")) #Вводим строку
rgl = 0 #Переменная для заоплнения гласных
rsogl = 0 #Переменная для заполнения согласных
for i in k: #Цикл повторяющийся кол-ву строки
    if i in gl:
        rgl += 1 #К кол-ву гласных прибавляем 1
    elif i in sogl:
        rsogl += 1 #К кол-ву согласных прибавляем 1   
print(f"Кол-во гласных будет равно: {rgl}") #Выводим кол-во гласные
print(f"Кол-во согласных будет равно: {rsogl}") #Выводим кол-во согласные
print(f"Длина строки будет равна: {len(k)}") #Выводим длину строки
