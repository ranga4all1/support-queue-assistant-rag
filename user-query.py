import requests

# Prompt the user for a question
user_question = input("Please enter your question: ")

# Service URL
url = "http://localhost:5000/question"

# Prepare the data with the user's question
data = {"question": user_question}

# Send the request
response = requests.post(url, json=data)

# Print the response from the service
try:
    response_data = response.json()  # Parse the JSON response
    print("Response: ", response_data)
except ValueError:
    print("Failed to decode JSON response. Raw response: ", response.text)
