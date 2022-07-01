from rest_framework import generics, permissions

from user import serializers


class CurrentUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = serializers.CurrentUserSerializer

    def get_object(self):
        return self.request.user
