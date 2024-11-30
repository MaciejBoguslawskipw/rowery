import json
import os
import datetime
import smtplib
from email.mime.text import MIMEText

# Ścieżki plików
RENTALS_FILE = "data/rentals.json"
REPORTS_DIR = "data/daily_reports/"


# Funkcja obliczająca koszt wynajmu roweru
def calculate_cost(rental_duration):
    """Oblicza koszt wynajmu roweru."""
    if rental_duration <= 0:
        raise ValueError("Czas wynajmu musi być większy niż 0.")
    return 10 + max(0, rental_duration - 1) * 5


# Funkcja zapisująca wynajem roweru
def save_rental(rental, file_path=RENTALS_FILE):
    """Zapisuje wynajem do pliku JSON."""
    if not os.path.exists(file_path):
        rentals = []
    else:
        with open(file_path, "r") as file:
            rentals = json.load(file)

    rentals.append(rental)

    with open(file_path, "w") as file:
        json.dump(rentals, file, indent=4)


# Funkcja wczytująca istniejące wynajmy
def load_rentals(file_path=RENTALS_FILE):
    """Wczytuje wynajmy z pliku JSON."""
    if not os.path.exists(file_path):
        print("Brak aktywnych wynajmów.")
        return []
    with open(file_path, "r") as file:
        return json.load(file)


