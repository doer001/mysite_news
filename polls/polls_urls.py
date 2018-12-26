from django.urls import path, include
from .views import index, results, vote, detail

app_name = 'polls'
urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', include([
        path('', detail, name='detail'),
        path('vote/', vote, name='vote'),
        path('results/', results, name='results'),
    ])),
]
