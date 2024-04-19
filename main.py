from os import path
from tjfu import TJFU
from datetime import timedelta

HERE = path.abspath(path.dirname(__file__))

def error_404(error):
    return "Not Found!!!", 404

def error_500(error):
    return "Error!!!", 500

"""
    The TJFU configuration must be placed
    at the beginning of the main function.
    Absolutely do not define or import any Route
    before calling the build() function because an error may occur.
"""
(
    TJFU
    .host_name("0.0.0.0") # required
    .host_port(3100) # required        
    .root_path(HERE) # optinal (default: '.')        
    .template_folder("templates") # optinal (default: 'templates')
    .static_folder("static") # optinal (default: 'static')
    .jwt_secret_key("your_jwt_secret_key")
        # optinal / enter value if you want to use JWT, 
        # Otherwise the jwt_required function will throw an error
    .jwt_access_token_expires(timedelta(days=7)) # optinal (default: 'timedelta(days=7)')
    .jwt_refresh_token_expires(timedelta(days=14)) # optinal (default: 'timedelta(days=14)')
    .socket_root("socket") # optinal (default: 'socket') 
    .ignore_cors(True) # optinal (default: 'True')
    .add_error_handler(404, error_404) # optional
    .add_error_handler(500, error_500) # optional
    .limiter_storage_uri("memory://") # optinal (default: 'memory://')
    .default_limits(["200 per day", "50 per hour"]) # optinal (default: '[]')
    .log_output(False) # optinal (default: 'True')
    .debug(False) # optinal (default: 'True')
    .use_reloader(False) # optinal (default: 'True')
    .allow_unsafe_werkzeug(True) # optinal (default: 'True')
    .build()
)

from tjfu import SimpleRenderTemplateRoute

app = TJFU.init_app(SimpleRenderTemplateRoute("index", "/" ,"index.html"))

IS_PRODUCTION = False

if __name__ == "__main__":
    if IS_PRODUCTION:
        app.run()
    else:
        TJFU.run()