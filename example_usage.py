#!/usr/bin/env python3
"""
Example: How to use Gym Tracker to load a project from a local folder
"""

from gym_tracker import GymTracker


def main():
    print("=== Gym Tracker - Loading Local Projects ===\n")
    
    # Create a new tracker instance
    tracker = GymTracker()
    
    # Example 1: Load the example project
    print("Example 1: Loading example project...")
    try:
        project_data = tracker.load_project_from_folder("./example_project")
        print(f"✓ Project loaded successfully")
        print(f"  Project name: {project_data.get('name', 'Unnamed')}")
        print(f"  Workouts: {len(project_data.get('workouts', []))}")
        print()
        
        # Display project info
        print(tracker.get_project_info())
        print()
        
        # List workouts
        print(tracker.list_workouts())
        print()
        
    except Exception as e:
        print(f"Error: {e}")
        print()
    
    # Example 2: Load from a different path
    print("\nExample 2: How to load your own project...")
    print("1. Create a folder for your gym project")
    print("2. Create a 'project.json' file in that folder")
    print("3. Use tracker.load_project_from_folder('/path/to/your/folder')")
    print()
    
    # Show expected JSON format
    print("Example project.json format:")
    print("""
{
  "name": "My Gym Training",
  "created": "2026-01-09",
  "workouts": [
    {
      "date": "2026-01-06",
      "exercises": [
        {
          "name": "Bench Press",
          "sets": 3,
          "reps": 10,
          "weight_kg": 80
        }
      ]
    }
  ]
}
    """)


if __name__ == "__main__":
    main()
