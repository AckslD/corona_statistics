import os
import requests
from datetime import date

from data import get_file_cases_path, get_file_path

FILE_LAST_DATE = "data/.last_date"


def update_cases():
    url = ("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/"
           "master/csse_covid_19_data/csse_covid_19_time_series/"
           "time_series_covid19_confirmed_global.csv")
    data = requests.get(url).text

    # Write to file
    filepath = get_file_cases_path()
    with open(filepath, 'w') as f:
        f.write(data)


def update_date():
    filepath = get_file_path(FILE_LAST_DATE)
    with open(filepath, 'w') as f:
        today = str(date.today())
        f.write(today)


def update_all():
    print("updating")
    update_cases()
    update_date()


def need_update():
    filepath = get_file_path(FILE_LAST_DATE)
    if not os.path.exists(filepath):
        return True
    with open(filepath, 'r') as f:
        last_update = date.fromisoformat(f.read().strip())
    return last_update < date.today()


def main(force=False):
    if force:
        update_all()
    else:
        if need_update():
            update_all()


if __name__ == '__main__':
    main()
