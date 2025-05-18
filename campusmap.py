import webbrowser
import pyttsx3  # For text-to-speech

def open_map_route(start_address, end_coordinates):
    """Opens a Google Maps route in the browser."""
    end_lat, end_lon = end_coordinates
    url = f"https://www.google.com/maps/dir/{start_address}/{end_lat},{end_lon}"
    webbrowser.open_new_tab(url)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    engine = pyttsx3.init()

    # Dictionary of destinations with coordinates (Update if you have more accurate ones)
    locations = {
        "1": ("Vignan Canteen", (17.3443066, 78.7222610)),
        "2": ("Vignan Cafeteria", (17.343803, 78.723112)),  # Nearby point
        "3": ("Pharmacy Block", (17.344901, 78.722725)),
        "4": ("Library", (17.345270, 78.722540)),
        "5": ("Administrative Block", (17.344580, 78.721980)),
        "6": ("Vignan University", (17.344163, 78.722121)),
    }

    # Get user's current location
    speak("Hi, I am your Vignan campus navigation bot. Please enter your current location.")
    start_address = input("Enter your current location: ")

    # Display the menu
    speak("Here are the places you can navigate to:")
    for key, (name, _) in locations.items():
        print(f"{key}. {name}")
    speak("Please enter the number corresponding to your destination.")

    # Get user choice
    choice = input("Enter your destination number: ").strip()

    if choice in locations:
        destination_name, end_coordinates = locations[choice]
        speak(f"Here is the route from {start_address} to {destination_name}. Opening Google Maps now.")
        open_map_route(start_address, end_coordinates)
    else:
        speak("Sorry, I didn't recognize that choice. Please run the program again and select a valid option.")
