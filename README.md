* Description:
This microservice provides accurate date and time information using a ZeroMQ publish-subscribe pattern.

* Communication Contract:
Requesting Data:
There is no explicit request mechanism. The subscriber automatically receives updates.
Receiving Data:
Format: Timestamp string in the format YYYY-MM-DD HH:MM:SS
Frequency: Every 1 second
Protocol: ZeroMQ PUB/SUB
Port: 5555
Topic: No specific topic (empty string to subscribe to all)

* Example Usage:

Python
# Subscriber (Client) Code Example

import zmq

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://[Your Microservice IP or Hostname]:5555")
subscriber.setsockopt_string(zmq.SUBSCRIBE, "") 

while True:
    timestamp = subscriber.recv_string()
    print(f"Received: {timestamp}")
    
* UML Sequence Diagram:
participant Subscriber
participant Microservice

Subscriber -> Microservice: Connects (zmq.SUB) to tcp://[Your Microservice IP or Hostname]:5555
Subscriber -> Microservice: Subscribes (zmq.SUBSCRIBE, "")
loop Every 1 second
    Microservice -> Subscriber: Sends timestamp (zmq.PUB)
    Subscriber -> Subscriber: Processes timestamp
  end
  
* Mitigation Plan:
  
Status: The microservice is fully functional.
Access:
The code for this microservice is available on GitHub: [https://github.com/ICANDIGITAL/](https://github.com/ICANDIGITAL/date-time-microservice/tree/master)
Your teammate can either run it locally or you can provide a hosted instance if they prefer.
Contingency:
If your teammate cannot access your microservice:
They should immediately contact me via Slack.
My availability is 9:30 am to 6:00 pm (Monday through Friday).
The deadline for notification is 05/27/2024, preferably within 48 hours.
Additional Notes:
Ensure your teammate has ZeroMQ installed in their Python environment (pip install pyzmq).
If you are hosting the service, please provide the IP address or hostname where it is running.
Consider potential network issues or firewalls that might block communication and discuss solutions in advance.
For robust error handling, all teammates should incorporate timeout mechanisms and retry logic in their subscriber code.
