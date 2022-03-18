# x3p1

See https://www.youtube.com/watch?v=094y1Z2wpJg.

This is about sequences having just these rules:
* if value `y` is even, then divide it by 2
* if it's odd, then turn it into `3*y + 1`

## Requirements

* A recent Python 3.
* [Matplotlib](https://matplotlib.org/).

## Usage

```
python x3p1.py <max_initial_value>
```

## A video was made out of plot pictures

See https://www.youtube.com/watch?v=TzE3z4Burdk.

Video was made with
```
ffmpeg -framerate 2 -pattern_type glob -i 'plots/jpg/*.jpg' out.mp4
```