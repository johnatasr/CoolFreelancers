from rest_framework import serializers


class FreelancerSearchedSerializer(serializers.Serializer):
    id = serializers.IntegerField
    computedSkills = serializers.OrderedDict()
