# Backend Development Learning Plan

## Overview
This 30-day learning plan is designed for beginners to progressively build a social media application backend using Flask. Each day includes specific tasks with clear objectives, gradually increasing in complexity while building on previous knowledge.

## Week 1: Understanding the Basics & Simple Enhancements

### Day 1: Project Setup & Environment Configuration
- **Morning Session (1.5 hours)**
  - [ ] Clone the repository
  - [ ] Create a virtual environment: `python -m venv .venv`
  - [ ] Activate the virtual environment: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Mac/Linux)
  - [ ] Install dependencies: `pip install -r requirements.txt`

- **Afternoon Session (2 hours)**
  - [ ] Set up PostgreSQL database
    - Install PostgreSQL if not already installed
    - Create a database named `social_media_dev`
    - Update `.env` file with your database credentials
  - [ ] Run database migrations: `flask db upgrade`
  - [ ] Start the application: `python run.py`
  - [ ] Test the health check endpoint: `GET /health`

### Day 2: Code Walkthrough & Understanding Architecture
- **Morning Session (2 hours)**
  - [ ] Study the project structure
    - Identify the key directories: `app`, `config`, `migrations`
    - Understand the purpose of each directory
  - [ ] Analyze the MVC architecture
    - Models: `app/models/`
    - Views/Controllers: `app/controllers/`
    - Routes: `app/routes/`

- **Afternoon Session (2 hours)**
  - [ ] Trace a request flow
    - Follow a request from route to controller to service to model
    - Use the user registration endpoint as an example
  - [ ] Test existing endpoints using Postman
    - Import the `postman_collection.json` file
    - Test user registration, login, and CRUD operations

### Day 3: User Model Enhancement - Part 1
- **Morning Session (2 hours)**
  - [ ] Add new fields to the User model in `app/models/user.py`
    - Add `bio` (Text field)
    - Add `location` (String field)
    - Add `website` (String field)
  - [ ] Create a database migration
    - Run: `flask db migrate -m "Add profile fields to User model"`
    - Run: `flask db upgrade`

- **Afternoon Session (2 hours)**
  - [ ] Update the UserSchema in `app/schemas/user_schema.py`
    - Add validation for new fields
    - Ensure proper serialization/deserialization
  - [ ] Test the changes by creating a new user with the new fields

### Day 4: User Model Enhancement - Part 2
- **Morning Session (2 hours)**
  - [ ] Add profile picture support
    - Add `profile_picture_url` field to User model
    - Create a migration for the new field
  - [ ] Create a utility function for handling file uploads
    - Create `app/utils/file_utils.py`
    - Implement a function to save uploaded files

- **Afternoon Session (2 hours)**
  - [ ] Create a new endpoint for uploading profile pictures
    - Add a new route in `app/routes/user_routes.py`
    - Implement the controller method in `app/controllers/user_controller.py`
  - [ ] Test the profile picture upload functionality

### Day 5: Authentication Improvement - JWT Implementation
- **Morning Session (2 hours)**
  - [ ] Install Flask-JWT-Extended: `pip install flask-jwt-extended`
  - [ ] Add JWT configuration in `app/__init__.py`
  - [ ] Update `requirements.txt` with the new dependency

- **Afternoon Session (2 hours)**
  - [ ] Modify the login endpoint to return JWT tokens
    - Update `app/controllers/user_controller.py`
    - Generate access and refresh tokens
  - [ ] Create a protected route that requires authentication
    - Add a new endpoint that returns the current user's details
    - Secure it with JWT authentication

### Day 6: Authentication Improvement - JWT Protection
- **Morning Session (2 hours)**
  - [ ] Create authentication middleware
    - Create `app/utils/auth.py`
    - Implement decorators for route protection
  - [ ] Add token refresh endpoint
    - Create a new route for refreshing tokens
    - Implement the controller method

- **Afternoon Session (2 hours)**
  - [ ] Secure existing routes with authentication
    - Add authentication to update and delete user endpoints
    - Ensure only the owner can modify their profile
  - [ ] Test all secured endpoints with valid and invalid tokens

### Day 7: Password Reset Functionality
- **Morning Session (2 hours)**
  - [ ] Create password reset token generation
    - Add a method to User model to generate reset tokens
    - Store token expiration time
  - [ ] Create endpoints for requesting password reset
    - Add routes in `app/routes/user_routes.py`
    - Implement controller methods

- **Afternoon Session (2 hours)**
  - [ ] Implement token validation and password update
    - Create endpoint to validate reset token
    - Create endpoint to update password with valid token
  - [ ] Mock email notification service
    - Create `app/services/notification_service.py`
    - Implement a method to "send" password reset emails (log instead of actually sending)

## Week 2: Core Social Media Features

