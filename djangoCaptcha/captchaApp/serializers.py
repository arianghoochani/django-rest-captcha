from rest_framework import serializers
from rest_captcha.serializers import RestCaptchaSerializer
class HumanOnlyDataSerializer(RestCaptchaSerializer,serializers.Serializer):
    captcha_key = serializers.CharField()
    captcha_value = serializers.CharField()