import zmq

def main():
    context = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5555")
    subscriber.setsockopt_string(zmq.SUBSCRIBE, '')

    try:
        while True:
            # Receive the date and time from the publisher
            message = subscriber.recv_string()
            print(f"Current Date and Time: {message}")
    except KeyboardInterrupt:
        print("Subscriber service is shutting down...")
    finally:
        subscriber.close()
        context.term()

if __name__ == "__main__":
    main()