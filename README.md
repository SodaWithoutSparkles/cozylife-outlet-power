# cozylife-outlet-power
Small python script to get information from cozylife outlets

## How to use
Replace the host variable to the IP of your cozylife outlet.

## FAQ
### What are the attributes? Where are the other attributes?
I found the available attributes by brute-forcing all numbers from 0-28. Are there anything else? probably, but I am too lazy to reverse-engineer it.

### What does the attributes mean?
I can only be certain that attribute 28 means "real time wattage". This was confirmed by experiment and officially confirmed by cozylife in one of the [PRs](https://github.com/cozylife/hass_cozylife_local_pull/pull/35#issuecomment-2047188529)


