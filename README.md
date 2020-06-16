A twitter-like, Django based RESTful API.

Supported API endpoints:
1. CreateUser(Userame) - POST request.
2. PostMessage(UserId, Content) - POST request.
3. Follow(FollowingUser, FollowedUser) - POST request.
4. UnFollow(FollowingUser, FollowedUser) - DELETE request.
5. GetFeed(Userid) - GET request.
6. GetGlobalFeed - GET request.

Built With:
* Django - The web framework.
* Django REST Framework - A REST api toolkit.
* PostgreSQL - The supported DB.
