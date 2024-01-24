# to validate,check whether registered users exists or not


from rest_framework import serializers
# registers user in auth user
from django.contrib.auth import get_user_model


User=get_user_model()



class UserRegister(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        