### Day 8: Post Model Creation
- **Morning Session (2 hours)**
  - [ ] Create Post model in `app/models/post.py`
    - Add fields: `id`, `user_id`, `content`, `created_at`, `updated_at`
    - Define relationship with User model
  - [ ] Update User model to include relationship with posts
  - [ ] Create database migration for the Post model

- **Afternoon Session (2 hours)**
  - [ ] Create PostSchema in `app/schemas/post_schema.py`
    - Define fields and validation rules
    - Create schema instances for single and multiple posts
  - [ ] Test database operations with the new model

### Day 9: Post CRUD Operations - Part 1
- **Morning Session (2 hours)**
  - [ ] Create PostService in `app/services/post_service.py`
    - Implement `create_post` method
    - Implement `get_post_by_id` method
  - [ ] Create PostController in `app/controllers/post_controller.py`
    - Implement methods for creating and retrieving posts

- **Afternoon Session (2 hours)**
  - [ ] Create post routes in `app/routes/post_routes.py`
    - Add routes for creating and retrieving posts
    - Register the blueprint in `app/__init__.py`
  - [ ] Test the new endpoints using Postman

### Day 10: Post CRUD Operations - Part 2
- **Morning Session (2 hours)**
  - [ ] Add remaining CRUD operations to PostService
    - Implement `update_post` method
    - Implement `delete_post` method
    - Implement `get_posts_by_user_id` method

- **Afternoon Session (2 hours)**
  - [ ] Complete the PostController
    - Implement methods for updating and deleting posts
    - Add authentication checks to ensure only the author can modify posts
  - [ ] Add the remaining routes to post_routes.py
  - [ ] Test all post endpoints

### Day 11: Media Support for Posts
- **Morning Session (2 hours)**
  - [ ] Enhance Post model with media support
    - Add `media_url` field to Post model
    - Create a migration for the new field
  - [ ] Update PostSchema to include media fields

- **Afternoon Session (2 hours)**
  - [ ] Enhance file upload utility to support post media
    - Modify `app/utils/file_utils.py` to handle different file types
    - Implement validation for image/video files
  - [ ] Update post creation and update endpoints to handle media uploads
  - [ ] Test media upload functionality

### Day 12: Follow/Unfollow Functionality - Part 1
- **Morning Session (2 hours)**
  - [ ] Create Follower model in `app/models/follower.py`
    - Add fields: `id`, `follower_id`, `followed_id`, `created_at`
    - Define relationships with User model
  - [ ] Update User model with follower relationships
  - [ ] Create database migration for the Follower model

- **Afternoon Session (2 hours)**
  - [ ] Create FollowerService in `app/services/follower_service.py`
    - Implement `follow_user` method
    - Implement `unfollow_user` method
    - Implement methods to check if a user is following another

### Day 13: Follow/Unfollow Functionality - Part 2
- **Morning Session (2 hours)**
  - [ ] Create FollowerController in `app/controllers/follower_controller.py`
    - Implement methods for following and unfollowing users
    - Add authentication checks
  - [ ] Create follower routes in `app/routes/follower_routes.py`
    - Add routes for follow/unfollow actions
    - Register the blueprint in `app/__init__.py`

- **Afternoon Session (2 hours)**
  - [ ] Enhance FollowerService with additional methods
    - Implement `get_followers` method to get a user's followers
    - Implement `get_following` method to get users a user is following
  - [ ] Add corresponding controller methods and routes
  - [ ] Test all follower-related endpoints

### Day 14: Feed Implementation
- **Morning Session (2 hours)**
  - [ ] Create FeedService in `app/services/feed_service.py`
    - Implement method to get posts from followed users
    - Add sorting by creation date
  - [ ] Implement pagination support
    - Add offset and limit parameters
    - Return total count and pagination metadata

- **Afternoon Session (2 hours)**
  - [ ] Create FeedController in `app/controllers/feed_controller.py`
    - Implement method to get user's feed
    - Add authentication requirement
  - [ ] Create feed routes in `app/routes/feed_routes.py`
    - Add route for retrieving feed
    - Register the blueprint in `app/__init__.py`
  - [ ] Test feed functionality with multiple users and posts

## Week 3: Engagement Features & Performance

### Day 15: Like Functionality
- **Morning Session (2 hours)**
  - [ ] Create Like model in `app/models/like.py`
    - Add fields: `id`, `user_id`, `post_id`, `created_at`
    - Define relationships with User and Post models
  - [ ] Update Post model with like relationship
  - [ ] Create database migration for the Like model

- **Afternoon Session (2 hours)**
  - [ ] Create LikeService in `app/services/like_service.py`
    - Implement `like_post` method
    - Implement `unlike_post` method
    - Implement `get_post_likes` method
  - [ ] Create LikeController and routes
  - [ ] Test like functionality

