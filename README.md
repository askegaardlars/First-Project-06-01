# First-Project-06-01

The overall goal is to acquire images on one device and serve them via a network port over ZeroMQ.
We have a display program in Python that we can swap the video capture elements with received images via 
zmq and use for testing, which requires a connected camera that can be opened via the OpenCV library. 
Display program is named demo_display.py and will need to be modified to use zmq and subscribe to the server.
The program can rely on OpenCV to read in a similar manner as the demo program and can
be implemented in either C++ or Python.

Requirements: The server program must 1) open the available main camera interface, 2) provide a zmq publish topic via port 8083 and 
3) publish images to this topic. The client program (modified from demo_program.py) must 1) subscribe to the server's
topic 2) display images received and 3) print out the framerate. Printing out the latency will be a later goal (intentionally).



