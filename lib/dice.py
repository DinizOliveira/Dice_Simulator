class Dice:
    def __init__(self, choice):
        if choice == 1:
            self.max_value = 4
            return
        elif choice == 2:
            self.max_value = 6
            return
        elif choice == 3:
            self.max_value = 8
            return
        elif choice == 4:
            self.max_value = 10
            return
        elif choice == 5:
            self.max_value = 12
            return
        elif choice == 6:
            self.max_value = 20
            return
        elif choice == 7:
            self.max_value = 100
            return
        else: 
            return 0
