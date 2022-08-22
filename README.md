# what_pulse.py
Web-API for [whatpulse.org](https://whatpulse.org) website that measures your keyboard/mouse usage

## Example
```python
import what_pulse
what_pulse = what_pulse.WhatPulse()
user_stats = what_pulse.get_user_stats(user_id="")
print(user_stats)
```
