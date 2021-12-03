import aiohttp

session: aiohttp.ClientSession = aiohttp.ClientSession()


async def close_aiohttp_session():
    global session
    session = await session.close()
