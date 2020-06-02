# Wishlist Scrape
This project aims to generate simple log files containing current prices on items from your
wishlist (and their sum).

## Dependencies
This project makes use of the following `python3` libs:
+ `urllib`
+ `re`
+ `json`
+ `datetime`
+ `threadings`
+ `sys`
+ `os`
+ `bs4`

## Execution
Just follow the steps:
1. `make`
2. `./wcalc -l path/to/file/with/links -o output/file/directory`

```
usage: wcalc.py [-h] -l list.txt [-o output_file.txt] [-T]

optional arguments:
  -h, --help            show this help message and exit
  -l list.txt           List of products (one link per line)
  -o output_file.json   Output fetched prices
  -T, --no-threading    Disable parallel fetches
```

### Use examples
Let's say that i have a file on `lists/test.txt` with this inside:
```
https://produto.mercadolivre.com.br/MLB-1146730903-amd-ryzen-2700x-am4-43ghz-octa-core-16theads-rgb-lacrado-_JM
https://produto.mercadolivre.com.br/MLB-1024669523-adaptador-ativo-displayport-p-hdmi-20-4k-60hz-club3d-uhd-_JM
https://produto.mercadolivre.com.br/MLB-960954066-memoria-kingston-hyperx-fury-8gb-2400mhz-ddr4-gamer-cl15-_JM
```
I could run the program by typing the following commands:
```bash
./wcalc lists/test.txt logs
```
And then, the program will automatically see the domain on the links and select
the right API for that site.

### Supported Websites
At the moment, the `API` only extends to the following websites:
+ `mercadolivre`
+ `kabum`
+ `terabyteshop` (not stable)

# Creating your custom API
I've designed this script to be as modular as you want. So with that in mind, 
just need some little coding to make this script adapt to your desired website.

You'll need basic knowledge in `re` and `python3` in order to create your own
API.

With that in mind, follow these steps:
+ Navigate to `src/sites` and create your own website API (ex: `google.py`)
+ On the source file, follow the guide below:

    ```python3
    class Google:
        def fetch(self, link):
            # Here you fetch on the link given the information you want
            # then, after fetched, return a dictionary with the following
            # keys:
            # dict['title'] -> product title, need to be a String
            # dict['price'] -> product price, need to be a Float
    ```

+ Then, go to `src/sites/api.py` and include on the header an import to your API,
like this:
    
    ```python3
    from sites.google import Google
    #          ^your file    ^your class
    ```

+ And then, add support to your API down there:
    
    ```python3
    # Possible domains and it's correspondent API's
        domains = {
            'kabum.com.br': Kabum,
            'terabyteshop.com.br': Terabyte,
            'mercadolivre.com.br': ML,
            'google.com.br': Google,            # ADD THIS LINE
    }
    ```

+ Test your API and feel free to make a Pull Request!

# Authorship
Developed by Felipe Ramos under the **MIT License**

###### Stats
```
version     0.2.4
```
