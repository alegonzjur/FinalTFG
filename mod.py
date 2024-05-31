import pandas as pd
import matplotlib.pyplot as plt 
from pathlib import Path
data_path = Path("../FinalTFG/src")

#Ruta del archivo
archivo_csv = "FinalTFG\src\phising.csv"
#Carga de datos
data = pd.read_csv(archivo_csv)

#Vemos el índice. 
def intro():
    print(data.head())
    print(data.info())
    print(data.describe())
    
def main():
    intro()


main()