Yes, you can set up AWS Bedrock LLM (Large Language Model) with the key, secret, and region as environment variables and use a Python notebook for your proof of concept (PoC) without relying on AWS CLI or extensions. To interact with AWS services like Bedrock, you'll use the `boto3` library, which is the official AWS SDK for Python.

Here’s how you can go about it:

### Steps:

1. **Set up AWS credentials as environment variables**:
   You can set up your AWS credentials in the environment variables for authentication:

   * `AWS_ACCESS_KEY_ID`
   * `AWS_SECRET_ACCESS_KEY`
   * `AWS_DEFAULT_REGION`

   Set these environment variables in your terminal or within your notebook environment:

   ```bash
   export AWS_ACCESS_KEY_ID="your_access_key"
   export AWS_SECRET_ACCESS_KEY="your_secret_key"
   export AWS_DEFAULT_REGION="your_region"
   ```

   Or, inside your notebook, you can set them programmatically like so:

   ```python
   import os

   os.environ["AWS_ACCESS_KEY_ID"] = "your_access_key"
   os.environ["AWS_SECRET_ACCESS_KEY"] = "your_secret_key"
   os.environ["AWS_DEFAULT_REGION"] = "your_region"
   ```

2. **Install the necessary dependencies**:
   In your Python notebook, you'll need to install the `boto3` library to interact with AWS services:

   ```bash
   !pip install boto3
   ```

3. **Initialize the AWS Bedrock client**:
   AWS Bedrock provides APIs for interacting with large language models. Using `boto3`, you can set up the client for Bedrock.

   ```python
   import boto3

   # Create a Bedrock client
   bedrock_client = boto3.client('bedrock')
   ```

4. **Interact with Bedrock LLM**:
   You can call the Bedrock service to interact with the LLM models by passing the necessary input to the API methods. AWS Bedrock supports multiple models (like Jurassic-2, etc.).

   Example of making a request to the Bedrock service:

   ```python
   response = bedrock_client.invoke_model(
       ModelId='your_model_id',  # The model you want to use
       Body="Your input text here",  # The text you want to send to the model
       ContentType="application/json"
   )

   # Print the response from the model
   print(response)
   ```

5. **Handle the response**:
   After invoking the model, you’ll receive a response containing the generated output, which you can process further.

   Example of extracting and printing the result:

   ```python
   output = response['Body'].read().decode('utf-8')
   print(output)
   ```

### Notes:

* **API and Model Selection**: Make sure you have access to the specific LLM model within AWS Bedrock.
* **Permissions**: Ensure that your AWS credentials have the necessary permissions to invoke the Bedrock APIs.
* **Response Parsing**: Depending on the model's output format, you may need to adjust the response parsing.

This setup should work well for a PoC where you're testing AWS Bedrock in a Python notebook without needing to depend on AWS CLI or extensions.
