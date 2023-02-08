from http import HTTPStatus

import aiohttp
from clients.base import BaseClient

from src.logger import trace_config
from src.settings import API_KEY_NEWSAPI, NEWS_COUNT


class NewsClient(BaseClient):
    async def get_base_url(self) -> str:
        return "https://newsapi.org/v2/everything"

    async def _request(self, endpoint: str) -> dict | None:

        # формирование заголовков запроса
        headers = {}

        async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
            async with session.get(endpoint, headers=headers) as response:
                if response.status == HTTPStatus.OK:
                    return await response.json()
                print(f"Error: {response.status} {response.reason}")
                return None

    async def get_news(self, location: str) -> dict | None:
        """
        Получение новостей по стране

        :param location: str
        :return:
        """

        return await self._request(
            f"{await self.get_base_url()}?q={location}&apiKey={API_KEY_NEWSAPI}&pageSize={NEWS_COUNT}"
        )  # todo param
