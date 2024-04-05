PAYMENT_TABLE = 'payments'

class PaymentDao:
    payment: int = 0

    def __init__(self, initial_value: int = 0):
        self.payment = initial_value

    def retrieve(self) -> int:
        print(f'Calling PaymentDao.retrieve() {self.payment}')
        return self.payment

    def save(self, payment: int) -> None:
        print(f'Calling PaymentDao.save() {self.payment}')
        self.payment = payment
