class EventHandler:
    def __init__(self):
        self.events_queue = {}
        self.last_events = {}
        self.using_events = True
        self.MAX_QUEUE_LENGTH = 20

    def pop_queue(self, event_stream_port):
        while True:
            data = self.events_queue[event_stream_port].get()
            yield data

