from rest_framework import serializers
from base.models import Expense, Budget
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68,min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['username','password']
    def validate(self, attrs):
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError(
                self.default_error_messages)
        return attrs
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class ExpenseSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    id = serializers.ReadOnlyField()
    class Meta:
        model = Expense
        fields = ['id','amount','category','description','user']
        extra_kwargs = {
            'category':{
                'error_messages':{
                    'invalid_choice':'Invalid Choice, Available Options are: FOOD, DATA, TRANSPORT and MISCELLANEOUS'
                }
            }
        }

class BudgetSerializers(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    id = serializers.ReadOnlyField()
    class Meta:
        model = Budget
        fields = ['id','amount','category','user']
        extra_kwargs = {
            'category':{
                'error_messages':{
                    'invalid_choice':'Invalid Choice, Available Options are: FOOD, DATA, TRANSPORT, SAVINGS and MISCELLANEOUS'
                }
            }
        }