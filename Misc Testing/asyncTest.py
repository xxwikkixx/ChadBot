import asyncio
import time
import random

END_OF_QUEUE = "This is the end..."

async def producer(queue):
    while True:
        # emit_me = random.randint(1, 42)
        emit_me = 42
        # if emit_me == 42:
        #     print("At the end")
        #     break
        # else:
        msg = f"Emitting {emit_me}"
        print(msg)
        # simulate some IO time
        await asyncio.sleep(random.uniform(0, 0.5))
        await queue.put(msg)


async def consumer(queue):
    message = await queue.get()
    # if message == END_OF_QUEUE:
    #     print(f"This is the end my friend....")
    #     break
    print(f"Got message: {message}")
    # simulate some IO time
    await asyncio.sleep(random.uniform(0, 1.0))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()
    loop.run_until_complete(asyncio.gather(producer(queue), consumer(queue)))
    loop.close()


# async def hello_world():

#     await asyncio.sleep(1)
#     print('Hello World')
#     await good_evening()


# async def good_evening():

#     await asyncio.sleep(1)
#     print('Good Evening')
#     await hello_world()


# loop = asyncio.get_event_loop()

# try:

#     loop.run_until_complete(hello_world())
#     loop.run_until_complete(good_evening())
#     loop.run_forever()

# finally:

#     print('closing event loop')
#     loop.close()