#!/usr/bin/env python3
"""
Super Basic Gym Tracker - Main Application
Load and manage gym tracking data from local folders
"""

import os
import json
from datetime import datetime
from pathlib import Path


class GymTracker:
    """Main gym tracker application for loading projects from local folders"""
    
    def __init__(self):
        self.project_data = None
        self.project_path = None
    
    def load_project_from_folder(self, folder_path):
        """
        Load a gym tracker project from a local folder
        
        Args:
            folder_path (str): Path to the folder containing project data
            
        Returns:
            dict: The loaded project data
            
        Raises:
            FileNotFoundError: If folder doesn't exist
            ValueError: If project data is invalid
        """
        folder = Path(folder_path)
        
        if not folder.exists():
            raise FileNotFoundError(f"Folder not found: {folder_path}")
        
        if not folder.is_dir():
            raise ValueError(f"Path is not a folder: {folder_path}")
        
        # Look for project.json file
        project_file = folder / "project.json"
        
        if not project_file.exists():
            raise FileNotFoundError(
                f"No project.json found in folder: {folder_path}"
            )
        
        # Load project data
        with open(project_file, 'r', encoding='utf-8') as f:
            self.project_data = json.load(f)
        
        self.project_path = folder
        
        print(f"✓ Project loaded successfully from: {folder_path}")
        print(f"  Project name: {self.project_data.get('name', 'Unnamed')}")
        print(f"  Workouts: {len(self.project_data.get('workouts', []))}")
        
        return self.project_data
    
    def get_project_info(self):
        """Get information about the currently loaded project"""
        if not self.project_data:
            return "No project loaded"
        
        info = []
        info.append(f"Project: {self.project_data.get('name', 'Unnamed')}")
        info.append(f"Location: {self.project_path}")
        info.append(f"Workouts: {len(self.project_data.get('workouts', []))}")
        
        if 'created' in self.project_data:
            info.append(f"Created: {self.project_data['created']}")
        
        return "\n".join(info)
    
    def list_workouts(self):
        """List all workouts in the current project"""
        if not self.project_data:
            return "No project loaded"
        
        workouts = self.project_data.get('workouts', [])
        
        if not workouts:
            return "No workouts found in project"
        
        result = ["Workouts:"]
        for i, workout in enumerate(workouts, 1):
            date = workout.get('date', 'No date')
            exercises = len(workout.get('exercises', []))
            result.append(f"  {i}. {date} - {exercises} exercises")
        
        return "\n".join(result)


def main():
    """Main entry point for the application"""
    print("=== Super Basic Gym Tracker ===")
    print()
    
    tracker = GymTracker()
    
    # Example usage
    print("Usage: Load a project from a local folder")
    print("  tracker.load_project_from_folder('/path/to/folder')")
    print()
    print("The folder should contain a 'project.json' file with your gym data")
    print()
    
    return tracker


if __name__ == "__main__":
    main()
