import csv
import datetime
import os

class StudioManager:
    def __init__(self, log_file="progress_log.csv"):
        self.log_file = log_file
        self.team_members = [
            "Alex (Lead Designer)",
            "Sam (Unity Dev)",
            "Jordan (Roblox Dev)",
            "Casey (Artist)",
            "Riley (Sound Engineer)",
            "Morgan (QA Tester)",
            "Taylor (Project Manager)"
        ]
        self._initialize_log()

    def _initialize_log(self):
        """Ensures the CSV log file exists with a header."""
        if not os.path.exists(self.log_file):
            with open(self.log_file, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Member", "Task Description"])

    def display_menu(self):
        """Displays the interactive CLI menu."""
        print("\n" + "="*30)
        print("   STUDIO SYNC CLI")
        print("="*30)
        print("Select a team member:")
        for idx, member in enumerate(self.team_members, 1):
            print(f"{idx}. {member}")
        print("0. Exit")
        print("="*30)

    def log_progress(self):
        """Orchestrates the logging process."""
        while True:
            self.display_menu()
            try:
                choice = int(input("\nEnter choice (0-7): "))
                if choice == 0:
                    print("Exiting Studio Sync. Have a great day!")
                    break
                elif 1 <= choice <= 7:
                    member = self.team_members[choice - 1]
                    task = input(f"Enter daily progress for {member}: ").strip()
                    if task:
                        self._save_to_csv(member, task)
                        print(f"\n[SUCCESS] Logged for {member}.")
                    else:
                        print("\n[ERROR] Task cannot be empty.")
                else:
                    print("\n[ERROR] Invalid selection.")
            except ValueError:
                print("\n[ERROR] Please enter a valid number.")

    def _save_to_csv(self, member, task):
        """Writes the entry to the CSV file."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, member, task])

if __name__ == "__main__":
    manager = StudioManager()
    manager.log_progress()
