"""Location service to get country and state data from a JSON file"""
import requests
from models.location_models import Country, StateProvince


def get_country_states_from_api():
    url = "https://gist.githubusercontent.com/mebaysan/610479b2e5362853b876637aa1f58883/raw/0969bb2ba61f28da6e6d55a881b088cd83e53ba6/country_state.json"
    response = requests.get(url, timeout=5)
    return response.json()


def get_country_states():
    """Returns a list of countries and their states from a JSON file"""

    data = get_country_states_from_api()
    countries_states_db = []

    for country_data in data:
        country = Country(
            name=country_data["name"],
            country_code=country_data["countryCode"],
            country_code_alpha3=country_data["countryCodeAlpha3"],
            phone=country_data["phone"],
            currency=country_data["currency"],
        )
        countries_states_db.append({"country": country, "states": []})
        if country_data["stateProvinces"] is not None:
            for state_data in sorted(
                country_data["stateProvinces"], key=lambda x: x["name"]
            ):
                state = StateProvince(
                    name=state_data["name"],
                    country=country,
                )
                countries_states_db[-1]["states"].append(state)
    return countries_states_db
