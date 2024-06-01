import graphene
from graphene_django.types import DjangoObjectType
from webhook_app.models import Post
import requests

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        content = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, title, content):
        post = Post(title=title, content=content)
        post.save()
        return CreatePost(post=post)

class TriggerWebhook(graphene.Mutation):
    class Arguments:
        webhook_url = graphene.String()

    success = graphene.Boolean()

    def mutate(self, info, webhook_url):
        # Here you can make HTTP requests to the webhook_url
        # For simplicity, let's just print it
        print(f"Webhook triggered to: {webhook_url}")
        # You can also send data to the webhook if needed
        # For example:
        requests.post(webhook_url, json={'message': 'Hello from Django!'})
        return TriggerWebhook(success=True)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    trigger_webhook = TriggerWebhook.Field()

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
