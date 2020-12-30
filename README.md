# Python Uptime Watcher
> Monitor websites for a 200 status. Get a text from Twilio when a non-200 status code is reported.

## Installation
```
pipenv install
pipenv shell
```

Rename the `.env.example` file to `.env`.

Then put one website URL per line on `websites.txt`. You can see mine as an example.

## Twilio
- [ ] You need a Twilio account. It's free to sign up. Make sure you verify your phone number and email address.
- [ ] You need a Twilio phone number. They'll say you need to pay $1.00 but you can use their free trial for a while.
- [ ] You need your Twilio SID, Auth token, and to set the TO and FROM variables in your `.env` file.


## Running the script
- [ ] Make sure you have one website per line in websites.txt
- [ ] Run `python watcher.py`
- [ ] Check `log.txt` for details on each website

## License
Do as you please. ¯\_(ツ)_/¯
