
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

        # Some APIs return a dictionary containing the country list.
        if isinstance(data, dict):
            print("API returned a dictionary.")
            print("Available keys:", list(data.keys()))
            return data

        if isinstance(data, list):
            print(f"Successfully loaded {len(data)} countries.")
            return data

        print("Unexpected API data format.")
        return []

    except HTTPError as error:
        print(f"HTTP error: {error.code}")
    except URLError as error:
        print(f"Connection error: {error.reason}")
    except TimeoutError:
        print("The request timed out.")
    except json.JSONDecodeError:
        print("The API response is not valid JSON.")

    return []


def main():
    countries = fetch_countries()

    if isinstance(countries, list) and countries:
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
