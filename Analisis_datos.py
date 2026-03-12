import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler

df = pd.read_excel('Dataset_Limpio.xlsx')

# ANALISIS ESTADISTICO
variables = [
"years_experience",
"ai_replaces_my_tasks_pct",
"hours_with_ai_assistance_daily",
"weekly_ai_upskilling_hrs",
"burnout_score",
"job_satisfaction_1_5"
]

print(df[variables].describe())
print(df[variables].std())
print(df[variables].var())

# Para comparar el rol con el nivel del miedo
comparacion1=pd.crosstab(df["job_role"],df["fear_of_ai_replacement"])
#print(comparacion1)

# Para ver los porcentajes
porcentajes = comparacion1.div(comparacion1.sum(axis=1), axis=0) * 100
#print(porcentajes)

# Agrupamos para saber si el miedo viene del % de tareas que hace la ia
df["grupo_ai"] = pd.cut(x=df["ai_replaces_my_tasks_pct"],bins=[0,20,40,60,80,100],right=True)
pr=pd.crosstab(df["grupo_ai"], df["fear_of_ai_replacement"])
miedo0 = pr.div(pr.sum(axis=1), axis=0) * 100
#print(miedo0)

# Verficamos que si la aumento  en la habilidades en uso de ia dismunye el miedo
df["grupo_upskill"] = pd.cut(x=df["weekly_ai_upskilling_hrs"],bins=[0,2,4,6,8,10],right=True)
miedo1=pd.crosstab(df["grupo_upskill"], df["fear_of_ai_replacement"])
miedo_1 = miedo1.div(miedo1.sum(axis=1), axis=0) * 100
#print(miedo_1)

# Verficamos que si el miedo aumenta si la satisfaccion del trabajo es baja
df["job_satisfaction_group"] = pd.cut(df["job_satisfaction_1_5"],bins=[1,2,3,4,5,6],labels=[1,2,3,4,5],right=False)
miedo2 = pd.crosstab(df["job_satisfaction_group"],df["fear_of_ai_replacement"],normalize="index") * 100
print(miedo2)

# Verificamos que si el miedo aumenta si la empresa implementa mas la IA
#miedo4=pd.crosstab(df["ai_adoption_stage"], df["fear_of_ai_replacement"])
miedo3= pd.crosstab(df["ai_adoption_stage"],df["fear_of_ai_replacement"],normalize="index") * 100
#print(miedo3)

# Para realizar el modelo predictivo simple Arbol de decision
y = df["fear_of_ai_replacement"]
x = df [[
   "years_experience",
   "ai_replaces_my_tasks_pct",
   "hours_with_ai_assistance_daily",
   "weekly_ai_upskilling_hrs",
   "burnout_score",
   "job_satisfaction_1_5",
]]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

modelo = DecisionTreeClassifier(max_depth=3)
modelo.fit(x_train, y_train)
predicciones = modelo.predict(x_test)
accuracy = accuracy_score(y_test, predicciones)
#print("Accuracy del modelo:", accuracy)
importancia = pd.Series(modelo.feature_importances_, index=x.columns)
#print(importancia.sort_values(ascending=False))


sns.set(style="whitegrid")  
# Usando el DataFrame de porcentajes por rol
plt.figure(figsize=(12,6))
sns.heatmap(porcentajes, annot=True, fmt=".1f", cmap="YlOrRd")  # rojo=alto, amarillo=bajo
plt.title("Miedo al reemplazo por IA según rol")
plt.ylabel("Rol")
plt.xlabel("Nivel de miedo")
plt.tight_layout()


#tareas que hace la IA
miedo0.plot(marker="o", figsize=(8,5))
plt.title("Miedo según % de tareas realizadas por IA")
plt.ylabel("Porcentaje (%)")
plt.xlabel("Grupo de tareas IA (%)")
plt.grid(True)
plt.xticks(rotation=0)
plt.legend(title="Nivel de miedo")
plt.tight_layout()


# horas de upskilling
miedo_1.plot(marker="o", figsize=(8,5))
plt.title("Miedo según horas semanales de aprendizaje en IA")
plt.ylabel("Porcentaje (%)")
plt.xlabel("Horas de upskilling")
plt.grid(True)
plt.xticks(rotation=0)
plt.legend(title="Nivel de miedo")
plt.legend(title="Nivel de miedo", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()


# satisfacción laboral
plt.figure(figsize=(6,4))
sns.heatmap(miedo2, annot=True, fmt=".1f", cmap="YlGnBu")  # azul oscuro = alto
plt.title("Miedo según satisfacción laboral")
plt.ylabel("Nivel de satisfacción")
plt.xlabel("Nivel de miedo")
plt.tight_layout()


#adopción de IA en la empresa
plt.figure(figsize=(6,4))
sns.heatmap(miedo3, annot=True, fmt=".1f", cmap="YlOrRd")  # rojo = alto
plt.title("Miedo según etapa de adopción de IA")
plt.ylabel("Etapa de adopción IA")
plt.xlabel("Nivel de miedo")
plt.tight_layout()


# PARA MOSTRAR EL ARBOL DE DESICION
plt.figure(figsize=(20,10)) 
tree.plot_tree(
    modelo,
    feature_names=x.columns,
    class_names=modelo.classes_,
    filled=True,
    rounded=True,
    fontsize=12,
    precision=2
)
plt.title(f"Árbol de decisión (Accuracy: {accuracy:.2f})", fontsize=16, pad=20)
#plt.show()

# GRAFICA PARA EL ANALISIIS DE LA MEDIA Y ESO JAJA
# Normalizar datos
# Nombres más claros para el gráfico
nombres = [
"Años\nexperiencia",
"% tareas\nIA",
"Horas IA\npor día",
"Aprendizaje\nIA",
"Nivel\nBurnout",
"Satisfacción\nlaboral"
]

# Normalizar datos (escala 0 a 1)
scaler = MinMaxScaler()
df_normalizado = pd.DataFrame(
    scaler.fit_transform(df[variables]),
    columns=variables
)

# Boxplot
plt.figure(figsize=(10,6))
df_normalizado.boxplot()

plt.xticks(range(1, len(nombres)+1), nombres)

plt.title("Distribución comparativa de variables laborales y uso de IA")
plt.ylabel("Escala normalizada (0 – 1)")

plt.tight_layout()
plt.show()
