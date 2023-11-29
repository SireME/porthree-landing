Project API Documentation
=========================

This documents just the API

This documentation provides details on the API routes available in the Django project. The API is designed to manage various entities related to user profiles, posts, comments, skills, social links, hero sections, themes, projects, and project tools.

Base URL
--------

The base URL for the API is `http://your-api-base-url.com/api/`

API Endpoints
-------------

### Users

**GET /api/users/**

Retrieves a list of all users.

Bash

    curl http://your-api-base-url.com/api/users/
    

content\_copy

**POST /api/users/**

Creates a new user.

Bash

    curl -X POST http://your-api-base-url.com/api/users/ -H "Content-Type: application/json" -d '{
      "email": "newuser@example.com",
      "career_title": "Software Engineer",
      "user_name": "newuser",
      "phone_number": 1234567890,
      "first_name": "New",
      "last_name": "User",
      "rating": 0,
      "password": "your_password"
    }'
    

**GET /api/users/{id}/**

Retrieves details of a specific user.

Bash

    curl http://your-api-base-url.com/api/users/{id}/
    

**PUT /api/users/{id}/**

Updates details of a specific user.

Bash

    curl -X PUT http://your-api-base-url.com/users/{id}/ -H "Content-Type: application/json" -d '{
      "first_name": "Updated",
      "last_name": "User"
    }'
    

**DELETE /users/{id}/**

Deletes a specific user.

Bash

    curl -X DELETE http://your-api-base-url.com/users/{id}/
    

### Post Tags

**GET /api/posttags/**

Retrieves a list of post tags.

Bash

    curl http://your-api-base-url.com/api/posttags/
    

**POST /api/posttags/**

Creates a new post tag.

Bash

    curl -X POST http://your-api-base-url.com/api/posttags/ -H "Content-Type: application/json" -d '{
      "name": "Tag Name"
    }'
    

**GET /api/posttags/{id}/**

Retrieves details of a specific post tag.

Bash

    curl http://your-api-base-url.com/api/posttags/{id}/
    

**PUT /api/posttags/{id}/**

Updates details of a specific post tag.

Bash

    curl -X PUT http://your-api-base-url.com/api/posttags/{id}/ -H "Content-Type: application/json" -d '{
      "name": "Updated Tag Name"
    }'
    

**DELETE /api/posttags/{id}/**

Deletes a specific post tag.

Bash

    curl -X DELETE http://your-api-base-url.com/api/posttags/{id}/
    

### Posts

**GET /api/posts/**

Retrieves a list of posts.

Bash

    curl http://your-api-base-url.com/api/posts/
    

**POST /api/posts/**

Creates a new post.

Bash

    curl -X POST http://your-api-base-url.com/posts/ -H "Content-Type: application/json" -d '{
      "user": "user_id",
      "title": "Post Title",
      "content": "Post Content"
    }'
    

**GET /api/posts/{id}/**

Retrieves details of a specific post.

Bash

    curl http://your-api-base-url.com/api/posts/{id}/
    

**PUT /api/posts/{id}/**

Updates details of a specific post.

Bash

    curl -X PUT http://your-api-base-url.com/api/posts/{id}/ -H "Content-Type: application/json" -d '{
      "title": "Updated Post Title"
    }'
    

**DELETE /posts/{id}/**

Deletes a specific post.

Bash

    curl -X DELETE http://your-api-base-url.com/api/posts/{id}/
    

(Continue the same structure for other models like Comments, Skills, Socials, Heroes, Themes, Projects, ProjectTools, etc.)
