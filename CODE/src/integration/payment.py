# payment.py
class PaymentSystem:
    def __init__(self):
        self.transactions = {}

    def process_payment(self, transaction_id, amount):
        self.transactions[transaction_id] = amount
        return f"Payment of ${amount} processed"

    def refund_payment(self, transaction_id):
        if transaction_id in self.transactions:
            amount = self.transactions.pop(transaction_id)
            return f"Refund of ${amount} processed"
        return "Transaction not found"
