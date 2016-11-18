### ohesteebee

A pythonic OpenTSDB client to send and receive time series data.


#### Examples

##### Get.

```
from ohesteebee import Ostb

ostb = Ostb(host="ostb.local", port="8080")

# Defaults to a 1h window from now with no tags.
ostb.get('system.load.1')

# Add a lookback of either a timedelta or a value + y/m/d/h/m/s.
ostb.get('system.load.1', lookback="1d")
```


##### Put.
```
from ohesteebee import Ostb

ostb = Ostb(host="ostb.local", port="8080")

# Put takes any series of kwargs as tags.
ostb.put('system.load.1', 1.1, foo=bar, baz=qux)
```
