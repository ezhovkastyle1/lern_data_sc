import numpy as np

def binary_predict(number: int = 1) -> int:
    """Угадываем число методом бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        # Берём середину текущего диапазона
        predict_number = (low + high) // 2

        if predict_number == number:
            break  # Угадали!
        elif predict_number < number:
            # Если наше число меньше загаданного, ищем в верхней половине
            low = predict_number + 1
        else:
            # Если наше число больше загаданного, ищем в нижней половине
            high = predict_number - 1

    return count

def score_game(predict_func, seed: int = 42) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_func: функция угадывания
        seed (int): Зерно генератора случайных чисел для воспроизводимости. Defaults to 42.

    Returns:
        int: среднее количество попыток
    """
    np.random.seed(seed)  # Фиксируем seed для воспроизводимости результатов
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел

    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(binary_predict)