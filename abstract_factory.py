"""
抽象工厂模式（Abstract Factory Pattern）是围绕一个超级工厂创建其他工厂。该超级工厂又称为其他工厂的工厂。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。

在抽象工厂模式中，接口是负责创建一个相关对象的工厂，不需要显式指定它们的类。每个生成的工厂都能按照工厂模式提供对象。

所以这里给KFC增加一个产品族，鸡肉卷.就变成，汉堡和鸡肉卷两种产品了
"""

from abc import ABCMeta, abstractmethod


class AbsFood:
    """可以认为鸡肉卷和汉堡都是食物，共用一个基类"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def taste(self):
        """味道"""
        pass

    @abstractmethod
    def name(self):
        """名字"""
        pass


class AbsFoodFactory:
    """一个抽象的工厂，作为基类"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_food(self):
        pass


class Hamburger(AbsFood):
    """汉堡"""

    def __init__(self, material):
        self.material = str(material)

    def taste(self):
        print("like shit")

    def name(self):
        print("{} Hamburger".format(self.material))


class ChickenRoll(AbsFood):
    """鸡肉卷"""

    def __init__(self, material):
        self.material = str(material)

    def taste(self):
        print("like Chicken")

    def name(self):
        print("{} Chicken roll".format(self.material))


class HamburgerFactory(AbsFoodFactory):
    """汉堡工厂"""

    def __init__(self, material):
        self.material = material

    def get_food(self):
        return Hamburger(self.material)


class ChickenRollFactory(AbsFoodFactory):
    """鸡肉卷工厂"""

    def __init__(self, material):
        self.material = material

    def get_food(self):
        return ChickenRoll(self.material)


class KFC:
    @staticmethod
    def get_food_factory(factory_name):
        if factory_name == 'hamburger':
            return HamburgerFactory#(material)
        elif factory_name == 'chickenroll':
            return ChickenRollFactory#(material)

if __name__ == '__main__':
    hamburger_factory = KFC.get_food_factory("hamburger")
    hamburger = hamburger_factory("fruit").get_food()
    hamburger.name()
    hamburger.taste()

    chickenroll_factory = KFC.get_food_factory("chickenroll")
    chickenroll = chickenroll_factory("chicken").get_food()
    chickenroll.taste()
    chickenroll.name()



