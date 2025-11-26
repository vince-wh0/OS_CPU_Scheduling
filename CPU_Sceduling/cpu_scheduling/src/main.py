from cpu import clearscr, enter_process_details, view_process_details, sjf_non_preemptive, view_chart, view_avg_wait
from menu import print_menu

def main():
    while True:
        clearscr()
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
            print("Exiting Program...")
            break
        else:
            print("\nInvalid choice. Please try again.")
            input("Press Enter...")

if __name__ == "__main__":
    main()