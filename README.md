# Price Calculator

This project aims to generate simple log containing current prices on a given list
of products (and their sum).

# Dependencies
In order to execute this project, you're going to need `python3` installed onto
your computer, and the following dependencies:
+ `urllib2`
+ `re`

## Execution
First, you'll prepare the ambient with `make`. Then, to execute, just open the 
project folder on your favorite terminal and type:
```bash
python3 pcalc [file-with-links] [kabum/mercadolivre]
# file-with-links = A simple txt file containing one link per line.
# kabum/mercadolivre = The fetcher that you will use (at the moment, only these)
```
### Use examples
Let's say i have a file on `configs/test.txt`, and inside of it, i have:
```
https://produto.mercadolivre.com.br/MLB-1146730903-amd-ryzen-2700x-am4-43ghz-octa-core-16theads-rgb-lacrado-_JM
https://produto.mercadolivre.com.br/MLB-1024669523-adaptador-ativo-displayport-p-hdmi-20-4k-60hz-club3d-uhd-_JM#reco_item_pos=2&reco_backend=machinalis-seller-items&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=3f6356d6-c593-4365-a9e6-91122a156cba
https://produto.mercadolivre.com.br/MLB-960954066-memoria-kingston-hyperx-fury-8gb-2400mhz-ddr4-gamer-cl15-_JM#reco_item_pos=2&reco_backend=mp2v-combos-v3&reco_backend_type=low_level&reco_client=vip_combo&reco_id=eda13a9f-bdb7-4696-9425-a73a95d150f9
```
I could run the program by typing the following commands:
```bash
./pcalc.py configs/test.txt mercadolivre
```

# Authorship
Developed by Felipe Ramos under the **MIT License**.
