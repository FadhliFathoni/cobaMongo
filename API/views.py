from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import KaryawanSerializers
from Karyawan.models import Karyawan

@api_view(["GET", "POST"])
def listKaryawan(request):
    data = Karyawan.objects.all()
    serializer = KaryawanSerializers(data, many=True)
    if request.method == "POST":
        try:
            data.get_or_create(
                nama= request.data['nama'],
                password=request.data['password'],
                email=request.data['email'],
                alamat=request.data['alamat']
            )
        except:
            nama = request.data['nama']
            return Response(f"{nama} telah ada")
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteView(request,delete_id):
    Karyawan.objects.get(id = delete_id).delete()
    return redirect("/api/")

@api_view(["PUT"])
def updateView(request, nama):
    data = Karyawan.objects.filter(nama = nama)
    serializer = KaryawanSerializers(data, many=True)
    if request.method == "PUT":
        data.update(
            nama = request.data["nama"],
            password = request.data["password"],
            email = request.data["email"],
            alamat = request.data["alamat"],
        )
    return Response(serializer.data)