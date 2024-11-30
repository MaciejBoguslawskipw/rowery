import unittest
import os
import json
from bike_rental import (
    calculate_cost,
    save_rental,
    load_rentals,
    cancel_rental,
    rent_bike,
    generate_daily_report,
)

# Ścieżki testowe
TEST_RENTALS_FILE = "test_data/test_rentals.json"
TEST_REPORTS_DIR = "test_data/test_reports/"


class TestBikeRental(unittest.TestCase):
    def setUp(self):
        """Przygotowanie środowiska testowego."""
        if not os.path.exists("test_data"):
            os.makedirs("test_data")

        # Tworzenie pustego pliku JSON dla testów
        with open(TEST_RENTALS_FILE, "w") as file:
            json.dump([], file)

    def tearDown(self):
        """Czyszczenie po testach."""
        if os.path.exists(TEST_RENTALS_FILE):
            os.remove(TEST_RENTALS_FILE)

        if os.path.exists(TEST_REPORTS_DIR):
            for report_file in os.listdir(TEST_REPORTS_DIR):
                os.remove(os.path.join(TEST_REPORTS_DIR, report_file))
            os.rmdir(TEST_REPORTS_DIR)

    # Testy dla calculate_cost
    def test_calculate_cost_single_hour(self):
        self.assertEqual(calculate_cost(1), 10)

    def test_calculate_cost_multiple_hours(self):
        self.assertEqual(calculate_cost(3), 20)

    def test_calculate_cost_invalid_duration(self):
        with self.assertRaises(ValueError):
            calculate_cost(0)

    # Testy dla save_rental i load_rentals
    def test_save_and_load_rental(self):
        rental = {
            "customer_name": "Test User",
            "rental_duration": 2,
            "cost": 15,
            "rental_time": "2024-01-01 12:00:00",
        }
        save_rental(rental, TEST_RENTALS_FILE)
        rentals = load_rentals(TEST_RENTALS_FILE)
        self.assertEqual(len(rentals), 1)
        self.assertEqual(rentals[0]["customer_name"], "Test User")

    # Testy dla cancel_rental
    def test_cancel_rental(self):
        rental1 = {"customer_name": "User1", "rental_duration": 2, "cost": 15, "rental_time": "2024-01-01 12:00:00"}
        rental2 = {"customer_name": "User2", "rental_duration": 3, "cost": 20, "rental_time": "2024-01-01 13:00:00"}
        save_rental(rental1, TEST_RENTALS_FILE)
        save_rental(rental2, TEST_RENTALS_FILE)

        cancel_rental("User1", TEST_RENTALS_FILE)
        rentals = load_rentals(TEST_RENTALS_FILE)
        self.assertEqual(len(rentals), 1)
        self.assertEqual(rentals[0]["customer_name"], "User2")

    def test_cancel_nonexistent_rental(self):
        rental = {"customer_name": "User1", "rental_duration": 2, "cost": 15, "rental_time": "2024-01-01 12:00:00"}
        save_rental(rental, TEST_RENTALS_FILE)

        cancel_rental("Nonexistent User", TEST_RENTALS_FILE)
        rentals = load_rentals(TEST_RENTALS_FILE)
        self.assertEqual(len(rentals), 1)

    # Testy dla generate_daily_report
    def test_generate_daily_report(self):
        rental = {"customer_name": "User1", "rental_duration": 2, "cost": 15, "rental_time": "2024-01-01 12:00:00"}
        save_rental(rental, TEST_RENTALS_FILE)

        generate_daily_report(TEST_RENTALS_FILE, TEST_REPORTS_DIR)
        report_files = os.listdir(TEST_REPORTS_DIR)
        self.assertEqual(len(report_files), 1)

        with open(os.path.join(TEST_REPORTS_DIR, report_files[0]), "r") as report_file:
            report_data = json.load(report_file)
        self.assertEqual(len(report_data), 1)
        self.assertEqual(report_data[0]["customer_name"], "User1")


if __name__ == "__main__":
    unittest.main()
