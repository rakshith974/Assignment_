import requests

URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(URL)
    data = response.json()
    return data

def temperature_find(data, target_date):
    for entry in data['list']:
        if entry['dt_txt'] == target_date:
            return entry['main']['temp']
    return None

def get_wind_speed(data, target_date):
    for entry in data['list']:
        if entry['dt_txt'] == target_date:
            return entry['wind']['speed']
    return None

def get_pressure(data, target_date):
    for entry in data['list']:
        if entry['dt_txt'] == target_date:
            return entry['main']['pressure']
    return None

def main():
    data = get_weather_data()

    while True:
        print("\nOptions:")
        print("1. Get Temperature")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            break
        elif choice == 1:
            target_date = input("Enter date with time (YYYY-MM-DD HH:MM:SS): ")
            temperature = temperature_find(data, target_date)
            if temperature is not None:
                print(f"Temperature at {target_date}: {temperature} K")
            else:
                print("Data not found for the given date and time.")
        elif choice == 2:
            target_date = input("Enter date with time (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(data, target_date)
            if wind_speed is not None:
                print(f"Wind Speed at {target_date}: {wind_speed} m/s")
            else:
                print("Data not found for the given date and time.")
        elif choice == 3:
            target_date = input("Enter date with time (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(data, target_date)
            if pressure is not None:
                print(f"Pressure at {target_date}: {pressure} hPa")
            else:
                print("Data not found for the given date and time.")
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

