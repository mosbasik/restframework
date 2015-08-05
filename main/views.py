from django.contrib.auth.models import User

from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response

from main.models import Snippet
from main.serializers import SnippetSerializer, UserSerializer
from main.permissions import IsOwnerOrReadOnly


@api_view
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
    })


class SnippetViewSet(viewsets.ModelViewSet):
    '''
    This viewset automatically provides 'list', 'create', 'retrieve,
    'update' and 'destroy' actions.
    '''
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )

    @detail_route
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    This viewset automatically provides 'list' and 'detail' actions.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
