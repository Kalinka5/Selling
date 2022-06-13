class Clothes:
    def __init__(self, capital):
        self.amount_T_shirt = 0
        self.amount_Shorts = 0
        self.amount_Sneakers = 0
        self.__cost_buy_Tshirt = 35
        self.__cost_buy_Shorts = 40
        self.__cost_buy_Sneakers = 100
        self.capital = capital
        self.__cost_sell_Tshirt = 40
        self.__cost_sell_Shorts = 46
        self.__cost_sell_Sneakers = 115
    
    def buy_clothes(self, amountT, amountSh, amountSn):
        if amountT >= 0 and amountSh >= 0 and amountSn >= 0:
            self.amount_T_shirt = amountT
            self.amount_Shorts = amountSh
            self.amount_Sneakers = amountSn
            self.capital = self.capital - self.__cost_buy_Tshirt * amountT - self.__cost_buy_Shorts * amountSh - self.__cost_buy_Sneakers * amountSn
            if self.capital >= 0:
                print(f'You have {amountT} T-shirt, {amountSh} Shorts, {amountSn} Sneakers')
                if self.capital < self.__cost_buy_Tshirt:
                    print(f'And you have left {self.capital}$\n')
                elif self.capital < self.__cost_buy_Shorts:
                    print(f'And you have left {self.capital}$')
                    print('You can buy 1 T-shirt!')
                elif self.capital < self.__cost_buy_Sneakers:
                    print(f'And you have left {self.capital}$')
                    print('You can get more T-Shirts or Shorts!')
                else:
                    print(f'And you have left {self.capital}$')
                    print('You can get more T-Shirts or Shorts or even Sneakers!\n')
            else:
                print('You don`t have enough money!')
        else:
            print('Please enter positive number!')
    
    def sell_clothes(self, amountT, amountSh, amountSn):
        if amountT >= 0 and amountSh >= 0 and amountSn >= 0:
            if amountT == 0 and amountSh == 0 and amountSn == 0:
                print('Please sell some clothes!')
            elif amountT <= self.amount_T_shirt and amountSh <= self.amount_Shorts and amountSn <= self.amount_Sneakers:
                self.amount_T_shirt = self.amount_T_shirt - amountT
                self.amount_Shorts = self.amount_Shorts - amountSh
                self.amount_Sneakers = self.amount_Sneakers - amountSn
                self.capital = self.capital + self.__cost_sell_Tshirt * amountT + self.__cost_sell_Shorts * amountSh + self.__cost_sell_Sneakers * amountSn
                print(f'You have {self.amount_T_shirt} T-shirt, {self.amount_Shorts} Shorts, {self.amount_Sneakers} Sneakers')
                print(f'Your capital: {self.capital}$')
            else:
                print('You don`t have enough clothes!')
                print(f'You have {self.amount_T_shirt} T-shirt, {self.amount_Shorts} Shorts, {self.amount_Sneakers} Sneakers')
        else:
            print('Please enter positive number!')
        
    '''def result_of_selling(self):
        if self.total >= self.__maxprice:
            print(f'We have {self.total}$\nT-shirts:{self.Tshirt}, Shorts:{self.shorts}, Snickers:{self.snickers}')
        else:
            print(f'Please sell some clothes!\nT-shirts:{self.Tshirt}, Shorts:{self.shorts}, Snickers:{self.snickers}')'''
        
danya = Clothes(1000)
danya.buy_clothes(8, 8, 4)
danya.sell_clothes(0, 0, 0)