import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote['stock'],
                    quote['top_bid']['price'],
                    quote['top_ask']['price'],
                    (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
                )
            )

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote['stock'],
                    quote['top_bid']['price'],
                    quote['top_ask']['price'],
                    (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
                )
            )

    def test_getDataPoint_bidEqualAsk(self):
        quotes = [
            {'top_ask': {'price': 100.0, 'size': 50}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 100.0, 'size': 50}, 'id': '0.109974697771', 'stock': 'XYZ'}
        ]
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote['stock'],
                    quote['top_bid']['price'],
                    quote['top_ask']['price'],
                    (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
                )
            )

    def test_getDataPoint_bidLessThanAsk(self):
        quotes = [
            {'top_ask': {'price': 110.0, 'size': 30}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 105.0, 'size': 60}, 'id': '0.109974697771', 'stock': 'LMN'}
        ]
        for quote in quotes:
            self.assertEqual(
                getDataPoint(quote),
                (
                    quote['stock'],
                    quote['top_bid']['price'],
                    quote['top_ask']['price'],
                    (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
                )
            )

    def test_getRatio(self):
        self.assertEqual(getRatio(10, 2), 5)
        self.assertEqual(getRatio(10, 1), 10)
        self.assertEqual(getRatio(0, 10), 0)
        self.assertEqual(getRatio(10, 0), None)  # Division by zero case
        self.assertEqual(getRatio(0, 0), None)  # Both are zero

    def test_getRatio_withNegativeValues(self):
        self.assertEqual(getRatio(-10, 2), -5)
        self.assertEqual(getRatio(10, -2), -5)
        self.assertEqual(getRatio(-10, -2), 5)
        self.assertEqual(getRatio(-10, 0), None)  # Division by zero case

if __name__ == '__main__':
    unittest.main()
