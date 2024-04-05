from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import Home


@shared_task()
def celery_task():
    print("start test")
    result = requests.get("https://www.olx.uz/nedvizhimost/kvartiry/").text
    doc = BeautifulSoup(result, "html.parser")

    list_cards = doc.find(attrs={"class": "listing-grid-container"})
    for cards in list_cards.find_all(attrs={"type": "list"}):
        # Home.objects.create(content=cards.text)
        print(cards.text)

    # print("end test")

