import sys
import warnings
import os
from openai import OpenAI
from keyword_extraction import keygen


def generate_summary(input_data):
    warnings.filterwarnings("ignore")
    OPENAI_API_KEY="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"
    client = OpenAI(
        api_key=OPENAI_API_KEY)
    keywords = keygen(str(input_data))
    prompt = f'''
    {keywords}

    Using the above information, generate a short 1-2 lines of description, and make sure that the description generated has most of the text from the above information provided. Keep the description very professional
    '''

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.1,
        max_tokens=100
    )
    # print(response.choices[0].text.strip())

    return response.choices[0].text.strip()


# Example usage:
# input_data = sys.argv[1]
# summary = generate_summary(input_data)
# print(summary)
