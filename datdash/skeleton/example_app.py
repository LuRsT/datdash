from example_samplers import *

def run(app, event_handler):
    samplers = [
        SynergySampler(event_handler, 3),
        BuzzwordsSampler(event_handler, 2),
        ConvergenceSampler(event_handler, 1),
    ]

    try:
        app.run(
            debug=True,
            host='0.0.0.0',
            port=5000,
            threaded=True,
            use_reloader=False,
            use_debugger=True
        )
    finally:
        print "Disconnecting clients"
        event_handler.stopped = True

        print "Stopping %d timers" % len(samplers)
        for (i, sampler) in enumerate(samplers):
            sampler.stop()

    print "Done"

