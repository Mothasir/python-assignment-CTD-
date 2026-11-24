
# This program retrieves country data from a public API
# and displays information about the first few countries.

import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

API_URL = "https://countries.dev/countries"


def fetch_countries():
    """Fetch country data from the public API."""
    request = Request(
        API_URL,
        headers={"User-Agent": "CountryExplorer/1.0"}
    )

    try:
        print("Connecting to the Countries API...")

        with urlopen(request, timeout=15) as response:
            data = json.load(response)

        if isinstance(data, list):
            print(f"Successfully loaded {len(data)} countries.")
            return data

        if isinstance(data, dict):
            print("API returned a dictionary.")
            return data

        print("Unexpected API data format.")
        return []

    except HTTPError as error:
        print(f"HTTP Error: {error.code}")
    except URLError as error:
        print(f"Connection Error: {error.reason}")
    except TimeoutError:
        print("The request timed out.")
    except json.JSONDecodeError:
        print("The API response is not valid JSON.")

    return []


def main():
    countries = fetch_countries()

    if isinstance(countries, list) and countries:

        # Two variables used in a print statement
        country_name = countries[0].get("name", "Unknown")
        total_countries = len(countries)

        print(
            f"The first country is {country_name} "
            f"and there are {total_countries} countries in total."
        )

        print("\nFirst five country records:")
        for country in countries[:5]:
            print(country)

    elif isinstance(countries, dict):
        print("\nReceived API data:")
        print(json.dumps(countries, indent=2)[:3000])

    else:
        print("No country data was retrieved.")


if __name__ == "__main__":
    main()
