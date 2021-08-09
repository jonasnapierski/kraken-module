# Kraken-module for Leni
Leni-PY or just [Leni](https://github.com/zirkumflexlab/leni-py) is a home assistant backend. Based on Flask it is designed to quickly extend your own assistant with simple Python **modules**.

This module uses the [Kraken](https://docs.kraken.com/rest/) API to get cryptocurrency prices and show information of your Kraken account.
## Installing
To use this module you first need to install [Leni](https://github.com/zirkumflexlab/leni-py) and follow the instructions there.
## Use
If you only want to use the module to request public data, then you dont need an [API keypair](https://support.kraken.com/hc/en-us/articles/360000919966-How-to-generate-an-API-key-pair-). But  if you want to acsess private data form your account, you will need one.
Then you have to copy that keypair into the *kraken-module.json* file in the *config* folder.

Now the module can be used.

Currently you can request your account balance and the price of the cryptocurrencys available on Kraken.
