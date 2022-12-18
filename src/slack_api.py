import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Import sanitize function from sanitize module
from sanitize_input import sanitize_input as sanitize

class SlackAPI:
    def __init__(self, token: str='', channel: str='') -> None:
        """
        Initialize SlackAPI object with token and channel.
        """
        self.token = token
        self.channel = channel
        self.client = WebClient(token=self.token)

    def post_message(self, input: str) -> None:
        """
        Post message to Slack channel.
        """
        try:
            # Re-post the text in the chat as if it's the author
            self.client.chat_postMessage(
                channel=self.channel,
                text=input
            )
        except SlackApiError as e:
            print(e)


if __name__ == '__main__':
    # Load environment variables from .env file
    from dotenv import load_dotenv
    load_dotenv()

    # Initialize SlackAPI object with bot token and channel ID from environment variables
    slack = SlackAPI(
        token=os.getenv("SLACK_BOT_TOKEN"),
        channel=os.getenv("SLACK_CHANNEL_ID")
    )

    # Sanitize input and post message to Slack channel
    sanitized_input = sanitize("CXCc3##")
    slack.post_message(sanitized_input)
