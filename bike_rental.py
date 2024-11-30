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


# Funkcja anulująca wynajem
def cancel_rental(customer_name, file_path=RENTALS_FILE):
    """Usuwa wynajem na podstawie imienia klienta."""
    rentals = load_rentals(file_path)
    updated_rentals = [r for r in rentals if r["customer_name"] != customer_name]

    if len(rentals) == len(updated_rentals):
        print(f"Nie znaleziono wynajmu dla klienta: {customer_name}.")
        return

    with open(file_path, "w") as file:
        json.dump(updated_rentals, file, indent=4)
    print(f"Wynajem dla klienta {customer_name} został anulowany.")


# Funkcja dodająca wynajem
def rent_bike(customer_name, rental_duration):
    """Dodaje wynajem roweru."""
    try:
        cost = calculate_cost(rental_duration)
        rental = {
            "customer_name": customer_name,
            "rental_duration": rental_duration,
            "cost": cost,
            "rental_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        save_rental(rental)
        print(f"Wynajem zapisany. Klient: {customer_name}, Koszt: {cost} zł")
    except ValueError as e:
        print(f"Błąd: {e}")


# Funkcja generująca raport dzienny
def generate_daily_report(file_path=RENTALS_FILE, report_dir=REPORTS_DIR):
    """Generuje raport dzienny na podstawie aktywnych wynajmów."""
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    report_file = os.path.join(report_dir, f"daily_report_{date_str}.json")

    rentals = load_rentals(file_path)

    with open(report_file, "w") as report:
        json.dump(rentals, report, indent=4)

    print(f"Raport dzienny zapisany jako {report_file}.")


# Funkcja wysyłająca fakturę e-mailem
def send_rental_invoice_email(customer_email, rental_details):
    """Wysyła fakturę wynajmu roweru na e-mail klienta."""
    try:
        smtp_server = "smtp.example.com"
        smtp_port = 587
        sender_email = "your_email@example.com"
        sender_password = "your_password"

        subject = "Faktura za wynajem roweru"
        body = (
            f"Dziękujemy za skorzystanie z naszej wypożyczalni rowerów.\n\n"
            f"Szczegóły wynajmu:\n"
            f"Imię: {rental_details['customer_name']}\n"
            f"Czas wynajmu: {rental_details['rental_duration']} godz.\n"
            f"Koszt: {rental_details['cost']} zł\n"
            f"Data wynajmu: {rental_details['rental_time']}\n\n"
            f"Pozdrawiamy,\nZespół Bike Rental"
        )

        message = MIMEText(body, "plain")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = customer_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)

        print(f"Faktura wysłana na adres: {customer_email}")
    except Exception as e:
        print(f"Błąd podczas wysyłania e-maila: {e}")


