"""Initialize Flask app."""
from flask import Flask

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():
        # Import parts of our application
        from .home import routes
        from .budget import routes

        # Register Blueprints
        app.register_blueprint(home.home_bp)
        app.register_blueprint(budget.budget_bp, url_prefix='/budget')
        return app
