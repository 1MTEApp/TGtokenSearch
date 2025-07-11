import telebot
import time

print("ВНИМАНИЕ: Перед запуском обязательно включите VPN!")

time.sleep(10)

def main():
    token = input("Введите токен бота: ")
    bot = telebot.TeleBot(token)
    
    try:
        info = bot.get_me()
        print("\nБОТ ОБНАРУЖЕН")
        print(f"ID: {info.id}")
        print(f"Юзернейм: @{info.username}")
        print(f"Имя: {info.first_name}")
        
        while True:
            print("\nМЕНЮ")
            print("1: Отправить сообщение от имени бота")
            print("2: Изменить имя бота")
            print("3: Изменить описание профиля")
            print("4: Изменить краткое описание")
            print("5: Проверить другой токен")
            print("6: Выйти")
            
            choice = input("Выберите действие: ")
            
            if choice == "1":
                try:
                    chat_id = input("Введите ID чата/пользователя: ")
                    message = input("Текст сообщения: ")
                    bot.send_message(chat_id, message)
                    print("Сообщение отправлено!")
                except:
                    print("Ошибка отправки")
                    
            elif choice == "2":
                try:
                    new_name = input("Новое имя бота: ")
                    bot.set_my_name(new_name)
                    print(f"Имя изменено на: {new_name}")
                except:
                    print("Ошибка изменения имени")
                    
            elif choice == "3":
                try:
                    new_desc = input("Новое описание профиля: ")
                    bot.set_my_description(new_desc)
                    print(f"Описание изменено на: {new_desc}")
                except:
                    print("Ошибка изменения описания")
                    
            elif choice == "4":
                try:
                    new_short_desc = input("Новое краткое описание: ")
                    bot.set_my_short_description(new_short_desc)
                    print(f"Краткое описание изменено на: {new_short_desc}")
                except:
                    print("Ошибка изменения краткого описания")
                    
            elif choice == "5":
                return main()
                
            elif choice == "6":
                print("Выход из программы...")
                exit()
                
            else:
                print("Некорректный выбор")
    
    except:
        print("\nОшибка: Некорректный токен")
        retry = input("Попробовать другой токен? (y/n): ")
        if retry.lower() == 'y':
            main()
        else:
            print("Выход...")
            exit()

if __name__ == "__main__":
    print("TGtokenSearch")
    main()
