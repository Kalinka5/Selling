class Clothes:
    def __init__(self, Tshirt, shorts, snickers, total):
        self.Tshirt = Tshirt
        self.__priceT = 10
        self.shorts = shorts
        self.__priceSh = 8
        self.snickers = snickers
        self.__priceSn = 20
        self.total = total
        self.__maxprice = 200
    
    def sell_T_shirt(self, amount):
        if amount <= self.Tshirt:
            self.total += amount * self.__priceT
            self.Tshirt = self.Tshirt - amount
        else:
            print(f'You don`t have {amount} T-shirts!')
        return self.total
    
    def sell_shorts(self, amount):
        if amount <= self.shorts:   
            self.total += amount * self.__priceSh
            self.shorts = self.shorts - amount
        else:
            print(f'You don`t have {amount} Shorts!')
        return self.total
    
    def sell_snickers(self, amount):
        if amount <= self.snickers:
            self.total += amount * self.__priceSn
            self.snickers = self.snickers - amount
        else:
            print(f'You don`t have {amount} Snickers!')
        return self.total
    
    def result_of_selling(self):
        if self.__maxprice <= self.total:
            print(f'We have {self.total}$\nT-shirts:{self.Tshirt}, Shorts:{self.shorts}, Snickers:{self.snickers}')
        else:
            print(f'Please sell some clothes!\nT-shirts:{self.Tshirt}, Shorts:{self.shorts}, Snickers:{self.snickers}')
        
danya = Clothes(10, 10, 5, 0)
danya.sell_T_shirt(10)
danya.sell_shorts(10)
danya.sell_snickers(5)
danya.result_of_selling()