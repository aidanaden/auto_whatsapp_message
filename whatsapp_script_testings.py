import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(s): 
    print("Doing stuff...")
    # do your stuff
    s.enter(5, 1, do_something, (s,))

s.enter(5, 1, do_something, (s,))
s.run()