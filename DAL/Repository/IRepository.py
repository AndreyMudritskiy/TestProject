from abc import ABCMeta, abstractmethod

class IRepository(metaclass=ABCMeta):

    @abstractmethod
    def Get(self, ID):
        pass

    @abstractmethod
    def Insert(self, model):
        pass

    @abstractmethod
    def Update(self, model, ID):
        pass

    @abstractmethod
    def Delete(self, ID):
        pass