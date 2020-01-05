# mastodon-crier-bot
Mastodon bot that posts your instance's public stadistics (number of published posts, users and connections with other instances)

## Usage

1. Change the access token and API base URL to your API key and instance's URL.
2. Install dependencies running
  ```
    pip3 install -r requirements.txt
  ```
3. Set a cronjob to execute the `main.py` script everytime you want (I'm running it every 2h) 

## Hacking the bot

You can write your own post template and change whatever you need about the stadistics. See `Mastodon.py` docs to see what more can your bot do.

## Production example

I'm running this bot on [hispatodon.club](https://hispatodon.club/@pregonero) in order to show how the network is growing up.

## License

MIT license, do whatever you want.
