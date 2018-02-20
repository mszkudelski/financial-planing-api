from rest_framework import serializers

from restexample.models import Revenue, Expense, Category, Plan

class ValidationMsgs:
    value= 'This field must be greater than 0',
    category= {
        'r': 'Wrong category type. Should be \'r\' like \'revenue\'.',
        'e': 'Wrong category type. Should be \'e\' like \'expense\''
    }


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'type')

class RevenueSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Category.objects.all())
    description = serializers.CharField(allow_blank=True)
    class Meta:
        model = Revenue
        fields = ('id', 'value', 'name', 'category', 'description')
    def validate_value(self, value):
        if value > 0:
            return value
        else:
            raise serializers.ValidationError(ValidationMsgs.value)
    def validate_category(self, category):
        if category.type == 'r':
            return category
        else:
            raise serializers.ValidationError(ValidationMsgs.category['r'])

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Category.objects.all())
    description = serializers.CharField(allow_blank=True, read_only=True)
    class Meta:
        model = Expense
        fields = ('id', 'value', 'name', 'category', 'description')
    def validate_value(self, value):
        if value > 0:
            return value
        else:
            raise serializers.ValidationError(ValidationMsgs.value)
    def validate_category(self, category):
        if category.type == 'e':
            return category
        else:
            raise serializers.ValidationError(ValidationMsgs.category['e'])


class PlanSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Category.objects.all())
    date = serializers.DateField(read_only=True)
    class Meta:
        model = Plan
        fields = ('id', 'value', 'category', 'date')
    def validate_value(self, value):
        if value > 0:
            return value
        else:
            raise serializers.ValidationError(ValidationMsgs.value)
    def validate_category(self, category):
        if category.type == 'e':
            return category
        else:
            raise serializers.ValidationError(ValidationMsgs.category['e'])
