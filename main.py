from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine

load_dotenv()


data_path = os.path.join("data", "population.csv")
data_df = pd.read_csv(data_path)


data_query_engine = PandasQueryEngine(df=data_df, verbose=True)



