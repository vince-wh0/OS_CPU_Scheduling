# Function to print a boxed title
def box_title(title: str) -> None:
    line = "═" * (len(title) + 8)
    print(f"╔{line}╗")
    print(f"║    {title}    ║")
    print(f"╚{line}╝")

# Function to print the main menu
def print_menu():
    box_title("CPU Scheduling for SJF (Pre-emptive)")
    print("[1] Enter Process Details")
    print("[2] View Process Details")
    print("[3] View Gantt Chart")
    print("[4] View Average Waiting Time")
    print("[5] Turnaround Time")
    print("[6] Exit")
    
