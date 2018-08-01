from django.contrib.auth.models import User
from app.models import *
from rest_framework import serializers

class AgenteSerializer(serializers.ModelSerializer):

	#tipo_agente = serializers.StringRelatedField(many=True, read_only=True)
	class Meta:
		model = Agente
		fields = ('id')


