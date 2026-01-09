// Storage key for localStorage
const STORAGE_KEY = 'gymTrackerWorkouts';

// Get workouts from localStorage
function getWorkouts() {
    const workouts = localStorage.getItem(STORAGE_KEY);
    return workouts ? JSON.parse(workouts) : [];
}

// Save workouts to localStorage
function saveWorkouts(workouts) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(workouts));
}

// Format date for display
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('sv-SE', { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
    });
}

// Create workout item HTML
function createWorkoutItem(workout, index) {
    const item = document.createElement('div');
    item.className = 'workout-item';
    
    const weightText = workout.weight ? `${workout.weight} kg` : 'Kroppsvikt';
    
    item.innerHTML = `
        <div class="workout-details">
            <div class="workout-title">${workout.exercise}</div>
            <div class="workout-stats">
                ${workout.sets} set × ${workout.reps} reps @ ${weightText}
            </div>
            <div class="workout-date">${formatDate(workout.date)}</div>
        </div>
        <button class="delete-btn" data-index="${index}">Ta bort</button>
    `;
    
    return item;
}

// Render workout list
function renderWorkouts() {
    const workoutList = document.getElementById('workoutList');
    const workouts = getWorkouts();
    
    if (workouts.length === 0) {
        workoutList.innerHTML = '<p class="empty-message">Ingen träningshistorik än. Lägg till ditt första träningspass!</p>';
        return;
    }
    
    workoutList.innerHTML = '';
    
    // Sort workouts by date (newest first)
    workouts.sort((a, b) => new Date(b.date) - new Date(a.date));
    
    workouts.forEach((workout, index) => {
        const item = createWorkoutItem(workout, index);
        workoutList.appendChild(item);
    });
    
    // Add delete button listeners
    document.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const index = parseInt(e.target.dataset.index);
            deleteWorkout(index);
        });
    });
}

// Add new workout
function addWorkout(workout) {
    const workouts = getWorkouts();
    workouts.push(workout);
    saveWorkouts(workouts);
    renderWorkouts();
}

// Delete workout
function deleteWorkout(index) {
    if (confirm('Är du säker på att du vill ta bort detta träningspass?')) {
        const workouts = getWorkouts();
        workouts.splice(index, 1);
        saveWorkouts(workouts);
        renderWorkouts();
    }
}

// Clear all workouts
function clearAllWorkouts() {
    if (confirm('Är du säker på att du vill radera all träningshistorik? Detta kan inte ångras.')) {
        localStorage.removeItem(STORAGE_KEY);
        renderWorkouts();
    }
}

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    // Set today's date as default
    const dateInput = document.getElementById('date');
    dateInput.valueAsDate = new Date();
    
    // Render initial workouts
    renderWorkouts();
    
    // Handle form submission
    const form = document.getElementById('workoutForm');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const workout = {
            exercise: document.getElementById('exercise').value.trim(),
            sets: parseInt(document.getElementById('sets').value),
            reps: parseInt(document.getElementById('reps').value),
            weight: document.getElementById('weight').value ? parseFloat(document.getElementById('weight').value) : null,
            date: document.getElementById('date').value,
            timestamp: Date.now()
        };
        
        addWorkout(workout);
        form.reset();
        dateInput.valueAsDate = new Date();
        
        // Focus back to exercise input
        document.getElementById('exercise').focus();
    });
    
    // Handle clear all button
    const clearAllBtn = document.getElementById('clearAll');
    clearAllBtn.addEventListener('click', clearAllWorkouts);
});
