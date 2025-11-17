from typing import Dict
Pinfo = Dict[str, any]
Process = Dict[str, Pinfo]

def arrival_time(process: Process, count: int):
    n = input("How many processes are you entering? ")