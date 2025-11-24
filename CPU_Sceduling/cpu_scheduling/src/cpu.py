import os
class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.start = 0
        self.completion = 0
        self.waiting = 0
        self.turnaround = 0

processes = []

def clearscr():
    if os.name == 'nt':
        os.system('cls')
    else: os.system('clear')

def enter_process_details():
    clearscr()
    global processes
    processes = []
    n = int(input("\nHow many process are you entering? "))
    
    for i in range(n):
        print(f"\nProcess {i + 1} Details")
        arrival = int(input("Enter Arrival Time: "))
        burst = int(input("Enter Burst Time: "))
        processes.append(Process(f"P{i + 1}", arrival, burst))
        
    print("\nProcess added successfully!")
    input("Press Enter...")
        
def view_process_details():
    clearscr()
    if not processes:
        print("\nNo process details available. Please enter process details first.")
        input("Press Enter...")
        return
    
    print("\nProcess Details")
    print("PID\tArrival\tBurst")
    for p in processes:
        print(f"{p.pid}\t{p.arrival}\t{p.burst}")
        print("-" * 30)
    
    print("\nSuccessfully displayed process details!")
    input("Press Enter...")

def sjf_non_preemptive():
    clearscr()
    if not processes:
        print("\nNo processes to schedule. Please enter process details first.")
        input("Press Enter...")
        return []
    
    procs = sorted(processes, key=lambda x: x.arrival)
    timeline = []
    time = 0
    completed = 0
    n = len(procs)
    done = [False]*n
    
    while completed < n:
        available = []
        for i in range(n):
            if procs[i].arrival <= time and not done[i]:
                available.append(procs[i])
        
        if available:
            current = min(available, key=lambda x: x.burst)
        else:
            time += 1
            continue
        
        current.start = time
        time += current.burst
        current.completion = time
        current.turnaround = current.completion - current.arrival
        current.waiting = current.start - current.arrival
        
        done[procs.index(current)] = True
        completed += 1
        
        timeline.append((current.pid, current.start, current.completion))
        
    return timeline

def view_chart(timeline):
    clearscr()
    if not timeline:
        print("\nNo process to chart. Please enter process details.")
        input("Press Enter...")
        return
    
    print("\nGantt Chart SJF (Non-Preemptive)")
    for p, s, e in timeline:
        print(f"| {p} ({s}→{e}) ", end="")
    print("|")
    input("\nPress Enter...")

def view_avg_wait():
    clearscr()
    sjf_non_preemptive()
    total = sum(p.waiting for p in processes)
    print(f"\nAverage Waiting Time = {total/len(processes):.2f}")
    input("\nPress Enter...")
    
def view_turnaround():
    clearscr()
    sjf_non_preemptive()
    print("\nTurnaround Times")
    print("PID\tTAT")
    for p in processes:
        print(f"{p.pid}\t{p.turnaround}")
        print("-" * 20)
        
    input("\nPress Enter...")


        