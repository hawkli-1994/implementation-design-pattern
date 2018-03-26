"""
原型模式
原型模式是创建型模式的一种，其特点在于通过“复制”一个已经存在的实例来返回新的实例,而不是新建实例。被复制的实例就是我们所称的“原型”，这个原型是可定制的。

原型模式多用于创建复杂的或者耗时的实例，因为这种情况下，复制一个已经存在的实例使程序运行更高效；或者创建值相等，只是命名不一样的同类数据。
"""
from abc import ABCMeta, abstractmethod
import copy

class Prototype:
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @abstractmethod
    def clone(self):
        pass

class ConcretePrototypeA(Prototype):

    def clone(self):
        return copy.copy(self)

class ConcretePrototypeB(Prototype):
    """
    具体原型类
    """

    def clone(self):
        return copy.copy(self)


class Manager:

    def __init__(self):
        self._dict = {}

    def register(self, name, prototype):
        self._dict[name] = prototype

    def create(self, proto_name):
        p = self._dict.get(proto_name)
        return p.clone()

if __name__ == '__main__':
    ca = ConcretePrototypeA('ca')
    ca2 = ca.clone()

    cb = ConcretePrototypeB('cb')
    cb2 = cb.clone()

    m = Manager()
    m.register("ca", ca)
    m.register("cb", cb)
    x = m.create("cb")
    print(x)
    