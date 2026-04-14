# Churn en Fintech

### Contexto
Una fintech mexicana esta perdiendo clientes activos en su app. 
El problema: *no saben exactamente por que los usuarios abandonan el servicio (churn)*

### Objetivo
```
Identificar los factores clave del churn y proponer una estrategia accionable para reducirlo.

1. Predecir qué clientes tienen alta probabilidad de churn
2. Encontrar insights accionables (NO solo correlaciones)
3. Proponer soluciones de negocio claras

```

### Roles y responsabilidades

## Data Engineer (NAT)
```
Responsabilidades:

Limpieza de datos
Manejo de valores faltantes (simulen algunos)
Feature engineering:
churn_rate por segmento
ratio balance/ingresos
engagement score (ej: transacciones + actividad)

Entregables:

Dataset limpio
Pipeline reproducible (idealmente en notebooks o scripts)
```

## Data Scientist (Alfonso)
```
Responsabilidades:

EDA (exploratory data analysis)
Encontrar insights:
¿los usuarios con menos actividad churnean más?
¿las quejas afectan?
¿el balance importa?

Visualizaciones clave:

churn vs transacciones
churn vs complaints
churn vs tenure

Entregables:

3–5 insights claros
gráficos bien explicados (no solo bonitos)
```

## Machine Learning Engineer (Lauro)

```
Responsabilidades:

Modelo de clasificación (churn: 0/1)

Modelos sugeridos:

Logistic Regression
Random Forest
XGBoost (si quieres ir pro)

Métricas:

Accuracy
Precision / Recall
ROC-AUC

Extras (para ganar):

Feature importance
Interpretabilidad (SHAP si puedes)

Entregables:

Modelo entrenado
explicación de qué variables importan más
```

## Storyteller (Regi)
```
Responsabilidades:

Convertir datos en historia de negocio

Estructura:

Problema
Hallazgos clave
Impacto en negocio
Recomendaciones accionables

Ejemplo de insight bien contado:

“Clientes con menos de 10 transacciones mensuales tienen 4x más probabilidad de churn.”

NO hacer:

leer gráficas sin contexto
usar tecnicismos sin traducir

Entregable:

Pitch de 5–7 minutos
```
