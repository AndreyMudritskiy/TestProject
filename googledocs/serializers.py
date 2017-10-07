from rest_framework import serializers
from DAL.DomainModel.Food import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('Name', 'Proteins', 'Fats')

    def RestoreModel(self):
        food = Food()
        food.Name = self.data['Name']
        food.Proteins = self.data['Proteins']
        food.Fats = self.data['Fats']
        return food
