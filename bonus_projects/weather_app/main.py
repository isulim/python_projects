from model import get_weather, get_weather_details, Weather

"""
Bonus assignment:
1) Make it so the app retrieves the users city through their IP address
2) Use that city to give them details about their current location
3) Clean the data in the console to make it look more user friendly :)
"""


def main():
    # Ask the user for their city
    user_city: str = input('Enter a city: ')

    # Get the current weather details
    current_weather: dict = (get_weather(user_city, mock=False))
    weather_details: list[Weather] = get_weather_details(current_weather)

    # Get the current days
    days: set[str] = {date.date.day for date in weather_details}

    for day in days:
        print(day)
        print('---')

        # Group the weather data by date to make it easier to read
        grouped: list[Weather] = [current for current in weather_details if current.date.day == day]
        for element in grouped:
            print(element)

        print()  # An empty line


if __name__ == '__main__':
    main()
