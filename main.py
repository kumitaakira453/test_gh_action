from src.email_notification import EmailNotification
from src.zenn import ZennAPI, convert_article_to_html

ZENN_API_BASE_URL = "https://zenn.dev/api"
NOTIFICATION_EMAIL = "akirakumi.0815@gmail.com"
NOTIFICATION_TITLE = "[Zenn]記事一覧"


def main():
    print("start")
    zenn_api = ZennAPI(ZENN_API_BASE_URL)
    articles = zenn_api.get_articles()
    formatted_articles = [convert_article_to_html(article) for article in articles]
    email_notification = EmailNotification(
        NOTIFICATION_EMAIL,
        NOTIFICATION_TITLE,
        "\n".join(formatted_articles),
    )
    email_notification.notify()


if __name__ == "__main__":
    main()
