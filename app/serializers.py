from rest_framework import serializers
from .models import Customer, ExistingParty, Chinese, Uzbek
from .utils import create_key_word


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name_surname', 'telegram_id', 'key_word', 'created_at']
        read_only_fields = ['key_word']

    def create(self, validated_data):
        customer = Customer.objects.filter().last()
        key = create_key_word(customer=customer)
        validated_data['key_word'] = key
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name_surname = validated_data.get('name_surname', instance.name_surname)
        instance.telegram_id = validated_data.get('telegram_id', instance.telegram_id)
        instance.save()
        return instance


class ExistingPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExistingParty
        fields = ['id', "party_name", "register_date"]


class ChineseCustomerKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['key_word']


class ChineseSerializer(serializers.ModelSerializer):
    customer_key = ChineseCustomerKeySerializer()

    class Meta:
        model = Chinese
        fields = ['id', 'track_code', 'item_name', 'customer_key', 'item_number', 'item_weight', 'box_name',
                  'created_at']


class ChineseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chinese
        fields = ['party', 'track_code', 'item_name', 'customer_key', 'item_number', 'item_weight', 'box_name']


class ChineseTractCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chinese
        fields = ['track_code']


class UzbekSerializer(serializers.ModelSerializer):
    customer_key = ChineseCustomerKeySerializer()
    track_code = ChineseTractCodeSerializer()

    class Meta:
        model = Uzbek
        fields = ['id', 'track_code', 'price_per_kg', 'customer_key', 'item_weight', 'paid', 'created_at']


class UzbekCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uzbek
        fields = ['party', 'track_code', 'price_per_kg', 'customer_key', 'item_weight', 'paid']
