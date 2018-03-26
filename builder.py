"""
建造者模式（Builder Pattern）使用多个简单的对象一步一步构建成一个复杂的对象。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。

一个 Builder 类会一步一步构造最终的对象。该 Builder 类是独立于其他对象的。
"""


"""
在这里，我们定义一套肯德基套餐的制造过程，用来体现建造者模式。
"""
from abc import ABCMeta, abstractmethod


class Builder:
    __metaclass__ = ABCMeta

    @abstractmethod
    def build_burger(self)


class Diretor:
    """指挥者"""
    pass




class Client:
    pass


