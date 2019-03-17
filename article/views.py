from rest_framework import viewsets
from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import permissions
from article.permissions import IsOwnerOrReadOnly
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.http import Http404

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


# class ArticleList(APIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly,)
#
#     def get(self, request, format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=self.request.user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class ArticleDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Article.objects.get(pk=pk)
#         except Article.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         article = self.get_object(pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         article = self.get_object(pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


