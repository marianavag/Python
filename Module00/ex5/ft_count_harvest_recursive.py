def ft_count_harvest_recursive():
    def ft_days(current, last):
        if current > last:
            return
        print(f"Day {current}")
        ft_days(current + 1, last)
    days = int(input("Days until harvest: "))
    ft_days(1, days)
    print("Harvest time!")
