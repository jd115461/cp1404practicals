"""
CP1404/CP5632 Practical 7 - Project Management Program task
Create a program that completes the required applications with a loaded CSV file
Estimated time: 3.5 hours
Actual time:3 hours 51 minutes
"""
import datetime
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
            filename = input("Filename to load projects from: ").strip()
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}.")
        elif choice == "S":
            filename = input("Filename to save projects to: ").strip()
            save_projects(filename, projects)
            print(f"Projects saved to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").strip().upper()
    save_choice = input(f"Would you like to save to {FILENAME}? ").strip().lower()
    if save_choice in ("y", "yes"):
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from selected file."""
    projects = []
    with open(filename, "r", encoding="utf-8-sig") as input_file:
        input_file.readline()
        for line in input_file:
            parts = line.strip().split("\t")
            if len(parts) == 5:
                name, start_date, priority_str, cost_str, completion_str = parts
                priority = int(priority_str)
                cost_estimate = float(cost_str)
                completion_percentage = int(completion_str)
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save all changes to projects to the given file name."""
    with open(filename, "w", encoding="utf-8-sig") as output_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=output_file)
        for project in projects:
            output_file.write(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


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


def get_date_to_sort(project):
    return project.get_project_date()


def filter_projects(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ").strip()
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return

    filtered_projects = []
    for project in projects:
        project_date = project.get_project_date()
        if project_date and project_date.date() >= filter_date:
            filtered_projects.append(project)
    filtered_projects.sort(key=get_date_to_sort)

    if not filtered_projects:
        print("No projects found starting on or after that date.")
    else:
        for project in filtered_projects:
            print(project)


def add_project(projects):
    """Prompt for a new project and add it as incomplete to the list."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    while name == "":
        print("Input can not be blank")
        name = input("Name: ").strip()

    start_date = input("Start date (dd/mm/yyyy): ").strip()
    while start_date == "":
        print("Input can not be blank")
        start_date = input("Start date (dd/mm/yyyy): ").strip()

    priority = 0
    is_valid_input = False
    while not is_valid_input:
        try:
            priority = int(input("Priority: "))
            if 0 <= priority <= 10:
                is_valid_input = True
            else:
                print("Number must be between 1 and 10")
        except ValueError:
            print("Invalid input - please enter a valid number")

    cost_estimate = 0.0
    is_valid_input = False
    while not is_valid_input:
        try:
            cost_estimate = float(input("Cost estimate: $"))
            if cost_estimate < 0:
                print("Number must be greater than or equal to 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input - please enter a valid number")

    completion_percentage = 0
    is_valid_input = False
    while not is_valid_input:
        try:
            completion_percentage = int(input("Percent complete: "))
            if 0 <= completion_percentage <= 100:
                is_valid_input = True
            else:
                print("Number must be between 0 and 100")
        except ValueError:
            print("Invalid input - please enter a valid number")

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print(f"Project '{name}' added successfully.")


def update_project(projects):
    """Prompt user for a project number and update completion percentage and/or priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    if not incomplete_projects:
        print("All projects have been completed.")
        return

    for i, project in enumerate(incomplete_projects, start=1):
        print(f"{i} {project}")

    is_valid_input = False
    while not is_valid_input:
        try:
            chosen_project = int(input("Project choice: "))
            if chosen_project <= 0:
                print("Number must be > 0")
            elif chosen_project > len(incomplete_projects):
                print("Invalid project number")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input - please enter a valid number")

    chosen_project = incomplete_projects[chosen_project - 1]
    print(f"Selected: {chosen_project}")

    updated_percentage_input = input("New Percentage: ").strip()
    if updated_percentage_input != "":
        try:
            updated_percentage = int(updated_percentage_input)
            if 0 <= updated_percentage <= 100:
                chosen_project.completion_percentage = updated_percentage
            else:
                print("Invalid value – must be between 0 and 100. Percentage not changed.")
        except ValueError:
            print("Invalid input - please enter a valid number")

    updated_priority_input = input("New Priority: ").strip()
    if updated_priority_input != "":
        try:
            updated_priority = int(updated_priority_input)
            if 0 <= updated_priority <= 10:
                chosen_project.priority = updated_priority
            else:
                print("Invalid value, Priority not changed.")
        except ValueError:
            print("Invalid input - please enter a valid number")

    print("Project updated.")


if __name__ == "__main__":
    main()
