"""
CP1404/CP5632 Practical 7 - Project Management Program task

Estimated time: 2 hours
Actual time:
"""

from project import Project

FILENAME = "projects.txt"

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""


def main():
    """Run the Project Management Program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from projects.txt.")
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    projects = []
    with open(filename, "r", encoding="utf-8-sig") as input_file:
        input_file.readline()
        for line in input_file:
            parts = line.strip().split("\t")
            name, start_date, priority_str, cost_str, completion_str = parts

            priority = int(priority_str)
            cost_estimate = float(cost_str)
            completion_percentage = int(completion_str)

            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def save_projects(filename, projects):
    pass


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f" {project}")
    print("Complete projects:")
    for project in completed_projects:
        print(f" {project}")


def sort_projects():
    pass


def add_project():
    pass


def update_project():
    pass


if __name__ == "__main__":
    main()
