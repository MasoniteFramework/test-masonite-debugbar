from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get("/_debugbar/@id", "WelcomeController@get_debug"),
    Route.get("/_debugbar/", "WelcomeController@debug"),
    Route.get("/api/users", "WelcomeController@api"),
    Route.get("/api/me", "WelcomeController@api"),
    Route.get("/api/profiles", "WelcomeController@profile"),
    Route.get("/api/settings", "WelcomeController@settings"),
]

