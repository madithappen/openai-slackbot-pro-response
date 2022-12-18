import sys
import os
from flask import request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Append the 'src' directory to the system path
sys.path.append('./src')

# Import the required modules
from sanitize_input import sanitize_input as sanitize
from slackbot_webservice import ProResponseWebService
from openai_api import ProResponseOpenAI
from slack_api import SlackAPI

if __name__ == '__main__':
    # Initialize the OpenAI service using the API key from the environment variables
    ai_service = ProResponseOpenAI(
        openai_api_key = os.getenv("OPENAI_API_KEY")
    )

    # Initialize the Slackbot web service with the IP and port specified in the environment variables
    slackbot_service = ProResponseWebService(
        service_ip = os.getenv("SERVICE_IP"),
        service_port = os.getenv('SERVICE_PORT'),
        autostart = False
    )

    # Initialize the Slack API using the bot token and channel ID from the environment variables
    slack = SlackAPI(
        token=os.getenv("SLACK_BOT_TOKEN"),
        channel=os.getenv("SLACK_CHANNEL_ID")
    )


    # Custom route function for the '/pr' endpoint of the slackbot_service
    def pro_response():
        # Sanitize the input text
        text = sanitize(request.form['text'])
        # Get a response from the OpenAI service
        pro_response = ai_service.ask_openai(text) if len(text) > 6 else ''
        # Post the response to the Slack channel
        slack.post_message(pro_response)
        # Return an empty string
        return ""
    # Add the custom route function to the slackbot_service
    slackbot_service.app.add_url_rule('/pr', 'pro_response', pro_response, methods=['POST'])


    # Custom route function for the '/prr' endpoint of the slackbot_service
    def pro_response_recommendation():
        # Sanitize the input text
        text = sanitize(request.form['text'])
        # Get a response from the OpenAI service
        pro_response = ai_service.ask_openai(text) if len(text) > 6 else ''
        # Return the response with a formatted message
        return f'''
        [_Input_]: {text} \n[_Recommendation_]: {pro_response}
        '''
    # Add the custom route function to the slackbot_service
    slackbot_service.app.add_url_rule('/prr', 'pro_response_recommendation', pro_response_recommendation, methods=['POST'])

    # Run the Flask application
    slackbot_service.run()
