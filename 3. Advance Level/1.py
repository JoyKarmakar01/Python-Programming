import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Run the asynchronous function
asyncio.run(say_hello())