# test_task.py
import unittest
from task import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Learn Python", "Master Python programming.")
        self.assertEqual(len(self.manager.tasks), 1)

    def test_mark_task_completed(self):
        self.manager.add_task("Learn Python", "Master Python programming.")
        self.manager.mark_task_completed("Learn Python")
        self.assertTrue(self.manager.tasks[0].completed)

    def test_delete_task(self):
        self.manager.add_task("Learn Python", "Master Python programming.")
        self.manager.delete_task("Learn Python")
        self.assertEqual(len(self.manager.tasks), 0)

if __name__ == "__main__":
    unittest.main()