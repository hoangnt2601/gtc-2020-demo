# gtc example

```
gst-launch-1.0 uridecodebin source::latency=200 uri=rtsp://localhost:8557/mystream ! videoconvert ! autovideosink
```