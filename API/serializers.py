from rest_framework import serializers
from Karyawan.models import Karyawan

class KaryawanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Karyawan
        fields = "__all__"