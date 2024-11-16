from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
# Create Function
def search_wikipedia(query: str) -> str:
    """
    Runs a query on Wikipedia using WikipediaQueryRun.

    Args:
        query (str): The query to search on Wikipedia.

    Returns:
        str: The result from Wikipedia.
    """
    # Initialize the Wikipedia API Wrapper
    api_wrapper = WikipediaAPIWrapper()

    # Pass the API Wrapper to the WikipediaQueryRun tool
    wikipedia = WikipediaQueryRun(api_wrapper=api_wrapper)

    # Run the query and return the result
    return wikipedia.run(query)


# Convert Function to Tools
wikipedia_tool =Tool(
            name="Search Wikipedia",
            func=search_wikipedia,
            description="useful for when you need to search wikipedia for information"
        )


