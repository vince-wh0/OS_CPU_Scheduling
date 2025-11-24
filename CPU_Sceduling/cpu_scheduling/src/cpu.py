import os
# Process Class to hold process details
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

# Clear Screen Function
def clearscr():
    if os.name == 'nt':
        os.system('cls')
    else: os.system('clear')

# Function to enter process details
def enter_process_details():
    clearscr()
    global processes
    n = int(input("\nHow many process are you entering? "))
    
    # Get the starting index for new processes
    starting_index = len(processes)
    
    # Input process details
    for i in range(n):
        print(f"\nProcess {starting_index + i + 1} Details")
        arrival = int(input("Enter Arrival Time: "))
        burst = int(input("Enter Burst Time: "))
        processes.append(Process(f"P{starting_index + i + 1}", arrival, burst))
        
    print("\nProcess added successfully!")
    input("Press Enter...")

# Function to view process details        
def view_process_details():
    clearscr()
    # Check if there are any processes
    if not processes:
        print("\nNo process details available. Please enter process details first.")
        input("Press Enter...")
        return
    
    # Display process details
    print("\nProcess Details")
    print("PID\tArrival\tBurst")
    for p in processes:
        print(f"{p.pid}\t{p.arrival}\t{p.burst}")
        print("-" * 30)
    
    print("\nSuccessfully displayed process details!")
    input("Press Enter...")

# SJF Non-Preemptive Scheduling Algorithm
def sjf_non_preemptive():
    clearscr()
    if not processes:
        print("\nNo processes to schedule. Please enter process details first.")
        input("Press Enter...")
        return []
    
    # Sort processes by arrival time
    procs = sorted(processes, key=lambda x: x.arrival)
    timeline = []
    time = 0
    completed = 0
    n = len(procs)
    done = [False]*n
    
    # Scheduling Loop
    while completed < n:
        available = []
        # Check for available processes
        for i in range(n):
            if procs[i].arrival <= time and not done[i]:
                available.append(procs[i])
        
        # Select process with minimum burst time
        if available:
            current = min(available, key=lambda x: x.burst)
        # If no process is available, increment time
        else:
            time += 1
            continue
        
        # Execute current process
        current.start = time
        time += current.burst
        current.completion = time
        current.turnaround = current.completion - current.arrival
        current.waiting = current.start - current.arrival
        
        # Mark process as done
        done[procs.index(current)] = True
        completed += 1
        
        # Append to timeline
        timeline.append((current.pid, current.start, current.completion))
        
    return timeline

# Function to view Gantt Chart
def view_chart(timeline):
    clearscr()
    # Check if timeline is empty
    if not timeline:
        print("\nNo process to chart. Please enter process details.")
        input("Press Enter...")
        return

    # Display Gantt Chart
    print("\nGANTT CHART\n")

    # TOP borders
    for p, s, e in timeline:
        print("+--------+", end=" ")
    print()

    # PROCESS boxes
    for p, s, e in timeline:
        print(f"|   {p}   |", end=" ")
    print()

    # BOTTOM borders
    for p, s, e in timeline:
        print("+--------+", end=" ")
    print()

    # TIMELINE (start time of first process)
    print(timeline[0][1], end="")

    # Completion times spaced under each box
    for p, s, e in timeline:
        print(f"         {e}", end="")
    print()
    
    # Calculate and display Average Waiting Time   
    total = sum(p.waiting for p in processes)
    print(f"\nAverage Waiting Time = {total/len(processes):.2f}") 
    input("\nPress Enter...")

# Function to view Average Waiting Time
def view_avg_wait():
    clearscr()
    sjf_non_preemptive()
    # Calculate and display Average Waiting Time
    total = sum(p.waiting for p in processes)
    print(f"\nAverage Waiting Time = {total/len(processes):.2f}")
    input("\nPress Enter...")

# Function to view Turnaround Time    
def view_turnaround():
    clearscr()
    sjf_non_preemptive()
    print("\nTurnaround Times")
    print("PID\tTAT")
    for p in processes:
        print(f"{p.pid}\t{p.turnaround}")
        print("-" * 15)
        
    input("\nPress Enter...")


        