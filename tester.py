import subprocess
import time
import threading

def run_publisher():
    subprocess.run(["python", "publisher.py"])  # Run publisher.py as a subprocess

def run_subscriber():
    subprocess.run(["python", "subscriber.py"])  # Run subscriber.py as a subprocess

if __name__ == "__main__":
    publisher_thread = threading.Thread(target=run_publisher)
    subscriber_thread = threading.Thread(target=run_subscriber)

    publisher_thread.start()
    subscriber_thread.start()

    time.sleep(5)  # Let the scripts run for a bit (adjust as needed)

    # Terminate both scripts (simulates Ctrl+C)
    subprocess.run(["pkill", "-f", "publisher.py"])
    subprocess.run(["pkill", "-f", "subscriber.py"])