import re

import pandas as pd

orig_data = pd.read_csv("orig_fk.csv")
count_datasets = len(orig_data) // 3

dfs = [
    pd.DataFrame({
        "temperature": float(re.search(r"(\d*)\s\[C]", orig_data.columns[i + 1])[1]),
        "strain_rate": float(re.search(r"(\d+\.?\d*)\[-]", orig_data.columns[i + 1])[1]),
        "strain": orig_data.iloc[:, i],
        "flow_stress": orig_data.iloc[:, i + 1],
    }).dropna()

    for i in range(0, count_datasets, 2)
]

data = pd.concat(dfs, ignore_index=True)

data.to_csv("bst_fk.csv", index=False)