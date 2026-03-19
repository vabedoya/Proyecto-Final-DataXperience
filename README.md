<!-- PORTADA / BANNER -->
<p align="center">
  <img src="https://i.imgur.com/ueQwQvv.png" alt="AI Impact Banner" width="100%">
</p>

<h1 align="center">📊 Impacto de la Inteligencia Artificial en la Percepción de Reemplazo Laboral</h1>

<p align="center">
  <strong>Un análisis basado en datos, visualizaciones y modelado predictivo sobre el miedo laboral frente a la IA</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Model-Decision%20Tree-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Data%20Science-EDA%20%26%20ML-purple?style=for-the-badge">
</p>

---

# 🎯 Objetivo
Comprender cómo el uso de IA, el nivel de automatización de tareas y las condiciones laborales influyen en la percepción de reemplazo laboral.  
El análisis integra **limpieza de datos, análisis exploratorio, visualizaciones y un modelo predictivo explicable**, permitiendo identificar patrones humanos y organizacionales detrás del miedo laboral.

---

## 👥 Equipo de trabajo
- **Preparación y calidad de datos**  
- **Análisis exploratorio y visualización**  
- **Modelo predictivo, interpretación global y storytelling**

---

## 🧹 Preparación de los datos
Se realizó un proceso estructurado y riguroso de depuración para garantizar un dataset confiable y apto para modelado. Incluyó:

- Identificación y tratamiento de **63 valores nulos**  
- Corrección de valores negativos mediante imputación por mediana  
- Control de outliers mediante **capping**  
- Validación de variables críticas:
  - % de tareas automatizadas ajustado a un máximo realista de 100  
  - Límites coherentes para horas de uso de IA  
- Confirmación de ausencia de duplicados  

El resultado fue un dataset **limpio, consistente y sin valores faltantes**, habilitando un análisis sólido.

---

## 📊 Análisis exploratorio
Se desarrollaron visualizaciones orientadas a entender cómo se distribuye el miedo y qué factores lo influyen:

- Distribución del nivel de percepción de reemplazo por IA  
- Comparación del miedo según **rol laboral**  
- Asociación entre **nivel de automatización** y percepción de riesgo  
- Relación entre **satisfacción laboral** y miedo  
- Efecto del **aprendizaje en IA (upskilling)**  
- Percepción de miedo según **etapa de adopción tecnológica**

### 🔍 Principales hallazgos
- Predomina un **miedo intermedio**, reflejando incertidumbre más que alarma  
- El miedo es **transversal**, incluso en roles tecnológicos y expertos en IA  
- La automatización influye, pero no de forma lineal  
- El aprendizaje ayuda, pero **no elimina la sensación de riesgo**  
- El burnout incrementa la percepción de amenaza laboral  
- La satisfacción laboral actúa como factor protector, pero no absoluto  

---

## 🤖 Modelo predictivo
Se implementó un modelo de **árbol de decisión** para clasificar el nivel de miedo al reemplazo.

### Variables consideradas:
- Nivel de satisfacción laboral  
- Nivel de agotamiento laboral (burnout)  
- Porcentaje de tareas susceptibles de automatización  
- Horas de aprendizaje en IA  
- Horas de uso de herramientas de IA  
- Años de experiencia  

### 📈 Resultados del modelo:
- **Precisión aproximada: 40–42%**  
- Mejor desempeño en categorías **intermedias**  
- Dificultad para clasificar percepciones extremas (bajo o alto)

### 🧠 Interpretación
El modelo confirma que la percepción de reemplazo es un fenómeno **multifactorial**, influenciado tanto por aspectos tecnológicos como por factores emocionales y condiciones laborales.

---

## 💼 Aplicación en contexto profesional
Los resultados permiten ser aplicados en:

- Identificación de niveles de resistencia a la adopción de IA  
- Diseño de programas de **upskilling** y reconversión laboral  
- Estrategias de transformación digital con enfoque humano  
- Gestión del talento basada en analítica  
- Prevención de burnout y reducción de incertidumbre tecnológica  

---

## ⚠️ Limitaciones del estudio
- Relaciones no lineales entre variables  
- Precisión moderada del modelo  
- Falta de variables cualitativas (cultura organizacional, liderazgo)  
- Miedo laboral es una variable subjetiva y difícil de modelar  

---

## 📌 Conclusión
La IA no genera miedo por sí misma.  
El miedo surge por la combinación de **automatización**, **agotamiento**, **incertidumbre** y **sensación de falta de control**.

Los datos muestran que:

- El miedo no es extremo, sino **moderado y persistente**  
- El bienestar laboral influye tanto como la tecnología  
- La adopción de IA requiere acompañamiento, comunicación y formación  

La transformación digital no es solo tecnológica:  
es **humana, emocional y estratégica**.

---

## 🛠️ Tecnologías utilizadas
- Python  
- Pandas, NumPy  
- Scikit‑learn  
- Matplotlib, Seaborn  
- Jupyter Notebook  

---

## 📁 Estructura del proyecto
