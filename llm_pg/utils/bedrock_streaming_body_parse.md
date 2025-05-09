Yes, when using **AWS Bedrock**, the `response['body']` is typically a `StreamingBody`, so you'll need to read and decode it before parsing the JSON.

Here's a function to extract the parsed JSON body from a Bedrock response:

```python
import json

def parse_bedrock_response(response):
    """
    Reads and parses a Bedrock StreamingBody response into a Python dict.
    """
    try:
        body = response['body'].read().decode('utf-8')
        return json.loads(body)
    except (KeyError, AttributeError, json.JSONDecodeError) as e:
        print(f"Error parsing response: {e}")
        return None
```

### Usage:

```python
# response = bedrock_client.invoke_model(...) or similar
parsed_body = parse_bedrock_response(response)

# Optionally extract text if needed:
if parsed_body:
    text = extract_text(parsed_body)
    print(text)
```

Let me know if you'd like to handle chunked streaming (for models like Claude or Titan that support streaming inference).
