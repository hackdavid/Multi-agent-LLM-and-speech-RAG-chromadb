from task_manager import TaskManager
# Define a complex task (ticket text)
ticket_text = "I need help with my billing. The charges seem incorrect. It's urgent!"

# Initialize the task manager
task_manager = TaskManager()

# Execute the task
final_context = task_manager.execute_task(ticket_text)

# Display the final context
print("\nFinal Context:")
for key, value in final_context.items():
    print(f"{key}: {value}")
