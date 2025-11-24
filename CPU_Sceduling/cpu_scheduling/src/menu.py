# Function to print a boxed title
def box_title(title: str) -> None:
    line = "═" * (len(title) + 8)
    print(f"╔{line}╗")
    print(f"║    {title}    ║")
    print(f"╚{line}╝")

# Function to print the main menu
class Process: 
    def __init__(self, pid: int, burst_time: int, arrival_time: int):
        self.pid = pid
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        
process = []

def process_details():
    try:
        n = int(input("How many processes are you entering? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for i in range(n):
        start_id = i + 1
        burst_time = int(input(f"Enter burst time for P{start_id}: ")) 
        arrival_time = i
        print(f"Arrival Time (Automatic): {arrival_time}")

        p = Process(start_id, burst_time, arrival_time)
        process.append(p)
    print("\nProcesses added successfully!")

def view_process_details():
    if not process:
        print("No processes entered yet.")
        return

    print(f"{'Process':<10} {'Burst Time':<15} {'Arrival Time':<15}")
    print("-" * 40)
    for p in process:
        print(f"P{p.pid:<9} {p.burst_time:<15} {p.arrival_time:<15}")

#def view_gantt_chart():
#def view_avg_waiting_time():
#def view_turnaround_time():

def print_menu():
    while True:
        box_title("CPU Scheduling for SJF (Pre-emptive)")
        print("[1] Enter Process Details")
        print("[2] View Process Details")
        print("[3] View Gantt Chart")
        print("[4] View Average Waiting Time")
        print("[5] Turnaround Time")
        print("[6] Exit")
    
        choice = input("Enter your choice (1-6): ") 

        if choice == '1':
            process_details()
        elif choice == '2':
            view_process_details()
        #elif choice == '3':
            #view_gantt_chart()
        #elif choice == '4':
            #view_avg_waiting_time()
        #elif choice == '5':
            #view_turnaround_time()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    print_menu()