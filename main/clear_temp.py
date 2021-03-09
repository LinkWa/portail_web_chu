import os
from datetime import timedelta

from prefect import task, Flow
from prefect.schedules import Schedule
from prefect.schedules.clocks import IntervalClock


@task
def clear_temp(repertoire):
    files = os.listdir(repertoire)
    for i in range(0, len(files)):
        os.remove(repertoire + '/' + files[i])


wait = Schedule(
    clocks=[IntervalClock(timedelta(hours=2))],
)

with Flow("clear_temp", schedule=wait) as flow:
    c = clear_temp("tempPDF")

flow.run()

"""
Pour lancer : ouvrir un terminal et taper main\clear_temp.py
"""
