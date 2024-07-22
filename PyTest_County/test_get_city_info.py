from city_functions import get_city_info


def test_city_country_info():
    result = get_city_info("kathmandu", "nepal")
    assert result == "Kathmandu, Nepal"
