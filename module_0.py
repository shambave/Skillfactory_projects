#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


def binary_search(number):
    '''Применим бинарный поиск для поиска угадываемого числа.
        Обозначим максимальную границу поиска переменной maximum,
        минимальную границу – minimum. Функция принимает угадываемое 
        число и возвращает число попыток'''

    count = 0

    minimum = 0      # Минимальная граница поиска 
    maximum = 100  # Максимальная  граница поиска
    while (maximum - minimum) > 1:  # Пока максималная граница больше минимальной 
        middle = int((minimum + maximum) / 2) # вычисляем центр между макисмальной и минимальной границами 
        if (middle >= number): # Если число находится в центре или ближе к максимальной границе
            maximum = middle  # Передвигаем максимальную границу к центру 
        else:
            minimum = middle  # Иначе передвигаем минимальную границу к центру 

        count += 1

    return(count)  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать,
        как быстро игра угадывает число'''

    count_ls = []

    # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    np.random.seed(1)

    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# In[ ]:


score_game(binary_search)

