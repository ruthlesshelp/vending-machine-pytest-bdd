from data_access_objects import PaymentDao

class PaymentProcessor:
    _data: PaymentDao = None

    def __init__(self):
        self._data = PaymentDao()

    def is_payment_made(self):
        amount = self._data.retrieve()
        return amount > 0

    def make_payment(self, count):
        amount = self._data.retrieve()
        amount = amount + count*25
        self._data.save(amount)

    def reset(self):
        self._data.save(0)

    def payment_amount(self):
        amount = self._data.retrieve()
        return amount