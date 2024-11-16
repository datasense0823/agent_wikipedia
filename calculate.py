from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.tools import Tool

# Define an LLM-powered calculator tool
def llm_calculator(query):
    """
    Uses an LLM to process a mathematical query dynamically.
    """
    llm = ChatOpenAI(temperature=0, model="gpt-4")
    prompt_template = PromptTemplate(
            input_variables=["question"],
            template=(
                "You are a math assistant. Process the following operation and return only the final result:\n"
                "{question}\n"
            )
        )
    
    chain=prompt_template | llm
    result=chain.invoke({"question":query})

    return result.content

# Convert Function to Tools
calculator_tool =Tool(
            name="LLM Calculator",
            func=llm_calculator,
            description="Use this tool to perform dynamic calculations or mathematical operations"
        )

   



