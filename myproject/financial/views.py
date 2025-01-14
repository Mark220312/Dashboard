from rest_framework import viewsets
from .models import FinancialMovement
from .serializers import FinancialMovementSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FinancialMovement

class FinancialMovementViewSet(viewsets.ModelViewSet):
    queryset = FinancialMovement.objects.all()
    serializer_class = FinancialMovementSerializer


def categories(request):
    if request.method == 'GET':
        categories = FinancialMovement.objects.values_list('category', flat=True).distinct()
        return JsonResponse(list(categories), safe=False)