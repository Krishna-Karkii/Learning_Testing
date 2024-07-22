def get_city_info(city_name, country_name, population=""):

    """Get city and country name, join them, and return the titled
    version"""
    if population != "":
        result = f"{city_name}, {country_name} - population = {population}"
    else:
        result = f"{city_name}, {country_name}"

    return result.title()