### Day 16: Comment Functionality - Part 1
- **Morning Session (2 hours)**
  - [ ] Create Comment model in `app/models/comment.py`
    - Add fields: `id`, `user_id`, `post_id`, `content`, `created_at`, `updated_at`
    - Define relationships with User and Post models
  - [ ] Update Post model with comment relationship
  - [ ] Create database migration for the Comment model

- **Afternoon Session (2 hours)**
  - [ ] Create CommentSchema in `app/schemas/comment_schema.py`
    - Define fields and validation rules
    - Create schema instances for single and multiple comments
  - [ ] Create CommentService in `app/services/comment_service.py`
    - Implement `create_comment` method
    - Implement `get_comment_by_id` method

### Day 17: Comment Functionality - Part 2
- **Morning Session (2 hours)**
  - [ ] Complete CommentService
    - Implement `update_comment` method
    - Implement `delete_comment` method
    - Implement `get_comments_by_post_id` method

- **Afternoon Session (2 hours)**
  - [ ] Create CommentController in `app/controllers/comment_controller.py`
    - Implement CRUD methods for comments
    - Add authentication checks
  - [ ] Create comment routes in `app/routes/comment_routes.py`
  - [ ] Test all comment endpoints

### Day 18: Nested Comments (Replies)
- **Morning Session (2 hours)**
  - [ ] Enhance Comment model with parent-child relationship
    - Add `parent_id` field (nullable)
    - Add self-referential relationship
  - [ ] Create database migration for the new field

- **Afternoon Session (2 hours)**
  - [ ] Update CommentService to handle replies
    - Modify `create_comment` to accept parent_id
    - Add method to get replies for a comment
  - [ ] Update CommentController and routes
  - [ ] Test nested comment functionality

### Day 19: Basic Caching Implementation
- **Morning Session (2 hours)**
  - [ ] Install Redis and Flask-Caching
    - Add to requirements.txt
    - Set up Redis locally
  - [ ] Configure caching in the application
    - Add cache configuration to `app/__init__.py`
    - Create cache instance

- **Afternoon Session (2 hours)**
  - [ ] Implement caching for user profiles
    - Modify UserService to cache user data
    - Add cache invalidation on user updates
  - [ ] Test caching functionality
    - Verify improved response times for cached data

### Day 20: Advanced Caching Strategies
- **Morning Session (2 hours)**
  - [ ] Implement caching for posts
    - Cache individual posts
    - Cache user's posts list
  - [ ] Implement caching for feed
    - Cache feed results with appropriate keys

- **Afternoon Session (2 hours)**
  - [ ] Create a cache management utility
    - Add methods for common cache operations
    - Implement cache key generation strategies
  - [ ] Implement cache invalidation for related data
    - Invalidate feed caches when new posts are created
    - Invalidate post caches when comments or likes change

### Day 21: Database Optimization
- **Morning Session (2 hours)**
  - [ ] Add database indexes
    - Identify fields that need indexing (foreign keys, search fields)
    - Create migrations to add indexes
  - [ ] Implement eager loading for related data
    - Modify queries to use `joinedload` where appropriate

- **Afternoon Session (2 hours)**
  - [ ] Optimize complex queries
    - Identify and refactor inefficient queries
    - Use subqueries or CTEs for complex operations
  - [ ] Test performance improvements
    - Compare response times before and after optimization

## Week 4: Advanced Features & Testing

### Day 22: Notification System - Part 1
- **Morning Session (2 hours)**
  - [ ] Create Notification model in `app/models/notification.py`
    - Add fields: `id`, `user_id`, `type`, `data`, `read`, `created_at`
    - Define relationship with User model
  - [ ] Create database migration for the Notification model

- **Afternoon Session (2 hours)**
  - [ ] Create NotificationService in `app/services/notification_service.py`
    - Implement methods to create different types of notifications
    - Implement methods to mark notifications as read
    - Implement method to get user's notifications

### Day 23: Notification System - Part 2
- **Morning Session (2 hours)**
  - [ ] Create notification triggers
    - Add notification creation to like, comment, and follow actions
    - Implement notification for new followers
  - [ ] Create NotificationController and routes
    - Add endpoints to get and manage notifications

- **Afternoon Session (2 hours)**
  - [ ] Install and configure Flask-SocketIO
    - Add to requirements.txt
    - Set up WebSocket support in `app/__init__.py`
  - [ ] Implement real-time notification delivery
    - Create event handlers for notifications
    - Test real-time notification delivery

### Day 24: Search Functionality
- **Morning Session (2 hours)**
  - [ ] Implement user search
    - Create SearchService in `app/services/search_service.py`
    - Add method to search users by username or name
    - Optimize with database indexes

