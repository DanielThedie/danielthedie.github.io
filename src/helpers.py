from datetime import datetime


def format_date(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%d %B %Y")
