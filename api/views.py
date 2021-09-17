from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SentenceSerializer
from util.sentiment_analysis import TwitterSentiment
# Create your views here.


@api_view(['POST'])
def analyze_sentence(request):
    serializer = SentenceSerializer(data=request.data)
    if serializer.is_valid():
        analyzer = TwitterSentiment()
        result = analyzer.analyze(serializer.validated_data['sentence'])
        return Response({'Result': result})

    else:
        return Response(data={'Result': 'Input not valid'})
