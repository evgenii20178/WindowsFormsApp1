import tkinter as tk
from tkinter import messagebox

class InventoryModule:
    def __init__(self, master):
        self.master = master
        self.master.title("Управление запасами")
        self.master.geometry("500x300")  # Установите размер окна управления запасами
        
        self.label = tk.Label(master, text="Введите количество товара:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Добавить", command=self.add_item)
        self.add_button.pack(pady=10)

        self.quit_button = tk.Button(master, text="Выход", command=master.quit)
        self.quit_button.pack(pady=10)

    def add_item(self):
        item_count = self.entry.get()
        if item_count.isdigit():
            messagebox.showinfo("Успех", f"Товар добавлен. Количество: {item_count}")
        else:
            messagebox.showerror("Ошибка", "Введите корректное количество!")