# Price Fetcher

This project aims to generate simple log containing current prices on a given list
of products (and their sum).

# Dependencies
In order to execute this project, you're going to need `python3` installed onto
your computer, and the following dependencies:
+ `urllib2`
+ `re`
+ `json`
+ `datetime`
+ `sys`
+ `threadings`

## Execution
First, you'll prepare the ambient with `make`. Then, to execute, just open the 
project folder on your favorite terminal and type:
```bash
python3 pcalc [file-with-links] [fetcher] {[output-format]}
```
+ `file-with-links` - A simple `.txt` file containing one link per line ([example](#use-examples)).
+ `fetcher` - The fetcher that you will use, you can select any from 
[here](#available-fetchers).
+ `output-format` - The desired log output format (`json` or `csv`). If none, `json` will be selected.

### Available Fetchers
+ [`mercadolivre`](https://www.mercadolivre.com.br)
+ [`kabum`](https://www.kabum.com.br)

*Have one? feel free to make a pull request with it!*

### Use examples
Let's say i have a file on `configs/test.txt`, and inside of it, i have:
```
https://produto.mercadolivre.com.br/MLB-1146730903-amd-ryzen-2700x-am4-43ghz-octa-core-16theads-rgb-lacrado-_JM
https://produto.mercadolivre.com.br/MLB-1024669523-adaptador-ativo-displayport-p-hdmi-20-4k-60hz-club3d-uhd-_JM
https://produto.mercadolivre.com.br/MLB-960954066-memoria-kingston-hyperx-fury-8gb-2400mhz-ddr4-gamer-cl15-_JM
```
I could run the program by typing the following commands:
```bash
./pcalc.py configs/test.txt mercadolivre
```

# Creating your custom API
I've designed this script to be as modular as you want. So with that in mind, 
just need some little coding to make this script adapt to your desired website.

You'll need basic knowledge in `re`(regex) and `python` in order to create your own
API.

With that in mind, follow these steps:
+ Navigate to `src/sites` and create you're own website API (ex: `google.py`).
+ On the source file, make sure to follow the guide below:

    ```python
    class Google:
        def __init__(self):
            self.name = "Google"

        def fetch(self, link):
            # here you fetch on the link given the information you want
            # you can check out some existing examples like kabum.py or mercadolivre.py

        def getPrice(self):
            # return the price that you've found on fetch function

        def getName(self):
            # return the name of the product that you've found on fetch function
    ```

+ Then, when you're done, go to the `src/fetcher.py` file and include on the 
header the name of your brand new API, like the following:

    ```python
    from sites.google import Google
    # sites.google = path to sites/google.py
    # Google = class name
    ```

    And then add support to your API down there:

    ```python
    # ... inside the getSiteClass(self) function
    if (self.site.lower() == "google"): # word that you will use when executing
        self.ref = Google()             # Class that you've created
    ```

# Authorship
Developed by Felipe Ramos under the **MIT License**.

##### Stats
```
version     0.2.2
```
