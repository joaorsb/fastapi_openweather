from aiohttp import ClientSession


async def get_open_weather_forecast(url: str):
    async with ClientSession() as session:
        async with session.get(url) as response:
            try:
                data = await response.text()
            except:
                return Exception

            return data
