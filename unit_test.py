import unittest
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from zenq.api.tables import Facts 
from zenq.clvmodels.pareto import Model
from zenq.api.config import db_uri
from unittest.mock import MagicMock
from zenq.api.prepare_db import db


class TestMLSystem(unittest.TestCase):
    def test_main(self):
        # db_uri = 'sqlite:///test.db'
        # engine = create_engine(db_uri)
        mydb = db()
        mydb.main()
        self.assertIsNotNone(metadata)
        self.assertIsNotNone(engine)
        # self.assertTrue(engine.dialect.has_table(engine.connect(), 'Facts'))
    def setUp(self):
        self.engine = create_engine(db_uri)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        m=db()
        m.main()
        self.facts_data = {'customer_id_uniq': [1, 2, 3, 4, 5], 'location_id': [1, 2, 3, 4, 5], 'location_name': ['NY', 'CA', 'TX', 'IL', 'NY'], 'invoice_id': [100222, 100333, 100444, 100555, 100666], 'date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'], 'quantity': [2, 1, 3, 1, 2], 'total_price': [100, 50, 150, 75, 100]}
        self.facts_df = pd.DataFrame.from_dict(self.facts_data)

    def test_create_facts_table(self):
        self.assertTrue(Facts.__table__.exists(self.engine))
        print("Test create facts table passed.")
        
    def test_insert_facts(self):
        # Mock the data_prep class to return the facts_df DataFrame
        data_prep_mock = MagicMock(return_value=self.facts_df)
        insert_facts.__globals__['data_prep'] = data_prep_mock

        # Call the insert_facts function with the facts_data dictionary
        insert_facts('test.csv', 'customer_id_uniq', 'location_name', 'invoice_id', 'date', 'quantity', 'total_price')

        # Assert that the facts have been added to the database
        expected_facts = [(1, 'NY', 1001, '2022-01-01', 2, 100),
                          (1, 'NY', 1002, '2022-01-02', 1, 50),
                          (2, 'CA', 1003, '2022-01-03', 3, 150),
                          (3, 'TX', 1004, '2022-01-04', 1, 75),
                          (4, 'IL', 1005, '2022-01-05', 2, 100),
                          (5, 'NY', 1006, '2022-01-06', 1, 50)]
        actual_facts = self.session.query(Facts.customer_id, Facts.location_name, Facts.invoice_id,
                                           Facts.date, Facts.quantity, Facts.total_price).all()
        self.assertEqual(expected_facts, actual_facts)

 