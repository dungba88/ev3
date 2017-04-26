"""Trigger implementation for inquiring interest"""

from app import APP_INSTANCE as app
from utils import tts

def run(execution_context):
    """run the action"""
    interests = app.get_config('facts.tokenized_interests')
    tagged_text = execution_context.event.get('tagged_text')
    has_interest_react = app.get_config('behavior.interest_react.yes')
    no_interest_react = app.get_config('behavior.interest_react.no')

    for word in tagged_text:
        if word[1] == 'JJ' or word[1] == 'NN':
            if word[0] in interests:
                execution_context.finish('yes')
                tts.say_random(has_interest_react)
                return

    execution_context.finish('no')
    tts.say_random(no_interest_react)