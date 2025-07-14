import requests
from django.conf import settings

def search_aliexpress_products(query, page=1):
    url = "https://aliexpress-datahub.p.rapidapi.com/item_search_2"
    headers = {
        "X-RapidAPI-Key": settings.RAPIDAPI_KEY,
        "X-RapidAPI-Host": "aliexpress-datahub.p.rapidapi.com"
    }
    params = {
        "q": query,
        "page": str(page),
        "sort": "default"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        raw_results = response.json().get("result", {}).get("resultList", [])
        clean_products = []
        for r in raw_results:
            item = r.get("item", {})
            clean_products.append({
                "title": item.get("title"),
                "image": "https:" + item.get("image", ""),
                "price": item.get("sku", {}).get("def", {}).get("promotionPrice"),
                "url": "https:" + item.get("itemUrl", ""),
            })
        return clean_products
    return []
