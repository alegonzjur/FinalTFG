import pandas as pd 
import matplotlib.pyplot as plt  
from pathlib import Path
import warnings 
warnings.filterwarnings('ignore')

#Comienza el modulo identificando el archivo CSV a leer. 
data_path = Path('src')
nombre = input("Introduzca el nombre del archivo csv que quiere leer(Ejemplo_1.csv):  ")
csv = pd.read_csv(data_path / nombre)

#Vemos algunas características del CSV.
def intro():
    print(csv.head())
    print(csv.info())
    print(csv.describe())

def mostrar_indice(csv):
    print("Indices del dataframe",csv,":")
    n_columnas = csv.columns.tolist()
    for c in n_columnas:
        print(c)
#Creamos algunas funciones con Matplotlib. 
def g_barras_2_var():
    mostrar_indice(csv)
    varX = input("Introduzca el nombre de la variable X a dibujar: ")
    varY = input("Introduzca el nombre de la variable Y a dibujar: ")
    plt.plot(varX, varY, label="Contador de accidentes.")
    plt.xlabel("Eje X:")
    plt.ylabel("Eje Y:")
    plt.title("Muertes en carretera:")
    plt.legend()
    plt.grid(True)
    #Mostramos gráfico.
    plt.show()
    #
    #col1 = input("Introduzca el nombre de una columna: ")
    #val1 = input("Introduzca el valor de esa columna: ")
    #col2 = input("Introduzca el nombre de una segunda columna: ")
    #val2 = input("Introduzca el valor de esa segunda columna: ")
    #europa = csv.query('"col1" == "val1" & "col2" == "val2"')
    #print(europa)


def main():
    #intro()
    g_barras_2_var()


main()