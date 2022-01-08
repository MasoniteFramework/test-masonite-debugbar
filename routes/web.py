from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    Route.get("/_debugbar/@id", "WelcomeController@get_debug"),
    Route.get("/_debugbar/", "WelcomeController@debug"),
    Route.get("/api/users", "WelcomeController@api"),
]

