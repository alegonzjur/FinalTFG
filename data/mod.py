import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from pathlib import Path
data_path = Path("../src")

dataset = Path(data_path / "AnnualCauseDeathNumbers.csv")
data = pd.read_csv(dataset)
data.head()