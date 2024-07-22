from city_functions import get_city_info


def test_city_country_info():
    result = get_city_info("kathmandu", "nepal")
    assert result == "Kathmandu, Nepal"


def test_city_country_population_info():
    result = get_city_info("kathmandu", "nepal", "30000000")
    assert result == "Kathmandu, Nepal - Population = 30000000"
