# API keys configuration
import os

API_KEYS = {
    'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
    'STABILITY_API_KEY': os.getenv('STABILITY_API_KEY')
}

# Verify API keys are loaded
if not all(API_KEYS.values()):
    raise ValueError("Missing API keys. Please set OPENAI_API_KEY and STABILITY_API_KEY environment variables.") 