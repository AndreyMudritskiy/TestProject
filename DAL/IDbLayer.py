from abc import ABCMeta, abstractmethod

class IDbLayer(metaclass=ABCMeta):

    @abstractmethod
    def FoodsRepository(self):
        pass