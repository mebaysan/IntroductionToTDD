"""Test fixtures."""
import pytest
from main import create_app


@pytest.fixture
def app():
    """Create an application for the tests."""
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture
def client(app):
    """Client for the app to make requests"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Click runner for the app to run commands"""
    return app.test_cli_runner()


@pytest.fixture
def mocked_get_country_states_from_api(mocker):
    mocker.patch(
        "services.location.get_country_states_from_api",
        return_value=[
            {
                "name": "Turkey",
                "countryCode": "TR",
                "countryCodeAlpha3": "TUR",
                "phone": "90",
                "currency": "TRY",
                "stateProvinces": [
                    {"name": "Istanbul"},
                    {"name": "Ankara"},
                ],
            }
        ],
    )
