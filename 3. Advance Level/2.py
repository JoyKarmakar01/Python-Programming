from multiprocessing import Process

def print_numbers():
    for i in range(5):
        print(i)

if __name__ == "__main__":  # Ensure safe process creation
    # Create a process
    process = Process(target=print_numbers)
    process.start()  # Start the process
    process.join()   # Wait for the process to complete
