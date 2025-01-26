import tkinter as tk
from inventory_module import InventoryModule

class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Склад мебельного магазина")
        self.master.geometry("600x400")  # Установите размер основного окна

        self.inventory_button = tk.Button(master, text="Управление запасами", command=self.open_inventory)
        self.inventory_button.pack(pady=20)

        self.quit_button = tk.Button(master, text="Выход", command=master.quit)
        self.quit_button.pack(pady=20)

    def open_inventory(self):
        inventory_window = tk.Toplevel(self.master)
        inventory_window.geometry("500x300")  # Установите размер окна управления запасами
        InventoryModule(inventory_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()