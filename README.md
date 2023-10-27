# Glitchlib

This library implements a couple of utility functions for communication with fault-injection tools such as the Pico Debug'n'Dump based glitchers.

## Install

```bash
python3 setup.py install
```

## Glitcher

A simple class that automatically connects and interfaces with glitchers that use the **Simple Glitcher Protocol**.

### Usage

```python
from glitchlib import Glitcher
# Automatically opens all USB serial devices, sends the ID command, and checks whether the device identifies itself as a glitcher.
g = Glitcher()

# Flush queued serial data
g.flush()

# Reset the target (if implemented)
g.reset()

# Set delay & pulse
g.set_delay(1000)
g.set_pulse(15)

# Glitch (Does not block)
g.glitch()
# Read from serial
g.read()
g.read(1)
```

## GlitchDataCollection

A utility library to manage, store and visualize glitching results.

### Usage

First we need to initialize a GlitchDataCollection:

```python
from glitchlib import GlitchDataCollection
gdc = GlitchDataCollection()
```

Next, we add different types of glitch results we want to store, such as success & hang. The first argument is a unique key, such as an int or a char, that identifies the result type. The second argument is the name used on the legend etc.

```python
gdc.add_data("HNG", "Hang", color="red")
gdc.add_data("X", "Other", color="gray")
# Additional options: color, zorder (higher = rendered in front), alpha
gdc.add_data("SUC", "Success", color="green", zorder=2, alpha=1.0)
```

Next, we can start adding data to each of the result categories:

```python
for delay in range(0, 3000):
    for pulse in range(0, 15):
        if((delay + pulse) % 100 = 0):
            gdc.add("SUC", delay, pulse)
        elif((delay + pulse)) % 33 = 0:
            gdc.add("HNG", delay, pulse)
        else:
            gdc.add("X", delay, pulse)
```

Finally, we can visualize the glitches:

```python
# Autorange
gdc.plot()
# Use explicit range
gdc.plot(x=[start, end], y=[pulse_min, pulse_max])
```

We can also load and store GlitchDataCollections.

**Note:** This currently uses pickle. Do not load GlitchDataCollections from untrusted sources.

```python
gdc.save("filename")
gdc = GlitchDataCollection.load("filename")
```
