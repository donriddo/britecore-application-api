from rest_framework import serializers

from .models import RiskType, RiskField, Risk


class RiskFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskField
        fields = ('id', 'field_name', 'field_type',
                  'enum_choices', 'default_value')


class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = ('id', 'json_body')


class RiskTypeSerializer(serializers.ModelSerializer):
    risk_fields = RiskFieldSerializer(many=True)

    class Meta:
        model = RiskType
        fields = ('id', 'created_at', 'risk_name', 'risk_type', 'risk_fields')

    def create(self, validated_data):
        fields_data = validated_data.pop('risk_fields')
        risk_type = RiskType.objects.create(**validated_data)
        for field_data in fields_data:
            risk_field = RiskField.objects.create(**field_data)
            risk_type.risk_fields.add(risk_field)
        return risk_type
