# x3p1

See https://www.youtube.com/watch?v=094y1Z2wpJg.

## Usage

```
python x3p1.py <max_initial_value>
```

It will draw two lines: the one which reaches the higest peak,
and the one which "lasts longer" before reaching the value of 1.

All attempted sequences (with a different initial value ranging from 1 to `max_initial_value`)
are interrupted when the value `1` is reached (otherwise, from there, it will just continue
in a loop 1, 4, 2, 1, 4, 2, 1, 4, 2, 1, ...).

### Examples

```
python x3p1.py 3421

Loading from cache...............................
Computing 94.5 %
```


![3421](https://user-images.githubusercontent.com/55979/158028295-6ad65564-446f-4e34-886f-0269cd05cd6f.png)

Scientific notation from the command line also supported:

```
python x3p1.py 3.7e5
Loading from cache...............................
Computing 100.0 %
```

![image](https://user-images.githubusercontent.com/55979/158028401-1ba7444f-e505-47a9-8b3d-24db3f940072.png)

Using interactive matplotlib GUI, we can e.g. redraw in logarithmic scale to appreciate the different order of magnitude:

![image](https://user-images.githubusercontent.com/55979/158028504-9ac0198b-8653-4a02-bbac-cf0b383b345c.png)

## Caching

Results from previous runs are automatically cached and reused to speedup the execution if possible.

Just delete the file `.cache.json` if you want to start fresh instead.
