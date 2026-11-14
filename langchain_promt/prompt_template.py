from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

# Define template
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# Fill in the variable
prompt = template2.invoke({'name': 'Sujit'})

# Send to Gemini
result = model.invoke(prompt)

# Print response
print(result.content)
