# reservation.py
class ReservationSystem:
    def __init__(self):
        self.reservations = {}

    def reserve_table(self, table_number, customer_name):
        if table_number in self.reservations:
            return "Table already reserved"
        self.reservations[table_number] = customer_name
        return f"Table {table_number} reserved for {customer_name}"

    def cancel_reservation(self, table_number):
        if table_number in self.reservations:
            customer_name = self.reservations.pop(table_number)
            return f"Reservation for {customer_name} at table {table_number} canceled"
        return "Reservation not found"
