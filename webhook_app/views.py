from django.http import JsonResponse
from webhook_app.models import Post
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook_handler(request):
    if request.method == 'POST':
        # Fetch all posts from the database
        posts = Post.objects.all()

        # Serialize posts data using GraphQL type
        posts_data = [serialize_post(post) for post in posts]
        
        # Return posts data in the response
        return JsonResponse({'status': 'success', 'posts': posts_data})
    else:
        # Handle other request methods (e.g., GET, PUT, DELETE) as needed
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def serialize_post(post):
    return {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'created_at': post.created_at.strftime("%Y-%m-%d %H:%M:%S")  # Format the datetime as needed
    }
