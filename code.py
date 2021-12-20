
import os
os.getcwd()

import pandas as pd
import json
df = pd.read_json("product (1).json")

with open ("product (1).json",'r', encoding="utf8") as f:
    x = json.loads(f.read())

pd.DataFrame.from_dict(x[0]).to_csv('Test.csv',index=False)

x[0].keys()
