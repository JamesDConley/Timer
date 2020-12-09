# Timer

A simple timer utility that logs task start and stop. The interface roughly mimics the functionality of an actual stopwatch.

I imagine something like this already exists somewhere, but all I could find online was timeit which is more complex than I want

## Usage
```
t = Timer(log=True)
t.start("Run training") # Logs ~ "Run training started"
model.train()
total_seconds = t.stop() # Logs ~ "Run training took 1.5 minutes"
print(total_seconds) # Prints 90 
```