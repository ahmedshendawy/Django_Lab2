from rest_framework import serializers
from netflix.models import Movie
from .serializers import MovieSerial, UserSerial
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes


@api_view(["POST"])
def api_signup(request):
    serializer = UserSerial(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
        except Exception as e:
            return Response(data={
                "success": False,
                "errors": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={
            "success": True,
            "message": "User has been created successfully"
        }, status=status.HTTP_201_CREATED)
    return Response(data={
        "success": False,
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def index(request):
    movies = Movie.objects.all()
    seralizers= MovieSerial(instance=movies, many=True)
    return Response(data=seralizers.data, status=status.HTTP_200_OK)


@api_view(["POST",])
def create(request):
    serializer = MovieSerial(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success":True,
            "message":"Movie has been created successfuly"
        },status=status.HTTP_201_CREATED)

    return Response(data={
        "success": False,
        "errors": serializer.errors
    },status=status.HTTP_400_BAD_REQUEST)




@api_view(["POST","PUT"])
def update(request, id):
    movies=Movie.objects.get(id=id)
    serializer= MovieSerial(data=request.data, instance=movies)
    if serializer.is_valid():
        serializer.save()
        return Response(data=
        {
            "Success:": True,
            "message": "Movie has been updated"
        },
        status=status.HTTP_200_OK)

    return Response(data=
        {
            "Success:": False,
            "message": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete(request, id):
    movie=Movie.objects.get(pk=id)
    movie.delete()
    return Response(data=
        {
            "Success:": True,
            "message": "Movie has been deleted"
        },
        status=status.HTTP_204_NO_CONTENT)


class createMovie(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerial
