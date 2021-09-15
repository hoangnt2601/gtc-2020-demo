import time
from pygstc.gstc import *
from pygstc.gstcerror import GstdError


# Create GstD Python client
client = GstdClient()

# Create camera pipelines
name = 'camera0'
parse = 'uridecodebin source::latency=200 uri=rtsp://localhost:8557/mystream ! videoconvert ! autovideosink'
try:
    client.pipeline_create(name, parse)
    print(f"Creating pipeline: {name}")
except GstdError as e:
    print(e)

client.pipeline_play(name)
print(f"Playing pipeline: {name}")

time.sleep(10)

client.pipeline_stop(name)
print(f"Stopping pipeline: {name}")