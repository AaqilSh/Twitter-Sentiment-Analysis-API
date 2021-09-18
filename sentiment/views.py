from django.shortcuts import render
from .forms import SentimentForm
from util.sentiment_analysis import TwitterSentiment
# Create your views here.


def index(request):
    result = ''
    if request.method == 'POST':
        form = SentimentForm(data=request.POST)
        if form.is_valid():
            sentence = form.cleaned_data['sentence']
            analyzer = TwitterSentiment()
            result = analyzer.analyze(sentence)
    else:
        form = SentimentForm()
    return render(request, template_name='sentiment/index.html', context={'form': form, 'result': result})
