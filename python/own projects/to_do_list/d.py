import signal
import time

# Define a custom exception
class TimeoutException(Exception):
    pass

# Handler that raises our exception when called
def timeout_handler(signum, frame):
    raise TimeoutException("The function took too long and was interrupted!")

# Register the signal handler
signal.signal(signal.SIGALRM, timeout_handler)

def long_running_function():
    print("Function started...")
    time.sleep(10) # Simulating heavy work
    print("Function finished successfully!")

try:
    signal.alarm(3)  # Set interrupt timer for 3 seconds
    long_running_function()
except TimeoutException as e:
    print(f"Caught interruption: {e}")
finally:
    signal.alarm(0)  # Disable the alarm
