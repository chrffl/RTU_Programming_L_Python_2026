"""
Lab 2.1 – Simple Datasets and Aggregates
----------------------------------------
Practice lists, dictionaries and tuples by computing simple aggregates.

Examples (these are also used to check your work):
>>> average([1, 2, 3, 4])
2.5
>>> average([])
0.0
>>> cities = {"Riga": 605000, "Daugavpils": 78000, "Liepaja": 67000}
>>> largest_city(cities)
('Riga', 605000)
>>> smallest_city(cities)
('Liepaja', 67000)
>>> total_population(cities)
750000
>>> largest_city({})
('', 0)
>>> largest_city({"A": 10, "B": 10})
('A', 10)
"""


def average(values: list[float]) -> float:
    """Return the average of values, or 0.0 for an empty list."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def largest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the largest population."""
    if not populations:
        return ("", 0)
    # max() returns the first key on ties, which matches the requirement
    name = max(populations, key=lambda city: populations[city])
    return (name, populations[name])


def smallest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the smallest population."""
    if not populations:
        return ("", 0)
    # min() returns the first key on ties, which matches the requirement
    name = min(populations, key=lambda city: populations[city])
    return (name, populations[name])


def total_population(populations: dict[str, int]) -> int:
    """Return the sum of all populations."""
    return sum(populations.values())


if __name__ == "__main__":
    # Keep all input() and print() calls inside this block, otherwise the
    # autograder cannot import your file.

    temperatures = [3.6, 8, 6.7, 6, 4, 4, 4]
    city_population = {
        "Pavlograd": 100000,
        "Oslo": 607159,
        "Chernivtsi": 260000,
        "Berlin": 3897145,
        "Bergen": 291189,
    }

    avg_temp = average(temperatures)
    big_name, big_pop = largest_city(city_population)
    small_name, small_pop = smallest_city(city_population)
    total = total_population(city_population)

    print(f"Average temperature: {avg_temp:.1f}")
    print(f"Largest city: {big_name} - {big_pop}")
    print(f"Smallest city: {small_name} - {small_pop}")
    print(f"Total population: {total}")
