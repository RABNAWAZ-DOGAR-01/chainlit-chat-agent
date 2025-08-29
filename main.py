import chainlit as cl
from decouple import config 
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner , set_tracing_disabled

set_tracing_disabled(True)

key = config("GEMINI_API_KEY")
base_url = config("BASE_URL")

gemini_client = AsyncOpenAI(api_key=key, base_url=base_url)
model = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client)
agent = Agent(
    name="Rabnawaz Dogar Frontend Developer",
    instructions="""
tuhm coding ma expert ho ager coding ka topics sa bihr bih kio question kara to ossa answer da dana 
""",
    model=model
)

@cl.on_message
async def main(message: cl.Message):
    result = await Runner.run(starting_agent=agent, input=message.content)
    await cl.Message(content=result.final_output).send()
