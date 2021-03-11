# great-circle-distance

## Installation

Python3.7+ is required.

Only standard python libraries used for execution. Install pytest to run the unit tests.

You can install pytest by `pip install -r requirements.txt`.

## Run 
Base command:
```
Python main.py --customer-list </path/to/input>
```

Run with optional arguments:
```
Python main.py --customer-list </path/to/input> --distance <distance_limit> --output-name </path/to/output>
```
Help command:
```
Python main.py --help
```

customer.txt is provided as a sample input.
If distance and output name are not specified, default values of 100 KM and output.txt are used.

You should specify distance limit in KM and input should be the same format as customer.txt sample which means json customer object per line.

## Run Tests

`pytest -v` will run all the unit tests with test names.
