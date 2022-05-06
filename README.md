# Getting Started

PolyStocks is a custom module to watch stock prices for Polybar.

## Installation

- `$ pip3 install yahoo_fin`
- Copy `polystocks.py` to `~/.config/polybar/scripts`
- `$ chmod +x ~/.config/polybar/scripts/polystocks.py`

### ~/.config/polybar/config

```
[module/polystocks]
type = custom/script
exec = ~/.config/polybar/scripts/polystocks.py
tail = true
label = %output%
```
