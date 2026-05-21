# Studio Sync CLI
Studio Sync CLI is a professional-grade task tracking tool designed to streamline the workflow of high-performance game development teams. Built for reliability and ease of use, it ensures that every contribution is recorded and visible to the entire studio.

## 👥 Designed for Teams
This tool is optimized for a 7-member development team, providing a centralized system to track tasks across different disciplines. By using Studio Sync, team members like Unity Developers, Roblox Designers, and Artists can seamlessly log their daily output, reducing friction in stand-up meetings and ensuring project transparency.

## ⚙️ Core Functionalities
- **Interactive CLI Menu**: Simple, number-driven interface for quick task entry.
- **Object-Oriented Structure**: Built with Pythonic OOP principles for maintainability and scalability.
- **Automatic CSV Logging**: Real-time persistence of team progress.
- **Data persistence**: Reliable local storage in a structured CSV format, ready for review or integration into larger reporting tools.

## 📦 Installation & Usage
To get started with Studio Sync CLI, ensure you have Python installed, then follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Studio_Sync_CLI
   ```

2. **Run the application:**
   ```bash
   python studio_manager.py
   ```

## 📊 Sample Output
The `progress_log.csv` file will maintain entries in the following format:

| Timestamp           | Member           | Task Description            |
|---------------------|------------------|-----------------------------|
| 2026-05-21 10:00:00 | Alex (Lead)      | Roblox map layout done      |
| 2026-05-21 11:30:00 | Sam (Unity Dev)  | Unity bug fixed             |
| 2026-05-21 14:15:00 | Casey (Artist)   | UI assets exported          |
