
# System Wynajmu Rowerów

## Opis Projektu
System wynajmu rowerów to aplikacja umożliwiająca dodawanie, anulowanie i zarządzanie wynajmami rowerów. 
Dodatkowe funkcjonalności obejmują generowanie raportów dziennych oraz wysyłanie faktur e-mail. 
Zaawansowane funkcje obejmują integrację z Google Calendar.

---

## Instalacja

1. **Klonowanie repozytorium**
   Skopiuj projekt na swój komputer:
   ```bash
   git clone https://github.com/username/bike_rental.git
   cd bike_rental
   ```

2. **Instalacja zależności**
   Upewnij się, że masz zainstalowanego Pythona w wersji 3.7 lub nowszej. Zainstaluj wymagane biblioteki za pomocą pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Struktura katalogów**
   Upewnij się, że struktura katalogów wygląda następująco:
   ```
   bike_rental/
   ├── bike_rental.py
   ├── test_bike_rental.py
   ├── data/
   │   ├── rentals.json
   │   └── daily_reports/
   └── README.md
   ```

4. **Tworzenie plików konfiguracyjnych**
   - Utwórz folder `data/` w głównym katalogu, jeśli jeszcze nie istnieje.
   - Upewnij się, że w folderze `data/` istnieje plik `rentals.json` (pusty plik JSON).

---

## Jak używać

1. **Dodanie wynajmu**
   Uruchom plik `bike_rental.py` i użyj funkcji `rent_bike(customer_name, rental_duration)` do dodania wynajmu.  
   Przykład:
   ```python
   from bike_rental import rent_bike
   rent_bike("Anna Nowak", 3)
   ```

2. **Anulowanie wynajmu**
   Użyj funkcji `cancel_rental(customer_name)` do anulowania wynajmu:
   ```python
   from bike_rental import cancel_rental
   cancel_rental("Anna Nowak")
   ```

3. **Generowanie raportu dziennego**
   Użyj funkcji `generate_daily_report()`:
   ```python
   from bike_rental import generate_daily_report
   generate_daily_report()
   ```

4. **Wysyłanie faktury e-mail**
   Użyj funkcji `send_rental_invoice_email(customer_email, rental_details)`:
   ```python
   from bike_rental import send_rental_invoice_email

   rental_details = {
       "customer_name": "Anna Nowak",
       "rental_duration": 3,
       "cost": 20,
       "rental_time": "2024-01-01 12:00:00"
   }
   send_rental_invoice_email("anna.nowak@example.com", rental_details)
   ```

---

## Konfiguracja Google Calendar

1. **Uzyskanie klucza API**
   - Przejdź do konsoli [Google Cloud Console](https://console.cloud.google.com/).
   - Utwórz nowy projekt i włącz API Google Calendar.
   - Wygeneruj plik `credentials.json` i zapisz go w katalogu projektu.

2. **Instalacja bibliotek**
   Zainstaluj dodatkowe biblioteki:
   ```bash
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

3. **Integracja w kodzie**
   Skonfiguruj przypomnienia zwrotu roweru, dodając do swojego skryptu integrację z Google Calendar.

---

## Testowanie

1. **Uruchamianie testów**
   Plik `test_bike_rental.py` zawiera testy jednostkowe dla systemu. Aby uruchomić testy, wykonaj:
   ```bash
   python -m unittest test_bike_rental.py
   ```

---

## Autorzy
Projekt stworzony przez Maciej Bogusławski .

---

## Licencja
Projekt udostępniany na licencji MIT. Szczegóły znajdują się w pliku `LICENSE`.
