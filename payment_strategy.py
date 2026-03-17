from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Processing credit card payment of ${amount}"


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Processing PayPal payment of ${amount}"


class CryptoPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Processing crypto payment of ${amount}"


class ApplePayPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Processing Apple Pay payment of ${amount}"


class PaymentProcessor:
    def __init__(self):
        self._strategy: PaymentStrategy | None = None

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def process_payment(self, amount: float) -> str:
        if self._strategy is None:
            raise ValueError("No payment strategy set")
        return self._strategy.pay(amount)
