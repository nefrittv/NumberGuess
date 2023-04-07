import pickle

def save_progress(player_name, player_level, total_experience, player_rewards, player_coins):
    try:
        with open(f"{player_name}_progress.pickle", "wb") as file:
            progress_data = (player_name, player_level, total_experience, player_rewards, player_coins)
            pickle.dump(progress_data, file)
            print(f"Прогресс игрока {player_name} успешно сохранён.")
    except Exception as e:
        print(f"Произошла ошибка при сохранении прогресса: {e}")

def safe_filename(player_name):
    safe_name = "".join(c if c.isalnum() else "_" for c in player_name)
    return safe_name + "_progress.pickle"

def load_progress():
    try:
        with open("progress.pickle", "rb") as f:
            progress = pickle.load(f)
            print("Прогресс загружен!")
            return progress["player_name"], progress["player_level"], progress["total_experience"], progress["player_rewards"], progress["player_coins"]
    except FileNotFoundError:
        print("Файл с прогрессом не найден.")
        return None

import random

def welcome_menu():
    print("\nДобро пожаловать!")
    print("1. Начать новую игру")
    print("2. Загрузить сохраненного персонажа")
    print("3. Выход")
    while True:
        try:
            choice = int(input("Введите ваш выбор: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Пожалуйста, выберите корректный вариант (1, 2 или 3).")
        except ValueError:
            print("Пожалуйста, введите число.")

def get_player_name():
    player_name = input("Введите ваше имя: ")
    return player_name

def introduction():
    print("Добро пожаловать в игру 'Угадай число: Путь Героя'!")
    print("Вы - отважный искатель приключений, решившийся пройти испытание бога чисел.")
    print("Чтобы доказать свою мудрость, вам предстоит угадывать числа, которые он загадывает.")
    print("За каждое угаданное число вы будете получать опыт и повышать свой уровень.")
    print("С каждым уровнем вы получаете награды, которые помогут вам на этом пути.")
    print("Удачи, путник! И помни, бог чисел наблюдает за тобой...\n")

def menu(player_level, player_coins):
    while True:
        print("\nГлавное меню:")
        print("1. Начать игру")
        print("2. Магазин")
        print("3. Сохранить прогресс")
        print("4. Загрузить прогресс")
        print("5. Выход")

        try:
            choice = int(input("Введите номер опции: "))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("Пожалуйста, выберите корректный номер опции (1, 2, 3, 4 или 5).")
        except ValueError:
            print("Пожалуйста, введите число.")

def display_player_statistics(player_name, player_level, total_experience, player_coins):
    experience_to_next_level = (player_level + 1) * 100 - total_experience
    print("\nСтатистика игрока:")
    print(f"Имя: {player_name}")
    print(f"Уровень: {player_level}")
    print(f"Опыт: {total_experience} (еще {experience_to_next_level} до следующего уровня)")
    print(f"Монеты: {player_coins}")


def get_difficulty_level():
    while True:
        try:
            difficulty = int(input("Выберите уровень сложности (1 - легкий, 2 - средний, 3 - сложный): "))
            if difficulty in [1, 2, 3]:
                return difficulty
            else:
                print("Пожалуйста, выберите корректный уровень сложности (1, 2 или 3).")
        except ValueError:
            print("Пожалуйста, введите число.")


def calculate_experience(difficulty_level, remaining_attempts):
    base_experience = 50 * difficulty_level
    experience = base_experience + remaining_attempts * 2
    return experience

def reward_player(player_level, player_rewards):
    if player_level in player_rewards:
        return

    if player_level == 2:
        player_rewards[player_level] = 'extra_attempt'
        print("Поздравляем! На 2 уровне вы получаете дополнительную попытку!")
    elif player_level == 3:
        player_rewards[player_level] = 'hint'
        print("Поздравляем! На 3 уровне вы получаете возможность использовать подсказку!")
    elif player_level == 4:
        player_rewards[player_level] = 'extra_experience'
        print("Поздравляем! На 4 уровне вы будете получать больше опыта!")
    elif player_level == 5:
        player_rewards[player_level] = 'coins'
        print("Поздравляем! На 5 уровне вы начинаете получать монеты!")
    else:
        player_rewards[player_level] = None

def god_taunt(player_level):
    taunts = [
        "Очень слабо! Мне даже стыдно за тебя...",
        "Ха! Ты думаешь, ты сможешь угадать число?",
        "Плохо тебе идет. Возможно, это не твоя игра?",
        "Неужели ты думаешь, что сможешь победить меня?"
    ]
    print(f"Бог Чисел: {random.choice(taunts)}")


def god_guess(number_to_guess, max_attempts, max_number):
    lower_bound = 1
    upper_bound = max_number
    attempts = 0

    while attempts < max_attempts:
        god_number = random.randint(lower_bound, upper_bound)
        print(f"Бог Чисел думает, что это число {god_number}.")

        if god_number == number_to_guess:
            print("Ха-ха")
            return True

        attempts += 1

        if god_number < number_to_guess:
            lower_bound = god_number + 1
        else:
            upper_bound = god_number - 1

    return False


def reward_player(player_level, player_rewards):
    if player_level in player_rewards:
        return

    if player_level == 2:
        player_rewards[player_level] = 'extra_attempt'
        print("Поздравляем! На 2 уровне вы получаете дополнительную попытку!")
    elif player_level == 3:
        player_rewards[player_level] = 'hint'
        print("Поздравляем! На 3 уровне вы получаете возможность использовать подсказку!")
    elif player_level == 4:
        player_rewards[player_level] = 'extra_experience'
        print("Поздравляем! На 4 уровне вы будете получать больше опыта!")
    elif player_level == 5:
        player_rewards[player_level] = 'coins'
        print("Поздравляем! На 5 уровне вы начинаете получать монеты!")
    else:
        player_rewards[player_level] = None


def purchase_item(player_level, player_rewards, player_coins):
    print("\nМагазин предметов:")
    print("1. Дополнительная попытка - 10 монет")
    print("2. Подсказка - 15 монет")
    print("3. Выход из магазина")

    if player_level < 5:
        print("Заметка: Монеты начинают поступать игроку, достигнув 5 уровня. До этого вы не сможете их использовать.")

    while True:
        try:
            choice = int(input(
                "Введите номер предмета, который вы хотите приобрести, или выберите '3' для выхода из магазина: "))
            if player_level >= 5:
                if choice == 1:
                    if player_coins >= 10:
                        player_coins -= 10
                        player_rewards['extra_attempt'] += 1
                        print("Вы приобрели дополнительную попытку. Осталось монет:", player_coins)
                    else:
                        print("У вас недостаточно монет.")
                elif choice == 2:
                    if player_coins >= 15:
                        player_coins -= 15
                        player_rewards['hint'] += 1
                        print("Вы приобрели подсказку. Осталось монет:", player_coins)
                    else:
                        print("У вас недостаточно монет.")
                elif choice == 3:
                    print("Вы вышли из магазина.")
                    break
                else:
                    print("Выберите действительный вариант.")
            else:
                if choice == 3:
                    print("Вы вышли из магазина.")
                    break
                else:
                    print("Пока вы не достигнете 5 уровня, вы не сможете покупать предметы.")
        except ValueError:
            print("Пожалуйста, введите число.")
    return player_rewards, player_coins

def play_game(player_level, total_experience, player_rewards, player_coins):
    difficulty_level = get_difficulty_level()


    if difficulty_level == 1:
        number_to_guess = random.randint(1, 10)
        max_attempts = 5
        max_number = 10
    elif difficulty_level == 2:
        number_to_guess = random.randint(1, 50)
        max_attempts = 6
        max_number = 50
    else:
        number_to_guess = random.randint(1, 100)
        max_attempts = 7
        max_number = 100

    if 'extra_attempt' in player_rewards.values():
        max_attempts += 1

    attempts = 0
    hint_used = False
    win = False

    print("Я загадал число. У вас есть", max_attempts, "попыток, чтобы угадать его!")

    while attempts < max_attempts:
        try:
            god_won = god_guess(number_to_guess, 1, max_number)
            if god_won:
                print("Бог Чисел угадал число и сделал вам плохо! Ваш уровень понижается!")
                player_level = max(1, player_level - 1)
                break
            user_guess = int(input("Введите ваше число: "))
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue

        attempts += 1
        if user_guess < number_to_guess:
            print("Загаданное число больше вашего числа.")
        elif user_guess > number_to_guess:
            print("Загаданное число меньше вашего числа.")
        else:
            print(f"Поздравляю, вы угадали число {number_to_guess} за {attempts} попыток!")
            win = True
            break

        remaining_attempts = max_attempts - attempts
        print(f"Осталось попыток: {remaining_attempts}")

    if win:
        remaining_attempts = max_attempts - attempts
        experience_gained = calculate_experience(difficulty_level, remaining_attempts)
        total_experience += experience_gained

        if player_level >= 5:
            coins_gained = remaining_attempts * difficulty_level
            player_coins += coins_gained
            print(f"Вы получили {coins_gained} монет. Теперь у вас {player_coins} монет.")

        if total_experience >= (player_level + 1) * 100:
            player_level += 1
            print(f"Поздравляем! Вы достигли {player_level} уровня!")

        print(f"Вы получили {experience_gained} опыта. Теперь у вас {total_experience} опыта.")
    else:
        print(f"К сожалению, вы проиграли. Загаданное число было {number_to_guess}.")

    return win, player_level, total_experience, player_coins


def main():
    introduction()
    welcome_choice = welcome_menu()
    if welcome_choice == 1:
        player_name = get_player_name()
        player_level = 1
        total_experience = 0
        player_rewards = {}
        player_coins = 0
    elif welcome_choice == 2:
        progress = load_progress()
        if progress:
            player_name, player_level, total_experience, player_rewards, player_coins = progress
        else:
            print("Не удалось загрузить сохраненную игру. Создание нового персонажа...")
            player_name = get_player_name()
            player_level = 1
            total_experience = 0
            player_rewards = {}
            player_coins = 0
    else:
        print("Спасибо за игру! До свидания!")
        return

    while True:
        display_player_statistics(player_name, player_level, total_experience, player_coins)
        choice = menu(player_level, player_coins)
        if choice == 1:
            print(f"{player_name}, ваш текущий уровень: {player_level}, текущий опыт: {total_experience}, текущее количество монет: {player_coins}")
            win, player_level, total_experience, player_coins = play_game(player_level, total_experience, player_rewards, player_coins)

            if win:
                print("Поздравляем с победой!")
            else:
                print("Не отчаивайтесь, попробуйте еще раз!")

            reward_player(player_level, player_rewards)
        elif choice == 2:
            player_rewards, player_coins = purchase_item(player_level, player_rewards, player_coins)
        elif choice == 3:
            save_progress(player_name, player_level, total_experience, player_rewards, player_coins)
        elif choice == 4:
            progress = load_progress()
            if progress:
                player_name, player_level, total_experience, player_rewards, player_coins = progress
        else:
            print(f"Спасибо за игру, {player_name}! До свидания!")
            break

if __name__ == "__main__":
    main()