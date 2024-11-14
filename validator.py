import sys

def read_input_file(input_file):
    with open(input_file, 'r') as file:
        num_tasks = int(file.readline().strip())
        tasks = []
        for _ in range(num_tasks):
            processing_time, ready_time = map(int, file.readline().strip().split())
            tasks.append((processing_time, ready_time))
        
        setup_times = []
        for _ in range(num_tasks):
            setup_times.append(list(map(int, file.readline().strip().split())))
    
    return tasks, setup_times

def read_output_file(output_file):
    with open(output_file, 'r') as file:
        total_completion_time = int(file.readline().strip())
        task_order = list(map(int, file.readline().strip().split()))
    
    return total_completion_time, task_order

def calculate_completion_time(tasks, setup_times, task_order):
    current_time = 0
    completion_time_sum = 0
    
    for i, task_id in enumerate(task_order):
        task_idx = task_id - 1  # Convert to 0-indexed
        processing_time, ready_time = tasks[task_idx]
        
        # If this is the first task, no setup time is required.
        if i == 0:
            current_time = max(current_time, ready_time)
        else:
            prev_task_idx = task_order[i - 1] - 1
            setup_time = setup_times[prev_task_idx][task_idx]
            current_time += setup_time
            current_time = max(current_time, ready_time)
        
        current_time += processing_time
        completion_time_sum += current_time

    return completion_time_sum

def check_output_validity(input_file, output_file):
    tasks, setup_times = read_input_file(input_file)
    total_completion_time, task_order = read_output_file(output_file)
    
    calculated_completion_time = calculate_completion_time(tasks, setup_times, task_order)
    
    if calculated_completion_time == total_completion_time:
        print("Output is valid.")
    else:
        print(f"Output is invalid. Expected {calculated_completion_time}, but got {total_completion_time}.")

input_file = sys.argv[1]
output_file = sys.argv[2]
check_output_validity(input_file, output_file)