- **Afternoon Session (2 hours)**
  - [ ] Implement post search
    - Add method to search posts by content
    - Add hashtag extraction from post content
    - Create endpoint for searching by hashtag
  - [ ] Create SearchController and routes
  - [ ] Test search functionality

### Day 25: Unit Testing - Part 1
- **Morning Session (2 hours)**
  - [ ] Set up testing environment
    - Configure test database
    - Create test fixtures and helpers
  - [ ] Write tests for UserService
    - Test user creation, retrieval, update, and deletion
    - Test authentication methods

- **Afternoon Session (2 hours)**
  - [ ] Write tests for PostService
    - Test post creation, retrieval, update, and deletion
    - Test post retrieval by user
  - [ ] Run tests and fix any issues

### Day 26: Unit Testing - Part 2
- **Morning Session (2 hours)**
  - [ ] Write tests for FollowerService
    - Test follow/unfollow functionality
    - Test follower/following retrieval
  - [ ] Write tests for LikeService and CommentService

- **Afternoon Session (2 hours)**
  - [ ] Write tests for FeedService
    - Test feed generation
    - Test pagination
  - [ ] Add test coverage reporting
    - Install and configure coverage tool
    - Generate and analyze coverage reports

### Day 27: Integration Testing
- **Morning Session (2 hours)**
  - [ ] Create API test fixtures
    - Set up test client
    - Create helper functions for authentication
  - [ ] Write tests for user endpoints
    - Test registration, login, and profile management

- **Afternoon Session (2 hours)**
  - [ ] Write tests for post and engagement endpoints
    - Test post creation and interaction
    - Test comments and likes
  - [ ] Write tests for feed and search endpoints
  - [ ] Run all tests and ensure passing status

### Day 28: API Documentation
- **Morning Session (2 hours)**
  - [ ] Install and configure Swagger/OpenAPI
    - Add Flask-RESTX or similar library
    - Set up basic API documentation structure
  - [ ] Document user endpoints
    - Add descriptions, parameters, and response examples

- **Afternoon Session (2 hours)**
  - [ ] Document remaining endpoints
    - Posts, comments, likes, followers, etc.
    - Add authentication requirements
  - [ ] Create a comprehensive Postman collection
    - Update the existing collection with all endpoints
    - Add environment variables for easier testing

### Day 29: Containerization
- **Morning Session (2 hours)**
  - [ ] Create Dockerfile
    - Define base image and dependencies
    - Configure application for containerized environment
  - [ ] Create docker-compose.yml
    - Add services for app, database, and Redis
    - Configure networking and volumes

- **Afternoon Session (2 hours)**
  - [ ] Implement environment-specific configurations
    - Create separate config files for different environments
    - Use environment variables for sensitive information
  - [ ] Test containerized application
    - Build and run with Docker Compose
    - Verify all functionality works in containers

### Day 30: Monitoring and Deployment Preparation
- **Morning Session (2 hours)**
  - [ ] Implement structured logging
    - Configure logging formats and levels
    - Add context information to logs
  - [ ] Create health check and monitoring endpoints
    - Add detailed health check with component status
    - Add performance metrics endpoint

- **Afternoon Session (2 hours)**
  - [ ] Prepare deployment documentation
    - Document deployment steps and requirements
    - Create a production checklist
  - [ ] Final review and testing
    - Perform end-to-end testing of all features
    - Address any remaining issues
  - [ ] Celebrate completing the 30-day learning journey!

## Learning Outcomes

By the end of this plan, you will have learned:

1. **Backend Architecture**
   - MVC pattern implementation
   - Separation of concerns
   - RESTful API design

2. **Database Management**
   - ORM usage with SQLAlchemy
   - Database relationships (one-to-many, many-to-many)
   - Query optimization
   - Indexing strategies

3. **Authentication & Security**
   - JWT implementation
   - Password hashing
   - Secure API design
   - Input validation

4. **Performance Optimization**
   - Caching strategies
   - Database query optimization
   - Efficient file handling

5. **Testing & Quality Assurance**
   - Unit and integration testing
   - Test-driven development
   - API documentation

6. **Deployment & DevOps**
   - Containerization
   - Environment configuration
   - Monitoring and logging

## Next Steps After Completing This Plan

After completing this 30-day plan, consider these advanced topics:

1. **Scaling the Application**
   - Implementing a message queue (RabbitMQ, Kafka)
   - Horizontal scaling with load balancers

2. **Advanced Security**
   - Implementing rate limiting
   - Adding CSRF protection
   - Security auditing

3. **Infrastructure as Code**
   - Using Terraform or CloudFormation
   - Setting up CI/CD pipelines

4. **Microservices Architecture**
   - Breaking down the monolith into microservices
   - Implementing service discovery 