import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("Avances del Proyecto DataXperience.xlsx", 
                   sheet_name="1. Data Research & Cleaning (Ex")
print(df.info())

print("\nvalores nulos:")
print(df.isnull().sum())

print("\nduplicados:")
print(df.duplicated().sum())

print("\ndistribución para variable que responde a la pregunta de investigación:")
print(df["fear_of_ai_replacement"].value_counts())#nos indica cual categoria de la variable tiene mas indicadores 

# Encontrar outliers por metodo del rango intercuartilico:
Q1 = df['ai_replaces_my_tasks_pct'].quantile(0.25)
Q3 = df['ai_replaces_my_tasks_pct'].quantile(0.75)
IQR = Q3 - Q1

# se define el limite
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

# Hallar outliers
outliers = df[(df['ai_replaces_my_tasks_pct'] < limite_inferior) | (df['ai_replaces_my_tasks_pct'] > limite_superior)]
print(f"SE MUESTRAN OUTLIERS\n{outliers}")

# Mostrar outliers
sns.boxplot(x=df['ai_replaces_my_tasks_pct'])

#Identificamos todas las columnas numericas 
colum_num = df.select_dtypes(include=[np.number]).columns 


#Tratamiento de valores nulos en todas las columanas numericas aplicando mediana
df[colum_num] = df[colum_num].fillna(df[colum_num].median())

print("\n PROCESO COMPLETADO VALORES NULOS  ")
print(f"Columnas procesadas: {list(colum_num)}")
print("Nulos restantes en estas columnas:")
print(df[colum_num].isnull().sum())


df_num = df.select_dtypes(include=[np.number])
#valores negativos
negativos = df_num[df_num < 0].dropna(how='all', axis=0).dropna(how='all', axis=1)#se usa dropna para que solo se muestren los valores negativos 
print(f"\nResumen de valores negativos detectados:\n{negativos}")
plt.show()

#Tratamiento de valores negativos, imputamos con la mediana para no sesgar datos hacia abajo
mediana = df['team_size'].median()
df.loc[df['team_size'] < 0, 'team_size'] = mediana

#Tratamiento de outliers en TODAS las columnas numericas 
for col in colum_num:#Usamos for para iterar sobre cada columna numerica
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    limite_superior = Q3 + 1.5 * IQR

    limite_redondeado = round(limite_superior)#redondeamos el limite superior para que sea un numero entero y tenga mas sentido en el contexto de las variables
    df.loc[df[col] > limite_superior, col] = limite_redondeado

df['ai_replaces_my_tasks_pct'] = df['ai_replaces_my_tasks_pct'].clip(upper=100)#se asigna un tope maximo de 100% para esta variable ya que no tiene sentido que supere ese valor
df['hours_with_ai_assistance_daily'] = df['hours_with_ai_assistance_daily'].clip(upper=24)

sns.boxplot(x=df["ai_replaces_my_tasks_pct"])
plt.title("Variable principal despues del CAPPING global")
plt.show()

print("\n                                         ---VERIFICACIÓN DE TOPES---")
print(f"Valor máximo de ai_replaces_my_tasks_pct: {df['ai_replaces_my_tasks_pct'].max()}")
print(f"Valor máximo de hours_with_ai_assistance_daily: {df['hours_with_ai_assistance_daily'].max()}")


print("\n                                         ---RESUMEN ESTADISTICO---")
print(df.describe())



#Guardar el archivo ya limpio:
archivo_limpio = "Dataset_Limpio.xlsx"
df.to_excel(archivo_limpio, index=False)





