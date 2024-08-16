from django.shortcuts import render
from .services import search_books
from .models import Recommendation,Like,Comment
from django.shortcuts import render
from .forms import RecommendationForm
from rest_framework import viewsets
from .serializers import RecommendationSerializer


def search_view(request):
    query = request.POST.get('name', 'default')
    if (query!=""):
        results = search_books(query) if query else []
        return render(request, 'search_results.html', {'results': results["items"], 'query': query})
    else:
        text="Please Enter Book Name"
        return render(request, 'search_results.html', {'text': text})

def submit_recommendations(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            recommendation = form.save(commit=False)
            recommendation.user = request.user
            recommendation.save()
            form = RecommendationForm()
            return render(request,'submit_recommendation.html',{'form': form})
    else:
        form = RecommendationForm()
    return render(request, 'submit_recommendation.html', {'form': form})

def recommendations_view(request):
    recommendations = Recommendation.objects.all()
    likes = Like.objects.all()
    comments = Comment.objects.all()
    print(likes)
    return render(request, 'recommendations.html',{'recommendations': recommendations,'likes':likes,'comments':comments})

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    print(queryset)
    serializer = RecommendationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



