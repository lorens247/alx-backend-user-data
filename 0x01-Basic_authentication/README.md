# 0x01. Basic Authentication

## Introduction
This project explores the concept of basic authentication, including what authentication means, Base64 encoding, and how to implement basic authentication using the Authorization header.

## Authentication
Authentication is the process of verifying the identity of a user or entity. It ensures that the user or entity is who they claim to be before granting access to resources or services.

## Base64 Encoding
Base64 is a binary-to-text encoding scheme that converts binary data into ASCII characters. It is commonly used to encode binary data, such as images or cryptographic keys, into a format that can be safely transmitted over text-based protocols, such as HTTP.

## Encoding a String in Base64
To encode a string in Base64, you can use built-in functions or libraries available in most programming languages. For example, in Python, you can use the `base64` module:

## Sending the Authorization Header in Python
To send basic authentication credentials in Python, you can use the `requests` library. Here's an example of how to send an HTTP request with basic authentication:

```python
import requests

# Define the URL and credentials
url = 'https://example.com/api/resource'
username = 'username'
password = 'password'

# Encode the credentials in Base64
credentials = f"{username}:{password}"
encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

# Set up the Authorization header
headers = {'Authorization': f'Basic {encoded_credentials}'}

# Send the HTTP GET request with basic authentication
response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    print('Request successful!')
    print('Response:', response.text)
else:
    print('Request failed:', response.status_code)
