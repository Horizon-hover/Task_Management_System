# task.py
import logging
from dataclasses import dataclass
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@dataclass
class Task:
    """Represents a task with a title, description, and completion status."""
    title: str
    description: str
    completed: bool = False

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True
        logging.info(f"Task '{self.title}' marked as completed.")

    def __str__(self) -> str:
        """Return a string representation of the task."""
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} ({status}): {self.description}"

class TaskManager:
    """Manages a collection of tasks."""
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str) -> None:
        """Add a new task to the manager."""
        if not title or not description:
            raise ValueError("Title and description cannot be empty.")
        self.tasks.append(Task(title, description))
        logging.info(f"Added task: '{title}'")

    def view_tasks(self) -> None:
        """Display all tasks."""
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(task)

    def mark_task_completed(self, title: str) -> None:
        """Mark a task as completed by its title."""
        task = self._find_task(title)
        if task:
            task.mark_completed()
        else:
            logging.warning(f"Task '{title}' not found.")

    def delete_task(self, title: str) -> None:
        """Delete a task by its title."""
        task = self._find_task(title)
        if task:
            self.tasks.remove(task)
            logging.info(f"Deleted task: '{title}'")
        else:
            logging.warning(f"Task '{title}' not found.")

    def _find_task(self, title: str) -> Optional[Task]:
        """Find a task by its title."""
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def save_tasks(self, filename: str) -> None:
        """Save tasks to a file."""
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.completed}\n")
        logging.info(f"Tasks saved to '{filename}'.")

    def load_tasks(self, filename: str) -> None:
        """Load tasks from a file."""
        try:
            with open(filename, "r") as file:
                self.tasks = []
                for line in file:
                    title, description, completed = line.strip().split(",")
                    task = Task(title, description, completed == "True")
                    self.tasks.append(task)
            logging.info(f"Tasks loaded from '{filename}'.")
        except FileNotFoundError:
            logging.error(f"File '{filename}' not found.")