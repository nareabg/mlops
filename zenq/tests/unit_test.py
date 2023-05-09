# import unittest
# import pandas as pd
# from sqlalchemy import create_engine, inspect
# from sqlalchemy.orm import sessionmaker
# from zenq.api.tables import Facts 
# from zenq.clvmodels.pareto import Model
# from zenq.api.config import db_uri
# from unittest.mock import MagicMock
# from zenq.api.prepare_db import db
# from tempfile import NamedTemporaryFile
# import csv
# import datetime
# import os
# from zenq.api.endpoints import insert_facts


# class TestMLSystem(unittest.TestCase):
#     Facts = Facts()
#     model = Model()
#     metadata, engine = Facts.connect_to_db(db_uri)
    
#     session = sessionmaker(bind=engine)()
#     def test_main(self):
#         mydb = db()
#         mydb.main()
#         self.assertIsNotNone(self.metadata)
#         self.assertIsNotNone(self.engine)
            
#     def test_insert_facts(self):
#         # Create a temporary file with the test data
#         with NamedTemporaryFile(mode='w', delete=False) as f:
#             writer = csv.writer(f)
#             writer.writerow(['customer_id','gender', 'invoice_id', 'date', 'quantity', 'total_price'])
#             writer.writerow([1, 'F', 100222, '2022-01-01', 2, 100])
#             writer.writerow([2, 'M', 100333, '2022-01-02', 1, 50])
#             writer.writerow([3,'M',  100444, '2022-01-03', 3, 150])
#             writer.writerow([5, 'M', 100555, '2022-01-04', 1, 75])
#             writer.writerow([5, 'M', 100666, '2022-01-05', 2, 100])
#             writer.writerow([5, 'M', 100777, '2022-01-07', 1, 75])

        
#         # Call the insert_facts function with the test data
#         insert_facts(f.name,'customer_id', 'gender', 'invoice_id', 'date', 'quantity', 'total_price')
#         result = self.session.query(Facts).all()
#         assert len(result) == 6
#         # Check that the data was inserted into the database
        
#         first_fact = result[0]
#         assert first_fact.customer_id =='1'
#         assert first_fact.gender == 'F'
#         assert first_fact.invoice_id == '100222'
#         os.remove(f.name)
#         # session.query(Facts).delete()
#         self.session.commit()
    
#     def test_cltv_df(self):
#         cltv = self.model.cltv_df()
#         self.assertEqual(cltv.shape, (1, 6))
#         print(cltv)
#         predict = self.model.predict_paretonbd()
#         print(predict)

import pandas as pd
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from zenq.api.tables import Facts 
from zenq.clvmodels.pareto import Model
from zenq.api.config import db_uri
from unittest.mock import MagicMock
from zenq.api.prepare_db import db
from tempfile import NamedTemporaryFile
import csv
import datetime
import pytest
import os
from zenq.api.endpoints import insert_facts
facts=Facts() 
metadata, engine = facts.connect_to_db(db_uri)

session = sessionmaker(bind=engine)()

@pytest.mark.db
def test_main():
    mydb = db()
    mydb.main()
    assert metadata is not None
    assert engine is not None
        
@pytest.mark.clv
def test_insert_facts():
    # Create a temporary file with the test data
    with NamedTemporaryFile(mode='w', delete=False) as f:
        writer = csv.writer(f)
        writer.writerow(['customer_id','gender', 'invoice_id', 'date', 'quantity', 'total_price'])
        writer.writerow([1, 'F', 100222, '2022-01-01', 2, 100])
        writer.writerow([2, 'M', 100333, '2022-01-02', 1, 50])
        writer.writerow([3,'M',  100444, '2022-01-03', 3, 150])
        writer.writerow([5, 'M', 100555, '2022-01-04', 1, 75])
        writer.writerow([5, 'M', 100666, '2022-01-05', 2, 100])
        writer.writerow([5, 'M', 100777, '2022-01-07', 1, 75])

    # Call the insert_facts function with the test data
    insert_facts(f.name,'customer_id', 'gender', 'invoice_id', 'date', 'quantity', 'total_price')
    # session.commit()
    result = session.query(Facts).all()
    assert len(result) == 6
    # Check that the data was inserted into the database
    
    first_fact = result[0]
    assert first_fact.customer_id =='1'
    assert first_fact.gender == 'F'
    assert first_fact.invoice_id == '100222'
    os.remove(f.name)
    # # session.query(Facts).delete()
    session.commit()

@pytest.mark.model
def test_cltv_df():
    model = Model()
    cltv = model.cltv_df()
    assert cltv.shape == (1, 6)

