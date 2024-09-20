import logging
import azure.functions as func
from openai import AzureOpenAI
#from GenerateTextFunction import generate_text_on_topic

client = AzureOpenAI(
            api_version = "2024-02-15-preview",
            azure_endpoint = "https://demoazureai6064269374.openai.azure.com/",
            api_key = "a2af6b0615c54002bb66474dccd832c6"
            )

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')  
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        Topic = generate_text_on_topic(name)
        logging.info(Topic)
        #print(Topic)
        return func.HttpResponse(f"Let’s crack a joke about {name}!: {Topic}")
        #return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a Topic to generate a jokes.",
             status_code=200
        )

def generate_text_on_topic(topic: str) -> str:
    # Ensure the OpenAI API key is set
    #openai.api_key = "b00f1602be9f435fbc423597af147e21"
    
    # Define the prompt for the OpenAI model
    prompt = f"Write a joke on this topic: {topic}"
    
    # Call the OpenAI API to generate text
    #prompt = {resume_text}
    messages = [
            {"role": "system", "content": "You are a helpful assistant.how can generate a joke for you"},
            {"role": "user", "content":f'{prompt}'}]
    response = client.chat.completions.create(
            model="gpt-4o-funcion",
            messages = messages,
            temperature=0.5,
            max_tokens=400,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None)
    # #text = response.choices[0].message.content
    
    # Extract the generated text from the response
    generated_text = response.choices[0].message.content    
    #generated_text = f"generate_text_on_topic > Generate a topic on {topic}"   
    return generated_text