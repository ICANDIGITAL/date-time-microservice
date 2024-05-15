import zmq
import time

def main():
    context = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5555")

    try:
        while True:
            # Publish the current date and time
            publisher.send_string(time.strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(1)  # Wait for 1 second
    except KeyboardInterrupt:
        print("Publisher service is shutting down...")
    finally:
        publisher.close()
        context.term()

if __name__ == "__main__":
    main()