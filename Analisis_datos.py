import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
from sklearn.tree import plot_tree
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier

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
print(comparacion1)

# Para ver los porcentajes
porcentajes = comparacion1.div(comparacion1.sum(axis=1), axis=0) * 100
print(porcentajes)

# Agrupamos para saber si el miedo viene del % de tareas que hace la ia
df["grupo_ai"] = pd.cut(x=df["ai_replaces_my_tasks_pct"],bins=[0,20,40,60,80,100],right=True)
pr=pd.crosstab(df["grupo_ai"], df["fear_of_ai_replacement"])
miedo0 = pr.div(pr.sum(axis=1), axis=0) * 100
print(miedo0)

# Verficamos que si la aumento  en la habilidades en uso de ia dismunye el miedo
df["grupo_upskill"] = pd.cut(x=df["weekly_ai_upskilling_hrs"],bins=[0,2,4,6,8,10],right=True)
miedo1=pd.crosstab(df["grupo_upskill"], df["fear_of_ai_replacement"])
miedo_1 = miedo1.div(miedo1.sum(axis=1), axis=0) * 100
print(miedo_1)

# Verficamos que si el miedo aumenta si la satisfaccion del trabajo es baja
df["job_satisfaction_group"] = pd.cut(df["job_satisfaction_1_5"],bins=[1,2,3,4,5,6],labels=[1,2,3,4,5],right=False)
miedo2 = pd.crosstab(df["job_satisfaction_group"],df["fear_of_ai_replacement"],normalize="index") * 100
print(miedo2)

# Verificamos que si el miedo aumenta si la empresa implementa mas la IA
miedo3= pd.crosstab(df["ai_adoption_stage"],df["fear_of_ai_replacement"],normalize="index") * 100
print(miedo3)

# MODELO DE PREDICCIÓN
cols_decimal = [
    "hours_with_ai_assistance_daily",
    "weekly_ai_upskilling_hrs",
    "job_satisfaction_1_5"
]

for col in cols_decimal:
    df[col] = df[col].astype(str).str.replace(",", ".").astype(float)

# =============================
# RANDOM FOREST
# =============================

df_modelo = df.copy()
df_modelo = df_modelo.drop(columns=[
    "employee_id",
    "grupo_ai",
    "grupo_upskill",
    "job_satisfaction_group"
], errors='ignore')

# Variable objetivo
mapeo_y = {"Low": 0, "Medium": 1, "High": 2}
y = df_modelo["fear_of_ai_replacement"].map(mapeo_y)

# TODAS las variables menos la objetivo
x = df_modelo.drop(columns=["fear_of_ai_replacement"])

# Convertir TODAS las categóricas
x = pd.get_dummies(x, drop_first=True)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7, stratify=y)

modelo_rf = RandomForestClassifier(
    n_estimators=100, 
    max_depth=None, 
    min_samples_leaf=3, 
    class_weight="balanced", 
    random_state=42, 
    n_jobs=-1

)

modelo_rf.fit(x_train, y_train)
pred_rf = modelo_rf.predict(x_test)

# Accuracy
accuracy_rf = accuracy_score(y_test, pred_rf)
print("Accuracy Random Forest:", accuracy_rf)

# Matriz de confusión
cm_rf = confusion_matrix(y_test, pred_rf)
print("Matriz de confusión RF:\n", cm_rf)

# Importancia (TOP 10)
importancia = pd.Series(modelo_rf.feature_importances_, index=x.columns)
print("\nTop 10 variables más importantes:")
print(importancia.sort_values(ascending=False).head(10))

sns.set(style="whitegrid")  
# Usando el DataFrame de porcentajes por rol
plt.figure(figsize=(12,6))
sns.heatmap(porcentajes, annot=True, fmt=".1f", cmap="YlOrRd")  # rojo=alto, amarillo=bajo
plt.title("Miedo al reemplazo por IA según rol")
plt.ylabel("Rol")
plt.xlabel("Nivel de miedo")
plt.tight_layout()
plt.show()
plt.close()

#tareas que hace la IA
miedo0.plot(marker="o", figsize=(8,5))
plt.title("Miedo según % de tareas realizadas por IA")
plt.ylabel("Porcentaje (%)")
plt.xlabel("Grupo de tareas IA (%)")
plt.grid(True)
plt.xticks(rotation=0)
plt.legend(title="Nivel de miedo")
plt.tight_layout()
plt.show()
plt.close()

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
plt.show()
plt.close()

# satisfacción laboral
plt.figure(figsize=(6,4))
sns.heatmap(miedo2, annot=True, fmt=".1f", cmap="YlGnBu")  # azul oscuro = alto
plt.title("Miedo según satisfacción laboral")
plt.ylabel("Nivel de satisfacción")
plt.xlabel("Nivel de miedo")
plt.tight_layout()
plt.show()
plt.close()

#adopción de IA en la empresa
plt.figure(figsize=(6,4))
sns.heatmap(miedo3, annot=True, fmt=".1f", cmap="YlOrRd")  # rojo = alto
plt.title("Miedo según etapa de adopción de IA")
plt.ylabel("Etapa de adopción IA")
plt.xlabel("Nivel de miedo")
plt.tight_layout()
plt.show()
plt.close()

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
plt.close()

# Matriz de confusion
#RAMDON FOREST

disp_rf = ConfusionMatrixDisplay(
    confusion_matrix=cm_rf,
    display_labels=["Low", "Medium", "High"]
)

disp_rf.plot(cmap="Greens", values_format="d")
plt.grid(False)
plt.title("Matriz de Confusión - Random Forest")
plt.show()

# ARBOL DE RANDOM FOREST (1)
arbol = modelo_rf.estimators_[0]
plt.figure(figsize=(30,12))
plot_tree(
    arbol,
    feature_names=x.columns,
    class_names=["Low", "Medium", "High"],
    filled=True,
    max_depth=2,
    fontsize=8,
    precision=2   
)
plt.title("Árbol dentro del Random Forest", fontsize=18)
plt.title(f"Árbol dentro del Random Forest\nAccuracy: {accuracy_rf:.4f}",fontsize=18)
plt.tight_layout()
plt.show()
