import csv
import uuid
from typing import Any
from urllib.parse import urljoin


def convert_time(time: str, ampm: str) -> str:
    if ampm == "AM":
        return time
    else:
        time_list = time.split(":")
        hour = time_list.pop(0)
        hour = int(hour) + 12
        if hour == 24:
            hour = 0
        time_list.insert(0, str(hour))
        return ":".join(time_list)


def convert_table(transactions_table: str) -> list[dict[str, Any]]:
    transactions_table = transactions_table.split("\n")
    new_transactions_table = []
    for transaction in transactions_table:
        transaction_dict = {}
        transaction = transaction.replace(",", "").split(" ")
        transaction_dict[
            "datetime"
        ] = f"{transaction[1]} {transaction[0]} {transaction[2]} {convert_time(transaction[3], transaction[4])}"
        transaction_dict["amount"] = transaction[5]
        transaction_dict["transaction_type"] = transaction[6]
        new_transactions_table.append(transaction_dict)
    return new_transactions_table


def create_transactions_file(table_dict_data: list[dict[str, Any]]) -> str:
    name = f"transaction_{uuid.uuid4()}.csv"
    path = urljoin("transaction_files/", name)
    with open(path, "w", newline="") as csvfile:
        fieldnames = table_dict_data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(table_dict_data)
    return path
