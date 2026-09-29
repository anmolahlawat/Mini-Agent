import requests
from ollama import chat


# ---------------- TOOLS ----------------

def add(a: int, b: int):
    return a + b


def multiply(a: int, b: int):
    return a * b


def get_weather(city: str):
    """Get current weather for a city."""

    # Step 1: City → coordinates
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_response = requests.get(
        geo_url,
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }
    )

    geo_data = geo_response.json()

    if "results" not in geo_data:
        return f"Could not find the city: {city}"

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    # Step 2: Coordinates → weather
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_response = requests.get(
        weather_url,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,weather_code",
            "timezone": "auto"
        }
    )

    weather_data = weather_response.json()
    current = weather_data["current"]

    return {
        "city": city,
        "temperature": current["temperature_2m"],
        "humidity": current["relative_humidity_2m"],
        "weather_code": current["weather_code"]
    }


# ---------------- TOOL MAPPING ----------------

tools = {
    "add": add,
    "multiply": multiply,
    "get_weather": get_weather
}


# ---------------- CONVERSATION ----------------

messages = [
    {
        "role": "system",
        "content": """
You are a helpful AI agent.

You have access to tools.

Use a tool whenever it is necessary to answer the user's request.
After receiving a tool result, decide whether you need another tool
or whether you can provide the final answer.
"""
    }
]


# ---------------- AGENT ----------------

while True:

    user_input = input("\nUser: ")

    if user_input.strip().lower() == "exit":
        print("Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    # Agent loop
    while True:

        response = chat(
            model="qwen3:4b",
            messages=messages,
            tools=[add, multiply, get_weather]
        )

        # Add LLM response to conversation
        messages.append(response.message)

        # No tool call → final answer
        if not response.message.tool_calls:
            print("Agent:", response.message.content)
            break

        # Tool calls → execute them
        for tool_call in response.message.tool_calls:

            function_name = tool_call.function.name
            args = tool_call.function.arguments

            print(f"[Agent is using tool: {function_name}]")

            if function_name not in tools:
                result = f"Unknown tool: {function_name}"
            else:
                function = tools[function_name]
                result = function(**args)

            # Send tool result back to LLM
            messages.append({
                "role": "tool",
                "content": str(result)
            })