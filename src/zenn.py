from typing import Any, Iterable, TypedDict

import requests

ZENN_API_BASE_URL = "https://zenn.dev/api"


class User(TypedDict):
    id: str
    username: str
    name: str
    avatar_small_url: str


class Article(TypedDict):
    id: str
    slug: str
    title: str
    liked_count: int
    user: User
    path: str


def display_article(article: Article) -> None:
    print(
        f"- [{article['title']}](https://zenn.dev/{article['path']})({article['liked_count']})"
    )


class ZennAPI:
    articles = "articles"

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get_articles(self) -> Iterable[Article]:
        res = requests.get(f"{self.base_url}/{self.articles}")
        res.raise_for_status()
        return self._convert_articles(res.json()["articles"])

    def _convert_articles(
        self, raw_articles: list[dict[str, Any]]
    ) -> Iterable[Article]:
        articles: list[Article] = []
        for ra in raw_articles:
            articles.append(
                Article(
                    id=ra["id"],
                    slug=ra["slug"],
                    title=ra["title"],
                    liked_count=ra["liked_count"],
                    path=ra["path"],
                    user=User(
                        id=ra["user"]["id"],
                        username=ra["user"]["username"],
                        name=ra["user"]["name"],
                        avatar_small_url=ra["user"]["avatar_small_url"],
                    ),
                )
            )
        return articles
