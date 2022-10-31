from menu_item import MenuItem

class Food(MenuItem):
    def __init__(self, name, price, calorie_count):
        # Menggunakan super() panggil __init__() dari class induk
        super().__init__(name, price)
        
        # Hapus 2 baris di bawah
        # self.name = name
        # self.price = price
        
        self.calorie_count = calorie_count
    
    def info(self):
        return self.name + ': $' + str(self.price) + ' (' + str(self.calorie_count) + 'kkal)'
    
    def calorie_info(self):
        print('kkal: ' + str(self.calorie_count))