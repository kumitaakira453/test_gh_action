from src.zenn import ZennAPI, display_article

ZENN_API_BASE_URL = "https://zenn.dev/api"


def main():
    print("Hello from test-gh-action!")
    zenn_api = ZennAPI(ZENN_API_BASE_URL)
    articles = zenn_api.get_articles()
    for article in articles:
        display_article(article)


if __name__ == "__main__":
    main()
