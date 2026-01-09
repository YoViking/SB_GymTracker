#!/usr/bin/env python3
"""
Tests for Gym Tracker - Local Project Loading
"""

import unittest
import json
import os
import tempfile
import shutil
from pathlib import Path
from gym_tracker import GymTracker


class TestGymTrackerLocalLoading(unittest.TestCase):
    """Test cases for loading projects from local folders"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.tracker = GymTracker()
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test fixtures"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_load_valid_project(self):
        """Test loading a valid project from a local folder"""
        # Create test project
        project_data = {
            "name": "Test Project",
            "created": "2026-01-09",
            "workouts": [
                {
                    "date": "2026-01-01",
                    "exercises": [
                        {"name": "Push-ups", "sets": 3, "reps": 15}
                    ]
                }
            ]
        }
        
        project_file = Path(self.test_dir) / "project.json"
        with open(project_file, 'w') as f:
            json.dump(project_data, f)
        
        # Load project
        loaded_data = self.tracker.load_project_from_folder(self.test_dir)
        
        # Verify
        self.assertIsNotNone(loaded_data)
        self.assertEqual(loaded_data['name'], "Test Project")
        self.assertEqual(len(loaded_data['workouts']), 1)
    
    def test_load_folder_not_found(self):
        """Test loading from non-existent folder raises error"""
        with self.assertRaises(FileNotFoundError):
            self.tracker.load_project_from_folder("/nonexistent/folder")
    
    def test_load_missing_project_file(self):
        """Test loading from folder without project.json raises error"""
        with self.assertRaises(FileNotFoundError):
            self.tracker.load_project_from_folder(self.test_dir)
    
    def test_load_file_instead_of_folder(self):
        """Test loading from a file instead of folder raises error"""
        test_file = Path(self.test_dir) / "test.txt"
        test_file.touch()
        
        with self.assertRaises(ValueError):
            self.tracker.load_project_from_folder(str(test_file))
    
    def test_get_project_info_without_loading(self):
        """Test getting project info when no project is loaded"""
        info = self.tracker.get_project_info()
        self.assertEqual(info, "No project loaded")
    
    def test_get_project_info_after_loading(self):
        """Test getting project info after loading a project"""
        # Create test project
        project_data = {
            "name": "Test Gym",
            "created": "2026-01-09",
            "workouts": []
        }
        
        project_file = Path(self.test_dir) / "project.json"
        with open(project_file, 'w') as f:
            json.dump(project_data, f)
        
        self.tracker.load_project_from_folder(self.test_dir)
        info = self.tracker.get_project_info()
        
        self.assertIn("Test Gym", info)
        self.assertIn("Workouts: 0", info)
    
    def test_list_workouts(self):
        """Test listing workouts from loaded project"""
        # Create test project with multiple workouts
        project_data = {
            "name": "Test Project",
            "workouts": [
                {
                    "date": "2026-01-01",
                    "exercises": [{"name": "Exercise1", "sets": 3}]
                },
                {
                    "date": "2026-01-02",
                    "exercises": [
                        {"name": "Exercise2", "sets": 2},
                        {"name": "Exercise3", "sets": 4}
                    ]
                }
            ]
        }
        
        project_file = Path(self.test_dir) / "project.json"
        with open(project_file, 'w') as f:
            json.dump(project_data, f)
        
        self.tracker.load_project_from_folder(self.test_dir)
        workouts = self.tracker.list_workouts()
        
        self.assertIn("2026-01-01", workouts)
        self.assertIn("2026-01-02", workouts)
        self.assertIn("1 exercises", workouts)
        self.assertIn("2 exercises", workouts)
    
    def test_list_workouts_empty_project(self):
        """Test listing workouts from project with no workouts"""
        project_data = {
            "name": "Empty Project",
            "workouts": []
        }
        
        project_file = Path(self.test_dir) / "project.json"
        with open(project_file, 'w') as f:
            json.dump(project_data, f)
        
        self.tracker.load_project_from_folder(self.test_dir)
        workouts = self.tracker.list_workouts()
        
        self.assertEqual(workouts, "No workouts found in project")
    
    def test_load_invalid_json(self):
        """Test loading from folder with invalid JSON raises error"""
        project_file = Path(self.test_dir) / "project.json"
        with open(project_file, 'w') as f:
            f.write("{invalid json content")
        
        with self.assertRaises(ValueError) as context:
            self.tracker.load_project_from_folder(self.test_dir)
        
        self.assertIn("Invalid JSON", str(context.exception))


if __name__ == '__main__':
    unittest.main()
