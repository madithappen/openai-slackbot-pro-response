from flask import Flask

class ProResponseWebService:
    def __init__(self, service_ip: str='127.0.0.1', service_port: str='8123', autostart: bool=True) -> None:
        """
        Initialize ProResponseWebService object with service IP, service port, and autostart flag.
        """
        self.service_ip = service_ip
        self.service_port = service_port
        self.autostart = autostart
        self.app = Flask(__name__)
        self.add_routes()
        if self.autostart:
            self.run()

    def run(self) -> None:
        """
        Run Flask app.
        """
        self.app.run(
            host=self.service_ip,
            port=self.service_port
        )

    def add_routes(self) -> None:
        """
        Add default routes to Flask app.
        """
        self.app.add_url_rule('/ping', 'ping', self.ping, methods=['GET'])

    def ping(self) -> str:
        """
        Return 'pong' for '/ping' route.
        """
        return 'pong'


if __name__ == '__main__':
    # Initialize ProResponseWebService object with default values
    slackbot = ProResponseWebService()

    # Example usage with custom IP, port, and route
    #
    # import os
    # from dotenv import load_dotenv
    # load_dotenv()
    # from flask import request
    #
    # # Initialize ProResponseWebService object with custom values
    # slackbot = ProResponseWebService(
    #     service_ip=os.getenv("SERVICE_IP"),
    #     service_port=os.getenv('SERVICE_PORT'),
    #     autostart=False
    # )
    #
    # # Custom route function
    # def pro_response():
    #     text = sanitize(request.form['text'])
    #     return f'pong: {text}'
    #
    # # Add custom route to Flask app
    # slackbot.app.add_url_rule('/pr', 'pro_response', pro_response, methods=['POST'])
    #
    # # Run Flask app
    # slackbot.run()
