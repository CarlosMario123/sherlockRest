import asyncio
from sherlock_lib import search_target

async def searchUser(username):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, search_target, username)
    return result
