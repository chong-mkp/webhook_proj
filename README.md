# About
Webhook example on Django and GraphQL

# Install
```
pip3 install django graphene-django
```

# Migrate and run server
```
python3 manage.py makemigrations webhook_app
python3 manage.py migrate
python3 manage.py runserver
```

# To test the wehbook
```
curl -X POST http://127.0.0.1:8000/webhook/
```

* Example result
```
{
  "status": "success",
  "posts": [
    {
      "id": 1,
      "title": "New Post Title1",
      "content": "Here we are 1",
      "created_at": "2024-06-01 15:36:10"
    },
    {
      "id": 2,
      "title": "New Post Title2",
      "content": "Here we are 2",
      "created_at": "2024-06-01 15:36:16"
    }
  ]
}
```


# To access GraphQL Playground
```
http://127.0.0.1:8000/graphql/
```


# To add example modal
```
mutation {
  createPost(title: "New Post Title", content: "Lorem ipsum dolor sit amet") {
    post {
      id
      title
      content
    }
  }
}
```


# To query all modal
```
query MyQuery {
  allPosts {
    content
    createdAt
    id
    title
  }
}
```
