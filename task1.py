import heapq


def min_cost_to_connect_cables(cables):
    # Ініціалізуємо мінімальну купу з довжин кабелів.
    heapq.heapify(cables)

    total_cost = 0

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Витрати на з'єднання двох кабелів
        cost = first + second
        total_cost += cost

        # Поміщаємо отриману довжину назад у купу
        heapq.heappush(cables, cost)

    return total_cost


# Testing
cables = [4, 3, 2, 6, 10, 1, 12, 5]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
