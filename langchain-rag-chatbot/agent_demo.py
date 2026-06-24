# ==================================================
# STEP 1 : LOAD ENV VARIABLES
# ==================================================

from dotenv import load_dotenv

load_dotenv()


# ==================================================
# STEP 2 : IMPORT GEMINI MODEL
# ==================================================

from langchain_google_genai import ChatGoogleGenerativeAI


# ==================================================
# STEP 3 : IMPORT TOOL DECORATOR
# ==================================================

from langchain.tools import tool


# ==================================================
# STEP 4 : CREATE TOOL
# ==================================================
# This tool can perform mathematical calculations

@tool
def calculator(expression: str) -> str:
    """
    Performs mathematical calculations.
    Example:
    10 * 20
    100 + 50
    """

    return str(eval(expression))


# ==================================================
# STEP 5 : LOAD GEMINI MODEL
# ==================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

print("✅ Gemini Loaded")


# ==================================================
# STEP 6 : BIND TOOL TO GEMINI
# ==================================================
# Now Gemini knows calculator exists

llm_with_tools = llm.bind_tools(
    [calculator]
)

print("✅ Calculator Tool Connected")


# ==================================================
# STEP 7 : ASK QUESTION
# ==================================================

question = "What is 345 * 678?"

print("\nQuestion:")
print(question)


# ==================================================
# STEP 8 : GEMINI DECIDES WHETHER TOOL IS NEEDED
# ==================================================

response = llm_with_tools.invoke(question)


# ==================================================
# STEP 9 : PRINT TOOL CALLS
# ==================================================

print("\nTool Calls:")

print(response.tool_calls)


# ==================================================
# STEP 10 : PRINT RAW RESPONSE
# ==================================================

print("\nRaw Response:")

print(response)