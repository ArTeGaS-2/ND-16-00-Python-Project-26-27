class Order:
    def __init__(self):
        self.available_topings = {
            "кетчуп": 123,
            "майонез": 152,
            "ковбаса": 123,
            "Сир": 173,
            "Ананас": 555
        }
        self.pizza_size = None

    def pizza_size_choice(self):
        self.pizza_size = input("Оберіть розмір піци: /n")
        print(f"Розмір піци {self.pizza_size} см")