import openai
import random

class ProResponseOpenAI:
    def __init__(self, openai_api_key: str):
        """
        Initialize ProResponseOpenAI object with OpenAI API key.
        """
        self.openai_api_key = openai_api_key
        openai.api_key = self.openai_api_key
        self.model = 'text-davinci-003'
        self.max_tokens = 300
        self.temperature = 0
        self.n = 1
        self.top_p = 0.5
        self.stop = None
        self.frequency_penalty=0.2
        self.presense_penalty=0.2
        self.instruction = '''
        Correct user_input to standard English and make it sound friendly, curteous, and not offensive in any way. Do not try to complete a sentence.

        user_input:
        '''
        self.user_input = ''

    def ask_openai(self, user_input: str):
        """
        Query OpenAI for completion of user input.
        """
        self.user_input = user_input if user_input else ''

        # Create the question to OpenAI
        prompt_text = f'{self.instruction}\n\n{self.user_input}.'

        # Make the query to the model
        response = openai.Completion.create(
            model=self.model,
            prompt=prompt_text,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            n = self.n,
            top_p=self.top_p,
            stop=self.stop,
            frequency_penalty=self.presense_penalty,
            presence_penalty=self.presense_penalty
        )

        # Randomize answers, then select one
        answers = response['choices']
        return answers[0]['text'].split('\n')[-1]

if __name__ == '__main__':
    # Load environment variables from .env file
    import os
    from dotenv import load_dotenv
    load_dotenv()

    # Initialize ProResponseOpenAI object with OpenAI API key from environment variable
    ai = ProResponseOpenAI(
        openai_api_key=os.getenv('OPENAI_API_KEY')
    )

    # Gather user input
    user_input = input('Please enter some text: ')

    # Query OpenAI for completion of user input
    response = ai.ask_openai(user_input)

    print(response)
