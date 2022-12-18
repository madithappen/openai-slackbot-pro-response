from setuptools import setup, find_packages

setup(
    name='ProResponseSlackbot',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'sys',
        'os',
        'request',
        'load_dotenv',
        'Flask',
        'WebClient',
        'SlackApiError',
        're',
        'html',
        'openai',
        'random',
    ],
)
