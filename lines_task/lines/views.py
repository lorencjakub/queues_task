import json
from django.shortcuts import render, redirect
from django.contrib import messages
import random
import datetime
from pathlib import Path
from typing import Union

BASE_DIR = str(Path(__file__).resolve().parent.parent)


def time_tracker() -> str:
    return "\n" + datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S") + "    "


def log_watcher(message: str, log_action: str, init: bool = False) -> None:
    with open(BASE_DIR + "/log.txt", log_action, encoding="utf-8") as log:
        if init:
            log.write(str(message))

        else:
            log.write(str(time_tracker() + message))


def home(request):
    maximum_customers_at_start = 5
    customers_in_lines = [random.randint(1, maximum_customers_at_start) for _ in range(3)]
    customers = {f"line_{i + 1}": [random.randint(1, 999) for _ in range(customers_in_lines[i])]
                 for i in range(len(customers_in_lines))}

    message = ""

    for index, cust in enumerate(list(customers.values())):
        message += time_tracker() + f'Fronta č. {str(index + 1)}: {",".join([str(c) for c in cust])}'

    log_watcher(message=message, log_action="w", init=True)

    return render(request, "lines/homepage.html", customers)


def move_customers(request):
    if request.method != "POST":
        return redirect("/")

    elif "add_customer" in request.POST:
        new_customer = random.randint(1, 999)
        lines = {line: json.loads(dict(request.POST)[line][0]) for line in dict(request.POST).keys() if "line_" in line}
        lines["line_1"].append(new_customer)

        message = f"Přišel nový čekatel - {new_customer}."
        log_watcher(message=message, log_action="a")
        messages.success(request, message)
        return render(request, "lines/homepage.html", lines)

    else:
        lines = {line: json.loads(dict(request.POST)[line][0]) for line in dict(request.POST).keys() if "line_" in line}
        line_to_escape = int(request.POST.get("move_from").split("/")[0])
        customers_in_this_line = lines[f"line_{str(line_to_escape)}"]

        if len(customers_in_this_line) > 0:

            message = f"Čekatel {customers_in_this_line[0]} se přesunuje z fronty č. {line_to_escape}."
            log_watcher(message=message, log_action="a")

            if line_to_escape < len(lines.keys()):
                customers_in_next_line = lines[f"line_{str(line_to_escape + 1)}"]

                if len(customers_in_this_line) > 0:
                    customers_in_next_line.append(customers_in_this_line[0])

            else:
                message = f"Čekatel {customers_in_this_line[0]} byl odbaven."
                log_watcher(message=message, log_action="a")
                messages.success(request, message)

            lines[f"line_{line_to_escape}"] = lines[f"line_{line_to_escape}"][1:]

            return render(request, "lines/homepage.html", lines)

        message = f"Fronta č. {line_to_escape} už je prázdná!"
        log_watcher(message=message, log_action="a")
        messages.warning(request, message)
        return render(request, "lines/homepage.html", lines)


def restart_lines(request):
    return redirect("/")
