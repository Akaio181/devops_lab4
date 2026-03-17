import unittest
from payment_strategy import (
    PaymentProcessor,
    CreditCardPayment,
    PayPalPayment,
    CryptoPayment,
    ApplePayPayment,
)


class TestCreditCardPayment(unittest.TestCase):
    def test_pay(self):
        strategy = CreditCardPayment()
        result = strategy.pay(100)
        self.assertEqual(result, "Processing credit card payment of $100")

    def test_pay_different_amount(self):
        strategy = CreditCardPayment()
        self.assertIn("250", strategy.pay(250))


class TestPayPalPayment(unittest.TestCase):
    def test_pay(self):
        strategy = PayPalPayment()
        result = strategy.pay(100)
        self.assertEqual(result, "Processing PayPal payment of $100")


class TestCryptoPayment(unittest.TestCase):
    def test_pay(self):
        strategy = CryptoPayment()
        result = strategy.pay(100)
        self.assertEqual(result, "Processing crypto payment of $100")


class TestApplePayPayment(unittest.TestCase):
    def test_pay(self):
        strategy = ApplePayPayment()
        result = strategy.pay(100)
        self.assertEqual(result, "Processing Apple Pay payment of $100")


class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = PaymentProcessor()

    def test_credit_card_strategy(self):
        self.processor.set_strategy(CreditCardPayment())
        result = self.processor.process_payment(100)
        self.assertEqual(result, "Processing credit card payment of $100")

    def test_paypal_strategy(self):
        self.processor.set_strategy(PayPalPayment())
        result = self.processor.process_payment(100)
        self.assertEqual(result, "Processing PayPal payment of $100")

    def test_crypto_strategy(self):
        self.processor.set_strategy(CryptoPayment())
        result = self.processor.process_payment(100)
        self.assertEqual(result, "Processing crypto payment of $100")

    def test_strategy_switching(self):
        self.processor.set_strategy(CreditCardPayment())
        result1 = self.processor.process_payment(100)

        self.processor.set_strategy(PayPalPayment())
        result2 = self.processor.process_payment(100)

        self.assertNotEqual(result1, result2)
        self.assertIn("credit card", result1)
        self.assertIn("PayPal", result2)

    def test_no_strategy_raises_error(self):
        with self.assertRaises(ValueError):
            self.processor.process_payment(100)

    def test_multiple_switches(self):
        strategies = [
            (CreditCardPayment(), "credit card"),
            (PayPalPayment(), "PayPal"),
            (CryptoPayment(), "crypto"),
            (ApplePayPayment(), "Apple Pay"),
        ]
        for strategy, keyword in strategies:
            self.processor.set_strategy(strategy)
            result = self.processor.process_payment(50)
            self.assertIn(keyword, result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
