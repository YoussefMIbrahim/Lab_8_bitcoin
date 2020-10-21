import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestBitCoin(TestCase):

    @patch('bitcoin.request_bitcoin_rate')
    def test_convert_bitcoin_value(self, mock_rates):   
        mock_rate = 10000.1234

        example_api_response = {"time":{"updated":"Oct 21, 2020 01:01:00 UTC","updatedISO":"2020-10-21T01:01:00+00:00","updateduk":"Oct 21, 2020 at 02:01 BST"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin","bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"11,996.8817","description":"United States Dollar","rate_float":mock_rate},"GBP":{"code":"GBP","symbol":"&pound;","rate":"9,259.7811","description":"British Pound Sterling","rate_float":9259.7811},"EUR":{"code":"EUR","symbol":"&euro;","rate":"10,141.9478","description":"Euro","rate_float":10141.9478}}}

        mock_rates.side_effect = [example_api_response]

        converted = bitcoin.convert_bitcoin_value(100)
        expected = mock_rate * 100

        self.assertEqual(expected,converted)