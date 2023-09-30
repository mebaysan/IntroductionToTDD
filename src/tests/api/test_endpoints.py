"""Endpoint tests"""


def test_health_endpoint(client):
    """Test the health endpoint."""
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_index_endpoint(client):
    """Test the index endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}


def test_hello_endpoint(client):
    """Test the hello endpoint."""
    response = client.post("/hello/", json={"name": "Baysan"})
    assert response.status_code == 200
    assert response.json == {"message": "Hello, Baysan!"}


def test_endpoint_countries(client, mocked_get_country_states_from_api):
    """Test the countries endpoint."""

    response = client.get("/countries/")

    assert response.status_code == 200
    assert response.json == {
        "countries": [
            {
                "name": "Turkey",
                "country_code": "TR",
                "country_code_alpha3": "TUR",
                "phone": "90",
                "currency": "TRY",
            }
        ]
    }


def test_endpoint_country_detail(client, mocked_get_country_states_from_api):
    """Test the countries endpoint."""

    response = client.get("/countries/TR/")

    assert response.status_code == 200
    assert response.json == {
        "country": {
            "name": "Turkey",
            "country_code": "TR",
            "country_code_alpha3": "TUR",
            "phone": "90",
            "currency": "TRY",
        },
        "states": [
            {"name": "Ankara"},
            {"name": "Istanbul"},
        ],
    }


def test_endpoint_country_detail_fail(client, mocked_get_country_states_from_api):
    """Test the countries endpoint."""

    response = client.get("/countries/SALLAMASYON/")

    assert response.status_code == 404
