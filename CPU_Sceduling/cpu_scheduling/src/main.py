from cpu import clearscr, enter_process_details, view_process_details, sjf_non_preemptive, view_chart, view_avg_wait, view_turnaround
from menu import print_menu

def main():
    while True:
        print_menu()
        
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            enter_process_details()
        elif choice == "2":
            view_process_details()
        elif choice == "3":
            timeline = sjf_non_preemptive()
            view_chart(timeline)
        elif choice == "4":
            view_avg_wait()
        elif choice == "5":
            view_turnaround()
        elif choice == "6":
            print("Exiting Program...")
            break