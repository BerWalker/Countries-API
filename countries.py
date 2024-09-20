import json
import sys
import requests

BASE_URL = "https://restcountries.com/v2"


def request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException:
        print(f"Error making request to: {url}")


def country_count():
    countries = request(f"{BASE_URL}/all")
    if countries:
        return len(countries)


def list_countries():
    countries = request(f"{BASE_URL}/all")
    if countries:
        for country in countries:
            print(country['name'])


def show_population(country_name):
    countries = request(f"{BASE_URL}/name/{country_name}")
    if countries:
        for country in countries:
            print(f"{country['name']}: {country['population']} inhabitants")


def show_currencies(country_name):
    countries = request(f"{BASE_URL}/name/{country_name}")
    if countries:
        for country in countries:
            print(f"Currencies of {country['name']}:")
            for currency in country['currencies']:
                print(f"{currency['name']} - {currency['code']}")


def read_country_name():
    if len(sys.argv) > 2:
        return sys.argv[2]
    print("Please provide the name of a country.")
    return None


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("## Welcome to the countries system ##")
        print("Usage: python countries.py <action> <country name>")
        print("Actions: count, currency, population")
    else:
        action = sys.argv[1]

        if action == "count":
            print(f"There are {country_count()} countries in the world.")
        elif action in ["currency", "population"]:
            country = read_country_name()
            if country:
                if action == "currency":
                    show_currencies(country)
                elif action == "population":
                    show_population(country)
        else:
            print("Invalid action.")
