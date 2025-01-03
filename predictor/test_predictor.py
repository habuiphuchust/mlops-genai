import unittest
from unittest.mock import MagicMock, patch
import numpy as np
from .utils import predict_expenses

class TestPredictExpenses(unittest.TestCase):
    @patch('joblib.load')
    def test_predict_expenses(self, mock_joblib_load):


        # Gọi hàm predict_expenses
        predicted_expense = predict_expenses(30, "M", 25, 4, "N")

        # Kiểm tra kết quả
        print(predicted_expense)
        self.assertIsInstance(predicted_expense, float)
        #self.assertEqual(predicted_expense, 12345.67)

        # Kiểm tra các mock được gọi đúng
        

if __name__ == '__main__':
    unittest.main()
