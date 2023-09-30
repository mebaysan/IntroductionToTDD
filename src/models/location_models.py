"""Location models"""


class Country(object):
    """Country model"""

    def __init__(
        self,
        name: str,
        country_code: str,
        country_code_alpha3: str,
        phone: str,
        currency: str,
    ) -> None:
        self.name = name
        self.country_code = country_code
        self.country_code_alpha3 = country_code_alpha3
        self.phone = phone
        self.currency = currency


class StateProvince(object):
    """StateProvince model"""

    def __init__(self, name: str, country: Country) -> None:
        self.name = name
        self.country = country
