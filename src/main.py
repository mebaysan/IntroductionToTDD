"""Main module for the application."""
import os
from flask import Flask, request
from services.location import get_country_states


def create_app():
    """Create a Flask application."""
    app = Flask(__name__)

    app.config.update(
        SECRET_KEY=os.environ.get("SECRET_KEY", "dev"),
        DEBUG=os.environ.get("BAYSANSOFT_APP_DEBUG", False),
    )

    @app.route("/health/")
    def health_check():
        """Return a health check."""
        return {"status": "ok"}

    @app.route("/")
    def index():
        """Return a friendly HTTP greeting."""
        return {"message": "Hello, World!"}

    @app.route("/hello/", methods=["POST"])
    def hello():
        """Return a custom greeting to the name provided in the request body."""
        name = request.json.get("name")
        if not name:
            return {"error": "Please provide a name"}, 400
        return {"message": f"Hello, {name}!"}

    @app.route("/countries/")
    def countries():
        """Return a list of countries."""
        country_states = get_country_states()
        return {
            "countries": [country["country"].__dict__ for country in country_states]
        }

    @app.route("/countries/<country_code>/")
    def country(country_code):
        """Return a country by country code."""
        country_states = get_country_states()
        for country in country_states:
            if country["country"].country_code == country_code:
                return {
                    "country": country["country"].__dict__,
                    "states": [{"name": state.name} for state in country["states"]],
                }

        return {"error": "Country not found"}, 404

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5000)
