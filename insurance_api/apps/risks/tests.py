import copy
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from insurance_api.risks.models import RiskType, RiskField
from insurance_api.risks.serializers import RiskTypeSerializer

data = {
    'risk_name': 'Akindele Farms',
    'risk_type': 'property',
    'risk_fields': [
        {'field_name': 'address', 'field_type': 'text'}
    ]
}


class RiskTypeTests(APITestCase):
    def test_create_risk_type_name_is_required(self):
        """
        Ensure we can't create a new risk type without a name.
        """
        copied_data = copy.deepcopy(data)
        copied_data.pop('risk_name')
        serializer = RiskTypeSerializer(data=copied_data)
        self.assertEqual(serializer.is_valid(), False)

    def test_create_risk_type_type_is_required(self):
        """
        Ensure we can't create a new risk type without a type.
        """
        copied_data = copy.deepcopy(data)
        copied_data.pop('risk_type')
        serializer = RiskTypeSerializer(data=copied_data)
        self.assertEqual(serializer.is_valid(), False)

    def test_create_risk_type_fields_is_required(self):
        """
        Ensure we can't create a new risk type without fields.
        """
        copied_data = copy.deepcopy(data)
        copied_data.pop('risk_fields')
        serializer = RiskTypeSerializer(data=copied_data)
        self.assertEqual(serializer.is_valid(), False)

    def test_create_risk_type_fields_field_name_is_required(self):
        """
        Ensure we can't create a new risk type with any of the fields not having a name.
        """
        copied_data = copy.deepcopy(data)
        copied_data['risk_fields'][0].pop('field_name')
        serializer = RiskTypeSerializer(data=copied_data)
        self.assertEqual(serializer.is_valid(), False)

    def test_create_risk_type_fields_field_type_is_invalid(self):
        """
        Ensure we can't create a new risk type with any of the fields having invalid field_type.
        """
        copied_data = copy.deepcopy(data)
        copied_data['risk_fields'][0]['field_type'] = 'invalid'
        serializer = RiskTypeSerializer(data=copied_data)
        self.assertEqual(serializer.is_valid(), False)

    def test_create_risk_type_valid_data(self):
        """
        Ensure we can create a new risk type.
        """
        url = reverse('risk-type-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RiskType.objects.count(), 1)
        self.assertEqual(RiskField.objects.count(), 1)
        self.assertEqual(RiskType.objects.get().risk_name, 'Akindele Farms')

    def test_get_all_risk_types(self):
        """
        Ensure we can get a list of our created risks.
        """
        url = reverse('risk-type-list')
        self.client.post(url, data, format='json')
        self.client.post(url, data, format='json')
        self.client.post(url, data, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(RiskType.objects.count(), 3)
        self.assertEqual(RiskField.objects.count(), 3)

    def test_get_one_risk_type(self):
        """
        Ensure we can get a particular risk type with an ID.
        """
        url = reverse('risk-detail', args=[1])
        self.client.post(reverse('risk-type-list'), data, format='json')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(RiskType.objects.count(), 1)
        self.assertEqual(response.data['id'], 1)
