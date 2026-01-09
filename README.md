# SB_GymTracker
Super Basic Gym Tracker - Load and track your gym workouts from local folders

## Features
- ✅ Load gym tracker projects from local folders
- ✅ Store workout data in simple JSON format
- ✅ View project information and workout history
- ✅ Simple Python API for easy integration

## Quick Start

### 1. Load a project from a local folder

```python
from gym_tracker import GymTracker

tracker = GymTracker()
tracker.load_project_from_folder('./example_project')
```

### 2. View project information

```python
print(tracker.get_project_info())
print(tracker.list_workouts())
```

### 3. Run the example

```bash
python3 example_usage.py
```

## Project Structure

Your gym project folder should contain a `project.json` file:

```json
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
```

## Usage Examples

See `example_usage.py` for complete examples of how to:
- Load projects from local folders
- Display project information
- List workouts and exercises

## Testing

Run the test suite:

```bash
python3 test_gym_tracker.py -v
```

## Requirements

- Python 3.6+
- No external dependencies required

## How to Use

1. Create a folder for your gym project
2. Create a `project.json` file in that folder with your workout data
3. Use the GymTracker class to load and view your data:

```python
tracker = GymTracker()
tracker.load_project_from_folder('/path/to/your/project')
```

## Example Project

An example project is included in the `example_project/` folder. You can use it as a template for your own gym tracking data.
