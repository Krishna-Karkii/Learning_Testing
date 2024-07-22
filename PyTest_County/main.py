from city_functions import get_city_info

print("Input Joiner")
print("Enter q to quit")
while True:
    city_name = input("Enter a city name: ")
    if city_name.strip().lower() == "q":
        break
    country_name = input("Enter the city's country: ")
    if country_name.strip().lower() == "q":
        break
    response = get_city_info(city_name, country_name)
    print(response)
