# In myproject/urls.py

from django.urls import path
from graphene_django.views import GraphQLView
from webhook_app.views import webhook_handler

urlpatterns = [
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('webhook/', webhook_handler, name='webhook_handler'),
]
