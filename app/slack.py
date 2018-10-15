from slackclient import SlackClient
import os

zappy_token = "xoxp-455111924899-455032727220-455010954273-dae9a01702ef012cbc747fa3f3590b8c"
token = os.environ.get(zappy_token)
slack_client = SlackClient(token)

if slack_client.rtm_connect():
    # proceed
    while True:
        events = slack_client.rtm_read()
        for event in events:
            if (
                'channel' in event and
                'text' in event and
                event.get('type') == 'message'
            ):
                channel = event['channel']
                text = event['text']
                if 'go' in text.lower():
                    print("collect tweets")
                    # slack_client.api_call(
                    #     'chat.postMessage',
                    #     channel=channel,
                    #     text=link,
                    #     as_user='true:'
                    # )
        time.sleep(1)
else:
    print('Connection failed, invalid token?')