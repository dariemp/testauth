from rest_framework import serializers
from models import Distro


class DistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Distro
        fields = ('id','name','description')
