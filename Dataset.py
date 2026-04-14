import pandas as pd
import numpy as np

# Semilla para reproducibilidad
np.random.seed(42)

n = 2000
customer_id = np.arange(1001, 1001 + n)
age = np.random.randint(18, 75, n)
gender = np.random.choice(['M', 'F'], n)

# Estado activo (0 = No, 1 = Sí)
is_active = np.random.choice([0, 1], n, p=[0.4, 0.6])

# Quejas: clientes inactivos tienden a tener más quejas
complaints = np.random.poisson(lam=0.5, size=n)
complaints[is_active == 0] += np.random.randint(0, 3, sum(is_active == 0))
complaints = np.clip(complaints, 0, 10)

# Antigüedad en meses
tenure_months = np.random.randint(1, 120, n)

# Salario estimado: correlacionado con la edad y un factor aleatorio
estimated_salary = age * 1200 + np.random.randint(-10000, 25000, n)
estimated_salary = np.clip(estimated_salary, 12000, 150000)

# Balance: correlacionado con el salario
balance = estimated_salary * np.random.uniform(0.05, 0.4, n)
balance = np.round(balance, 0).astype(int)

# Score de crédito: mejor con mayor salario, peor con más quejas
credit_score = 650 + (estimated_salary / 1500) - (complaints * 15) + np.random.randint(-40, 50, n)
credit_score = np.clip(credit_score, 300, 850).astype(int)

# Número de productos
products = np.random.choice([1, 2, 3, 4], n, p=[0.5, 0.35, 0.1, 0.05])

# Transacciones el último mes: más altas si está activo
transactions_last_month = (is_active * np.random.randint(15, 80, n)) + ((1 - is_active) * np.random.randint(0, 15, n))

# Churn (Abandono): lógica de probabilidad basada en las variables
churn_prob = np.zeros(n)
churn_prob += complaints * 0.25 # Más quejas = más probabilidad de irse
churn_prob += (1 - is_active) * 0.3 # Inactivos = más probabilidad
churn_prob += (credit_score < 550) * 0.2 # Mal crédito = más probabilidad
churn_prob -= (balance > 30000) * 0.1 # Alto balance = menos probabilidad
churn_prob = np.clip(churn_prob, 0, 1)

churn = np.random.binomial(1, churn_prob)

# Creación del DataFrame
df = pd.DataFrame({
    'customer_id': customer_id,
    'age': age,
    'gender': gender,
    'tenure_months': tenure_months,
    'balance': balance,
    'products': products,
    'credit_score': credit_score,
    'is_active': is_active,
    'estimated_salary': estimated_salary,
    'transactions_last_month': transactions_last_month,
    'complaints': complaints,
    'churn': churn
})

# Exportar a CSV
df.to_csv('dataset_2000_customers.csv', index=False)