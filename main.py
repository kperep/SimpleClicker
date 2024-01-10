import tkinter as tk    # подключаем модуль для создания оконных приложений


# основная программа
def clicker():

    # функция прибавления кликов
    def click(event):
        click_count.configure(state="normal")   # разрешаем изменять поле с количеством кликов
        x = int(click_count.get())              # получаем текущее количество кликов
        x += int(power_label_amount['text'])    # увеличиваем его на значение мощности
        click_count.delete(0, tk.END)       # очищаем поле с количеством кликов
        click_count.insert(0, str(x))      # вставляем туда новое значение
        click_count.configure(state="readonly") # запрещаем редактирование поля с количеством кликов

    # функция покупки увеличения мощности
    def buy_item_1(event):
        amount = int(click_count.get())                     # получаем количество кликов
        cost = int(shop_item_1_cost['text'].split()[0])     # получаем стоимость товара
        if amount >= cost:          # если денег хватает
            click_count.configure(state="normal")           # разрешаем изменять поле с количеством кликов
            power = int(power_label_amount['text'])         # считываем текущее значение мощности
            power *= 5                                      # увеличиваем текущее значение мощности
            power_label_amount.configure(text=str(power))   # меняем старое значение мощности на новое
            amount -= cost          # забираем у пользователя стоимость товара
            click_count.delete(0, tk.END)               # очищаем количество кликов
            click_count.insert(0, str(amount))         # вставляем новое значение кликов
            cost *= 10                                      # увеличиваем стоимость следующего апгрейда в 10 раз
            shop_item_1_cost.configure(text=str(cost) + " кликов")  # меняем цену на новую
            click_count.configure(state="readonly")         # запрещаем редактирование поля с количеством кликов

    # функция покупки фона
    def buy_item_2(event):
        amount = int(click_count.get())                     # получаем количество кликов
        if amount >= 1000000:                               # если денег хватает
            click_count.configure(state="normal")           # разрешаем редактировать поле с количеством кликов
            window.config(bg="gold")                        # меняем фон
            amount -= 1000000                               # отнимаем у пользователя стоимость апгрейда
            # отключаем возможность повторной покупки
            shop_item_2_buy.destroy()
            shop_item_2_cost.destroy()
            shop_item_2_label.destroy()
            click_count.delete(0, tk.END)               # очищаем количество кликов
            click_count.insert(0, str(amount))         # добавляем новое значение кликов
            click_count.configure(state="readonly")         # запрещаем редактирование поля с количеством кликов

    window = tk.Tk()                    # создаём главную форму
    window.title("UberClicker")         # заголовок окна
    window.geometry('400x300')          # размер окна
    window.resizable(False, False)   # запрет на растягивание
    ### форматирование формы игры ###
    main_label = tk.Label(window, text="Кликай пока кликается!")
    main_label.grid(row=0, column=0, columnspan=3)
    clicks_label = tk.Label(window, text="Количество кликов:")
    clicks_label.grid(row=1, column=0)
    click_count = tk.Entry(window, width=10)
    click_count.grid(row=1, column=1)
    click_count.insert(0, "0")
    click_count.configure(state="readonly")
    click_button = tk.Button(window, text="Кликнуть!")
    click_button.grid(row=1, column=2)
    ### форматирование формы магазина ###
    shop_label = tk.Label(window, text="Магазин")
    shop_label.grid(row=2, column=0, columnspan=3)
    # Первый продукт
    shop_item_1_label = tk.Label(window, text="Мощность клика x5")
    shop_item_1_label.grid(row=3, column=0)
    item_1_cost = 10
    shop_item_1_cost = tk.Label(window, text=str(item_1_cost) + " кликов")
    shop_item_1_cost.grid(row=3, column=1)
    shop_item_1_buy = tk.Button(window, text="Купить!")
    shop_item_1_buy.grid(row=3, column=2)
    # Второй продукт
    shop_item_2_label = tk.Label(window, text="Сменить фон")
    shop_item_2_label.grid(row=4, column=0)
    item_2_cost = 1000000
    shop_item_2_cost = tk.Label(window, text=str(item_2_cost) + " кликов")
    shop_item_2_cost.grid(row=4, column=1)
    shop_item_2_buy = tk.Button(window, text="Купить!")
    shop_item_2_buy.grid(row=4, column=2)
    # функционал кнопок
    click_button.bind("<Button-1>", click)              # фарм кликов
    shop_item_1_buy.bind("<Button-1>", buy_item_1)      # прокачка кликов
    shop_item_2_buy.bind("<Button-1>", buy_item_2)      # покупка фона
    # показатель мощности
    power_label = tk.Label(window, text="Мощность")
    power_label.grid(row=0, column=3)
    power_label_amount = tk.Label(window, text="1")
    power_label_amount.grid(row=1, column=3)

    window.mainloop()


if __name__ == '__main__':
    clicker()
