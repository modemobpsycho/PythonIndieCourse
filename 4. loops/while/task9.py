a, b = map(int, input().split())
hour = 0
burn = 0
while a > 0:
    a -= 1        # Горит одна свеча
    hour += 1     # Прибавляем 1 час
    burn += 1     # Добавляем в запас 1 сгоревшую свечу
    if burn % b == 0:  # Если нам хватает запаса сгоревших свечей
        a += 1    # Создаем 1 новую свечу
        burn = 0  # Обнуляем наш запас сгоревших свечей
print(hour)
