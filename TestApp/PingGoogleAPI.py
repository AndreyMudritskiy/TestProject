from DAL.DbLayer import DbLayer
from DAL.DomainModel.Food import Food
import unittest
from DAL.Dataprovider.GoogleSheets.GoogleSheetsDataProvider import GoogleSheetsDataProvider


class testAPI(unittest.TestCase):

    def runTest(self):
        dblayer = DbLayer(GoogleSheetsDataProvider())
        model = Food()
        model.Name = "test"
        model.Proteins = "2"
        model.Fats = "3"

        id = dblayer.FoodsRepository().Insert(model)
        self.assertNotEqual(id , None, "Failed to inser object")

        rFood = dblayer.FoodsRepository().Get(id)
        self.assertEqual(rFood.Name, model.Name, "Name reading failed")
        self.assertEqual(rFood.Proteins, model.Proteins, "Name reading failed")
        self.assertEqual(rFood.Fats, model.Fats, "Name reading failed")

        rFood.Name = "newTest"
        dblayer.FoodsRepository().Update(rFood,id)
        uFood = dblayer.FoodsRepository().Get(id)
        self.assertEqual(rFood.Name, uFood.Name, "Name update failed")

        dblayer.FoodsRepository().Delete(id)
        dFood = dblayer.FoodsRepository().Get(id)
        self.assertEqual(dFood, None, "Name update failed")


test = testAPI()
test.runTest()

