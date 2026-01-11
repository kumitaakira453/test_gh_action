import datetime
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
    published_at: datetime.datetime


def convert_article_to_html(article: Article) -> str:
    return f"""
            <li style="margin-bottom: 12px;">
                <a
                    href="https://zenn.dev/{article["path"]}"
                    style="
                        display: block;
                        padding: 12px 14px;
                        background-color: #f9f9f9;
                        border-radius: 6px;
                        text-decoration: none;
                        color: #000000;
                    "
                >
                    <div style="
                        font-size: 16px;
                        font-weight: 500;
                        margin-bottom: 4px;
                    ">
                        {article["title"]}
                    </div>

                    <div style="
                        font-size: 12px;
                        color: #666;
                    ">
                        <span>★ {article["liked_count"]}</span>
                        <span style="margin-left: 10px;">
                            🕒 {article["published_at"].strftime("%Y/%m/%d %H:%M")}
                        </span>
                    </div>
                </a>
            </li>
            """


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
                    published_at=datetime.datetime.fromisoformat(ra["published_at"]),
                    user=User(
                        id=ra["user"]["id"],
                        username=ra["user"]["username"],
                        name=ra["user"]["name"],
                        avatar_small_url=ra["user"]["avatar_small_url"],
                    ),
                )
            )
        return articles
