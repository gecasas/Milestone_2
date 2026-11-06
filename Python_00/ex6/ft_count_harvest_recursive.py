def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursive_auxiliar(days)
    print("Harvest time!")


def recursive_auxiliar(days):
    if (days > 1):
        recursive_auxiliar(days - 1)
    print("Day", days)
