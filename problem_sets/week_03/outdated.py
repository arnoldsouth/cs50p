def main():
    get_date_input()


def get_date_input():
    months_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        date = input("Date: ")
        try:
            if "/" in date:
                month, day, year = date.split("/")
            elif "," in date:
                month, day, year = date.replace(",", "").split(" ")
                if month in months_list:
                    month = months_list.index(month) + 1
            else:
                continue

            month = int(month)
            day = int(day)
            year = int(year)
            if month > 12 or day > 31:
                raise ValueError
        except (ValueError, KeyError):
            continue

        print(f"{year}-{month:02}-{day:02}")
        break


main()
