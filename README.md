# cozylife-outlet-power
Small python script to get information from cozylife outlets

## How to use
Replace the host variable to the IP of your cozylife outlet. Run the script with python3. 

## FAQ
### What are the attributes? Where are the other attributes?
I found the available attributes by brute-forcing all numbers from 0-28. Are there anything else? probably, but I am too lazy to reverse-engineer it.

### What does the attributes mean?
I can only be certain that attribute 28 means "real time wattage". This was confirmed by experiment and officially confirmed by cozylife in one of the [PRs](https://github.com/cozylife/hass_cozylife_local_pull/pull/35#issuecomment-2047188529).

### How to use with Home Assistant?
You can use the [command line sensor](https://www.home-assistant.io/integrations/command_line/) component. Examples are in the `ha.yaml` file.

### How to get the energy usage in Home Assistant?
Use the [Riemann sum integral](https://www.home-assistant.io/integrations/integration/) helper. 

### Code is ugly.
Feel free to PR `¯\_(ツ)_/¯` 

### Where are the EXEs (:P)?
Are you serious?

## LICENSE
MIT Licensed. Contains code heavily modified from [StackOverflow](https://stackoverflow.com/a/34655152/9566810)
