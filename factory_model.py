"""
简单工厂模式

实现一个肯德基类
可以生产汉堡
"""


class Foodstuff:
    """食材"""
    vegetables = 'vegetables'  # 蔬菜
    meat = 'meat'  # 肉
    fruits = 'fruits'  # 水果
    eggs = 'eggs'  # 鸡蛋

class Hamburger:

    def __init__(self, *args):
        j = "".join([i + ' ' for i in args])
        self.name = "this is a {} hamburger".format(j)
        print("Make a {} burger".format(j))

    def __str__(self):
        return self.name

class VegetablesMeat(Foodstuff):
    """蔬菜水果汉堡"""
    
    def get_hamburger(self):
        return Hamburger(self.vegetables, self.fruits)


class FruitsEggs(Foodstuff):
    """水果鸡蛋汉堡"""
    def get_hamburger(self):
        return Hamburger(self.fruits, self.eggs)

class KFCFactory:

    @staticmethod
    def buy_hamburger(hamburger_name):
        if hamburger_name == 'vegetables fruits':
            return VegetablesMeat()
        elif hamburger_name == 'fruits eggs':
            return FruitsEggs()
        else:
            return VegetablesMeat()
        


if __name__ == '__main__':
    vegetables_fruits = KFCFactory.buy_hamburger('vegetables fruits').get_hamburger()
    fruits_eggs = KFCFactory.buy_hamburger('fruits eggs').get_hamburger()

