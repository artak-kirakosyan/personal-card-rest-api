from rest_framework import viewsets, status
from rest_framework.response import Response

from api.models import PersonalCard
from api.serializers import PersonalCardSerializer


class PersonalCardViewSet(viewsets.ModelViewSet):
    """
    Endpoints for interacting with personal cards
    """
    queryset = PersonalCard.objects.all().order_by(
        "last_name", "name", "middle_name"
    )
    serializer_class = PersonalCardSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        personal_card = PersonalCard.objects.filter(
            **serializer.validated_data).first()
        if personal_card is not None:
            serializer = self.get_serializer(personal_card)
            data = serializer.data
            status_code = status.HTTP_200_OK
        else:
            self.perform_create(serializer)
            data = serializer.data
            status_code = status.HTTP_201_CREATED
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status_code, headers=headers)
