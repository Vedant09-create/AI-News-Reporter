from datetime import datetime

def save_markdown(task_output):
    """
    Saves the task output to a markdown file with today's date as the filename.
    
    Args:
        task_output: The result of the newsletter compilation task.
        
    Returns:
        None
    """
    # Get today's date in the format YYYY-MM-DD
    today_date = datetime.now().strftime('%Y-%m-%d')
    # Set the filename with today's date
    filename = f"{today_date}.md"
    try:
        # Write the task output to the markdown file
        with open(filename, 'w') as file:
            file.write(task_output.result)
        print(f"Newsletter saved as {filename}")
    except Exception as e:
        print(f"Error saving the newsletter: {e}")