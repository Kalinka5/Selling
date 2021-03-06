# make class Clothes where we can buy and sell some clothes and then see a profit
class Clothes:
    # make init capital-our start sum 
    def __init__(self, capital):
        self.capital1 = capital
        self.capital2 = self.capital1   # If you wanna profit from start sum
        self.amount_T_shirt = 0         # how many clothes you have at start
        self.amount_Shorts = 0
        self.amount_Sneakers = 0
        self.__cost_buy_Tshirt = 35     # how much clothes cost to buy
        self.__cost_buy_Shorts = 40
        self.__cost_buy_Sneakers = 100
        self.__cost_sell_Tshirt = 40    # how much clothes cost to sell
        self.__cost_sell_Shorts = 46
        self.__cost_sell_Sneakers = 115
    
    # function where you can buy some clothes and lost money
    def buy_clothes(self, amountT, amountSh, amountSn):
        '''self.capital2 = self.capital1''' # If you wanna profit from end sum
        if amountT == 0 and amountSh == 0 and amountSn == 0:
            print('If you wanna buy smth, please enter numbers > 0)')
        elif self.capital1 >= self.__cost_buy_Tshirt and amountT >= 0 and amountSh >= 0 and amountSn >= 0:
            self.amount_T_shirt = self.amount_T_shirt + amountT
            self.amount_Shorts = self.amount_Shorts + amountSh
            self.amount_Sneakers = self.amount_Sneakers + amountSn
            self.capital1 = self.capital1 - self.__cost_buy_Tshirt * amountT - self.__cost_buy_Shorts * amountSh - self.__cost_buy_Sneakers * amountSn 
            if self.capital1 < 0:
                print('You don`t have enough money')
            else:
                print('============TIME TO SHOPPING!============')
                print(f'You have: {self.amount_T_shirt} T-shirt, {self.amount_Shorts} Shorts, {self.amount_Sneakers} Sneakers')
                if self.capital1 < self.__cost_buy_Tshirt:
                    print(f'And you have left {self.capital1}$\n')
                elif self.capital1 < self.__cost_buy_Shorts:
                    print(f'And you have left {self.capital1}$')
                    print('You can buy 1 T-shirt!')
                elif self.capital1 < self.__cost_buy_Sneakers:
                    print(f'And you have left {self.capital1}$')
                    print('You can get more T-Shirts or Shorts!')
                else:
                    print(f'And you have left {self.capital1}$')
                    print('You can get more T-Shirts or Shorts or even Sneakers!\n')
        else:
            print('You don`t have enough money or enter positive number!')
            
    # function where you sell some clothes and make money
    def sell_clothes(self, amountT, amountSh, amountSn):
        if amountT >= 0 and amountSh >= 0 and amountSn >= 0:
            if amountT == 0 and amountSh == 0 and amountSn == 0:
                print('Please sell some clothes, if you have) !')
            elif amountT <= self.amount_T_shirt and amountSh <= self.amount_Shorts and amountSn <= self.amount_Sneakers:
                self.amount_T_shirt = self.amount_T_shirt - amountT
                self.amount_Shorts = self.amount_Shorts - amountSh
                self.amount_Sneakers = self.amount_Sneakers - amountSn
                self.capital1 = self.capital1 + self.__cost_sell_Tshirt * amountT + self.__cost_sell_Shorts * amountSh + self.__cost_sell_Sneakers * amountSn 
                if self.amount_T_shirt == 0 and self.amount_Shorts == 0 and self.amount_Sneakers == 0:
                    print('============TIME TO SELLING!=============')
                    print('You`ve got nothing left!')
                else:
                    print('============TIME TO SELLING!=============')
                    print(f'You have: {self.amount_T_shirt} T-shirt, {self.amount_Shorts} Shorts, {self.amount_Sneakers} Sneakers')
                print(f'Your capital: {self.capital1}$\n')
            else:
                print('You don`t have enough clothes!')
                print(f'You have: {self.amount_T_shirt} T-shirt, {self.amount_Shorts} Shorts, {self.amount_Sneakers} Sneakers')
        else:
            print('Please enter positive number!')
            
    # function where we count profit from start or end sum     
    def profit(self):
        if self.capital1 > self.capital2:
            profit = self.capital1 - self.capital2
            print(f'Your profit: {profit}$\n')
        else:
            print('You don`t have profit yet')
    
    # represent your capital 
    def __repr__(self):
        return f'You have {self.capital1}$.\n\n'
       
# testing Clothes        
danya = Clothes(1000)
print(danya)
danya.buy_clothes(8, 8, 4)
danya.sell_clothes(8, 7, 4)
danya.sell_clothes(0, 1, 0)
danya.buy_clothes(8, 9, 5)
danya.sell_clothes(7, 8, 4)
danya.profit()

