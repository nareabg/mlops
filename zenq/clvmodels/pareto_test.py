import pandas as pd
import numpy as np
from .pareto import Model
from lifetimes import BetaGeoFitter, ParetoNBDFitter
import unittest
from unittest.mock import Mock, patch
 
class TestModel(unittest.TestCase):
    
    # Unit test for cltv_df() method
    @patch('zenq.clvmodels.pareto.Model.session')
    def test_cltv_df(self, mock_session):
        # create mock data for query results
        query_results = [(1, '2022-01-01', 10, 20, 5, 100), 
                         (2, '2022-02-01', 5, 15, 3, 75)]
        # set up the mock session to return the mock query results
        mock_session.query().group_by().having().all.return_value = query_results
        # create an instance of Model
        model = Model()
        # call the method cltv_df()
        result = model.cltv_df()
        # check that the output is correct
        expected_result = pd.DataFrame({
            'customer_id': [1, 2],
            'min_date': ['2022-01-01', '2022-02-01'],
            'recency': [10, 5],
            'T': [20, 15],
            'frequency': [5, 3],
            'monetary': [100, 75]
        })
        pd.testing.assert_frame_equal(result, expected_result)
    
    # Integration test for rfm_score() method
    @patch('zenq.clvmodels.pareto.Model.cltv_df')
    def test_rfm_score(self, mock_cltv_df):
        # create mock data for cltv_df() method output
        cltv_df_results = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'recency': [10, 20, 30],
            'frequency': [5, 3, 1],
            'monetary': [100, 50, 25]
        })
        mock_cltv_df.return_value = cltv_df_results
        # create an instance of Model
        model = Model()
        # call the method rfm_score()
        result = model.rfm_score()
        # check that the output is correct
        expected_result = pd.DataFrame({
            'customer_id': [1, 2, 3],
            'recency_score': [3, 1, 1],
            'frequency_score': [5, 3, 1],
            'monetary_score': [5, 3, 1],
            'rfm_score': [13, 7, 3]
        })
        pd.testing.assert_frame_equal(result, expected_result)

if __name__ == '__main__':
    unittest.main()
