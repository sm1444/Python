import pandas as pd
import numpy as np

dict={'First score':[100, 90, np.nan, 95],'Second Score': [30, 45, 56, np.nan],'Third Score':[np.nan, 40, 80, 98]}
df = pd.DataFrame(dict)

#df = df.isnull()
#df = df.fillna(0)
df = df.dropna()
print(df)