from payments import PaymentProcessor

class VendingMachine:
    def __init__(self):
        self.payment_processor = PaymentProcessor()
        self.message = 'Please insert money'
        self.coin_return = 0
        self.dispensed_product = False

    def release_change(self):
        if self.payment_processor.is_payment_made():
            amount = self.payment_processor.payment_amount()
            self.coin_return = amount
            self.payment_processor.reset()
            return 1
        else:
            return 0

    def insert_coin(self, count):
        self.payment_processor.make_payment(count)
        amount = float(self.payment_processor.payment_amount()) / 100.0
        self.message = "You have inserted $%s" % amount

    def buy_product(self):
        if self.payment_processor.is_payment_made():
            self.dispensed_product = True
            self.message = 'Enjoy!'
            amount = self.payment_processor.payment_amount()
            if amount > 50:
                self.coin_return = amount - 50
            else:
                self.coin_return = 0
            self.payment_processor.reset()
            return 'product'
        else:
            return None

    def get_product(self):
        if self.dispensed_product:
            self.dispensed_product = False
            return True
        else:
            return False

    def get_message(self):
        return self.message

    def get_coin_return(self):
        coin_return = self.coin_return
        self.coin_return = 0
        return coin_return

    def get_payment(self):
        payment_amount = self.payment_processor.payment_amount()
        return payment_amount

    def reset(self):
        self.payment_processor.reset()