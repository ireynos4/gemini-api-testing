
from google import genai

# Connect to Gemini using your environment variable
client = genai.Client()

# Test 1: Send a request to Gemini
print("Test 1: Testing Gemini API connection...")

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Say hello in one sentence."
    )

    if response.text:
        print("PASS: Gemini returned a response!")
        print("Response:", response.text)
    else:
        print("FAIL: Gemini returned an empty response.")

except Exception as error:
    print("FAIL: API request failed.")
    print("Error:", error)


# Test 2: Verify Gemini returns the expected information
print("\nTest 2: Checking API response data...")

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Respond with exactly this word: SUCCESS"
    )

    if response.text and response.text.strip() == "SUCCESS":
        print("PASS: Gemini returned the expected response!")
    else:
        print("FAIL: Unexpected response.")
        print("Received:", response.text)

except Exception as error:
    print("FAIL: API request failed.")
    print("Error:", error)



# Test 3: Verify token usage information
print("\nTest 3: Checking token usage...")

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="What is 2 + 2?"
    )

    usage = response.usage_metadata

    if usage and usage.total_token_count is not None:
        print("PASS: Token usage information returned!")
        print("Input tokens:", usage.prompt_token_count)
        print("Output tokens:", usage.candidates_token_count)
        print("Total tokens:", usage.total_token_count)
    else:
        print("FAIL: Token usage information missing.")

except Exception as error:
    print("FAIL: API request failed.")
    print("Error:", error)



# Test 4: Verify API error handling
print("\nTest 4: Checking error handling...")

try:
    response = client.models.generate_content(
        model="invalid-model-12345",
        contents="Hello"
    )

    print("FAIL: Expected an error but request succeeded.")

except Exception as error:
    if getattr(error, "code", None) == 404:
        print("PASS: API correctly rejected invalid model!")
        print("Error code: 404")
    else:
        print("FAIL: Unexpected error.")
        print("Error:", error)

# Test 5: Ask Gemini a question
print("\nTest 5: Asking Gemini a question...")

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="What is the most famous short poem? Give its title, author, and a brief explanation."
    )

    if response.text:
        print("PASS: Gemini answered the question!")
        print("Gemini's response:")
        print(response.text)
    else:
        print("FAIL: Gemini returned an empty response.")

except Exception as e:
    print("FAIL: API request failed.")
    print("Error:", e)