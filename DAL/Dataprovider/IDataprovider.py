from abc import ABCMeta, abstractmethod

class IDataprovider(metaclass=ABCMeta):

    @abstractmethod
    def GetRow(self, ID):
        pass

    @abstractmethod
    def InsertRow(self, model):
        pass

    @abstractmethod
    def UpdateRow(self, model, ID):
        pass

    @abstractmethod
    def DeleteRow(self, ID):
        pass
