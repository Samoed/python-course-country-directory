from clients.base import BaseClient

from settings import API_KEY_NEWSAPI, NEWS_COUNT


class NewsClient(BaseClient):
    params = {"apiKey": API_KEY_NEWSAPI, "pageSize": NEWS_COUNT}

    async def get_base_url(self) -> str:
        return "https://newsapi.org/v2/everything"

    async def get_news(self, location: str) -> dict | None:
        """
        Получение новостей по стране

        :param location: str
        :return:
        """
        self.params["q"] = location
        return await self._request(await self.get_base_url())
