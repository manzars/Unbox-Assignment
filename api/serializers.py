from common.models import TechStack
from django.db.models.fields import EmailField
from rest_framework import serializers
from developers.models import Developer, Designation, TechStack
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'age', 'sex', 'email']


class DeveloperSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tech_stack = serializers.StringRelatedField(many=True)
    designation = serializers.StringRelatedField()
    employment_type = serializers.StringRelatedField()

    class Meta:
        model = Developer
        fields = "__all__"


class DeveloperCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = ['id', 'user', 'designation', 'tech_stack', 'total_experience', 'employment_type',
                  'location', 'annual_ctc', 'linked_in_profile', 'start_date', 'end_date']
        extra_kwargs = {
            'user': {'read_only': False}
        }
