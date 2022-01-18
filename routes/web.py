from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get("/api/users", "WelcomeController@api"),
    Route.get("/api/me", "WelcomeController@api"),
    Route.get("/api/profile", "WelcomeController@profile"),
    Route.get("/api/settings", "WelcomeController@settings"),
]

