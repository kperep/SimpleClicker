import tkinter as tk    # подключаем модуль для создания оконных приложений


# основная программа
def clicker():
    def click(event):
        click_count.configure(state="normal")
        x = int(click_count.get())
        x += int(power_label_amount['text'])
        click_count.delete(0, tk.END)
        click_count.insert(0, x)
        click_count.configure(state="readonly")

    def buy_item_1(event):
        amount = int(click_count.get())
        cost = int(shop_item_1_cost['text'].split()[0])
        if amount >= cost:
            click_count.configure(state="normal")
            power = int(power_label_amount['text'])
            power *= 5
            power_label_amount.configure(text=str(power))
            amount -= cost
            click_count.delete(0, tk.END)
            click_count.insert(0, str(amount))
            cost *= 10
            shop_item_1_cost.configure(text=str(cost) + " кликов")
            click_count.configure(state="readonly")

    def buy_item_2(event):
        amount = int(click_count.get())
        if amount >= 1000000:
            click_count.configure(state="normal")
            window.config(bg="gold")
            amount -= 1000000
            click_count.delete(0, tk.END)
            click_count.insert(0, str(amount))
            click_count.configure(state="readonly")

    window = tk.Tk()                    # создаём главную форму
    window.title("UberClicker")         # заголовок окна
    window.geometry('400x300')          # размер окна
    window.resizable(0, 0)   # запрет на растягивание
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
