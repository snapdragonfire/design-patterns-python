class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} via Credit Card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} via PayPal")


class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def perform_payment(self, amount):
        self.payment_strategy.pay(amount)


cc_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

payment_context = PaymentContext(cc_payment)
payment_context.perform_payment(100)

payment_context.payment_strategy = paypal_payment
payment_context.perform_payment(50)
