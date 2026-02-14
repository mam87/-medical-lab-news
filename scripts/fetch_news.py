#!/usr/bin/env python3
import requests
import json
import feedparser
from datetime import datetime
import re

def fetch_cdc_news():
    """Fetch latest news from CDC"""
    try:
        # CDC RSS feeds
        urls = [
            "https://tools.cdc.gov/podcasts/feed.asp?feedid=183",
            "https://www.cdc.gov/media/rss.xml"
        ]
        
        news_items = []
        for url in urls:
            feed = feedparser.parse(url)
            for entry in feed.entries[:3]:  # Get top 3
                news_items.append({
                    "title": entry.title,
                    "excerpt": entry.summary[:200] + "..." if len(entry.summary) > 200 else entry.summary,
                    "source": "CDC",
                    "date": datetime.now().strftime("%d %B %Y"),
                    "tag": "outbreak",
                    "url": entry.link
                })
        return news_items
    except Exception as e:
        print(f"Error fetching CDC news: {e}")
        return []

def fetch_who_news():
    """Fetch latest news from WHO"""
    try:
        url = "https://www.who.int/rss-feeds/news-english.xml"
        feed = feedparser.parse(url)
        
        news_items = []
        for entry in feed.entries[:3]:
            news_items.append({
                "title": entry.title,
                "excerpt": entry.summary[:200] + "..." if hasattr(entry, 'summary') and len(entry.summary) > 200 else "تحديث جديد من منظمة الصحة العالمية",
                "source": "WHO",
                "date": datetime.now().strftime("%d %B %Y"),
                "tag": "tech",
                "url": entry.link
            })
        return news_items
    except Exception as e:
        print(f"Error fetching WHO news: {e}")
        return []

def fetch_fda_news():
    """Fetch latest FDA approvals"""
    try:
        # FDA RSS for device approvals
        url = "https://www.fda.gov/about-fda/contact-fda/stay-informed/rss-feeds/medical-devices/rss.xml"
        feed = feedparser.parse(url)
        
        news_items = []
        for entry in feed.entries[:2]:
            news_items.append({
                "title": entry.title,
                "excerpt": "اعتماد جديد من FDA: " + entry.title,
                "source": "FDA",
                "date": datetime.now().strftime("%d %B %Y"),
                "tag": "diagnostic",
                "url": entry.link
            })
        return news_items
    except Exception as e:
        print(f"Error fetching FDA news: {e}")
        return []

def generate_default_news():
    """Generate default news if fetching fails"""
    return [
        {
            "id": 1,
            "title": "CDC تحقق في تفشي جديد لسلمونيلا شديدة المقاومة للأدوية - فبراير 2026",
            "excerpt": "تحقق CDC وFDA في تفشي متعدد الولايات لسلمونيلا شديدة المقاومة للأدوية مرتبط بكبسولات المورينجا. المرضى في ولايات متعددة يحتاجون إلى اختبارات مخبرية متخصصة.",
            "source": "CDC",
            "sourceClass": "source-cdc",
            "date": datetime.now().strftime("%d %B %Y"),
            "tag": "outbreak",
            "tagClass": "tag-outbreak",
            "tagName": "وبائي"
        },
        {
            "id": 2,
            "title": "WHO تطلق استراتيجية 2026 للتشخيصات الرقمية في المناطق النائية",
            "excerpt": "منظمة الصحة العالمية تطلق مبادرة جديدة لعام 2026 لنشر نقاط الرعاية التشخيصية (POCT) في المناطق النائية.",
            "source": "WHO",
            "sourceClass": "source-who",
            "date": datetime.now().strftime("%d %B %Y"),
            "tag": "tech",
            "tagClass": "tag-tech",
            "tagName": "تقني"
        }
    ]

def main():
    print("Fetching latest laboratory medicine news...")
    
    all_news = []
    
    # Fetch from sources
    cdc_news = fetch_cdc_news()
    who_news = fetch_who_news()
    fda_news = fetch_fda_news()
    
    # If all fetching fails, use default
    if not cdc_news and not who_news and not fda_news:
        all_news = generate_default_news()
    else:
        # Combine and format
        id_counter = 1
        for item in cdc_news + who_news + fda_news:
            formatted = {
                "id": id_counter,
                "title": item["title"],
                "excerpt": item["excerpt"],
                "source": item["source"],
                "sourceClass": f"source-{item['source'].lower()}",
                "date": item["date"],
                "tag": item["tag"],
                "tagClass": f"tag-{item['tag']}",
                "tagName": get_tag_name(item["tag"]),
                "url": item.get("url", "#")
            }
            all_news.append(formatted)
            id_counter += 1
    
    # Save to news.json
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(all_news, f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(all_news)} news items to news.json")

def get_tag_name(tag):
    mapping = {
        "outbreak": "وبائي",
        "tech": "تقني",
        "diagnostic": "تشخيصي",
        "guideline": "إرشادات"
    }
    return mapping.get(tag, "عام")

if __name__ == "__main__":
    main()

