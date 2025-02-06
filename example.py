import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Исходные данные (пример)
np.random.seed(42)
original_sample = np.random.normal(loc=50, scale=10, size=100)  # 100 элементов из нормального распределения

# Количество бутстраповских выборок
num_bootstrap_samples = 1000

# Создание бутстраповских выборок с пуассоновским весом
bootstrap_means = []

for _ in range(num_bootstrap_samples):
    weights = np.random.poisson(lam=1, size=len(original_sample))  # Пуассоновские веса
    bootstrap_sample = np.repeat(original_sample, weights)  # Дублирование элементов
    if len(bootstrap_sample) > 0:  # Исключаем пустые выборки
        bootstrap_means.append(np.mean(bootstrap_sample))

# Визуализация распределения средних значений бутстраповских выборок
plt.figure(figsize=(8, 5))
plt.hist(bootstrap_means, bins=30, edgecolor='black', alpha=0.7)
plt.axvline(np.mean(original_sample), color='red', linestyle='dashed', label="Исходное среднее")
plt.xlabel("Среднее значение в бутстраповских выборках")
plt.ylabel("Частота")
plt.title("Распределение средних значений (Пуассоновский бутстрап)")
plt.legend()
plt.savefig("plot.png")
