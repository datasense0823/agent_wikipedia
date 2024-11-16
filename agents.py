import os
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from tools.calculate import calculator_tool
from tools.wiki import wikipedia_tool
load_dotenv()

def lookup(user_question: str) -> str:
    """
    Processes the user query using an agent that combines Wikipedia and calculator tools.
    """
    llm = ChatOpenAI(temperature=0, model_name="gpt-4")

    tools = [wikipedia_tool, calculator_tool]

    # Pull the React prompt from LangChain hub
    react_prompt = hub.pull("hwchase17/react")

    # Template for generating user query prompt
    template = "Given the user question '{input}', answer it completely. Make sure the question is answered completely."
    prompt_template = PromptTemplate(template=template, input_variables=["input"])

    # Format the input question using the template
    formatted_input = prompt_template.format(input=user_question)

    # Create the React agent
    agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)
    
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Invoke the agent to process the user query
    result = agent_executor.invoke(
        input={"input": formatted_input}
    )
    # Return the result content
    return result
print(lookup("What % of indian people live in USA"))



