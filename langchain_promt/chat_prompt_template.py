from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage
chat_template=ChatPromptTemplate([
    ('system',"you are hepful{domain} expert"),
    ('human',"Explain calculus in simple words what is {topic}")


])
prompt=chat_template.invoke({'domain':'student','topic':'integration'})
print(prompt)
