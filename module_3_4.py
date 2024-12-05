# Создаем программу проверки однокоренных слов
def single_root_words(root_word, *other_words):
    # Сразу переводим root_word в нижний регистр, создаем список вывода и список значений other_words
    root_word = root_word.lower()
    same_words = []
    other_words_list = [*other_words]
    # Первый цикл проверяющий значения из other word в root_word
    for i in other_words_list:
        if root_word in i.lower():
            same_words.append(i)
        # Если данная проверка не дала результатов создаем вложенный цикл для обратной проверки по тому же слову i
        else:
            for j in range((len(root_word)-len(i))):
                # Вытаскиваем из root_word корень равный длине i и проверяем, равно ли i, если нед двигаемся по букве
                if root_word[j: j + len(i)] == i.lower():
                    same_words.append(i)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)