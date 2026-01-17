from rest_framework import serializers
from .models import Company , Employee
# create serializers hear
#  It converts Company model instances into JSON format (Serialization) and converts incoming JSON data back into Python objects for saving to the database (Deserialization).
class companySerializer(serializers.HyperlinkedModelSerializer):
    comp_ID = serializers.CharField(read_only=False)
    class Meta:
        model = Company
        fields = '__all__'

class employeeSerializer(serializers.HyperlinkedModelSerializer):
    emp_ID = serializers.CharField(read_only = False)
    class Meta:
        model= Employee
        fields = '__all__'
# HyperlinkedModelSerializer: Unlike a standard ModelSerializer, this usually adds a url field to the JSON output, allowing API clients to click a link to see the specific details of a resource.