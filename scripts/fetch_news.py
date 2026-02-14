#!/usr/bin/env python3
import json
from datetime import datetime
import random

def generate_daily_news():
    """Generate daily news from static sources"""
    
    news_database = [
        {
            "title": "CDC تحقق في تفشي جديد لسلمونيلا شديدة المقاومة للأدوية",
            "excerpt": "تحقق CDC وFDA في تفشي متعدد الولايات لسلمونيلا شديدة المقاومة للأدوية مرتبط بكبسولات المورينجا. المرضى في ولايات متعددة يحتاجون إلى اختبارات مخبرية متخصصة.",
            "source": "CDC",
            "tag": "outbreak"
        },
        {
            "title": "WHO تطلق استراتيجية 2026 للتشخيصات الرقمية في المناطق النائية",
            "excerpt": "منظمة الصحة العالمية تطلق مبادرة جديدة لعام 2026 لنشر نقاط الرعاية التشخيصية (POCT) في المناطق النائية مع ربط النتائج إلكترونياً.",
            "source": "WHO",
            "tag": "tech"
        },
        {
            "title": "FDA تعتمد اختبار HbA1c جديد من Tosoh في 50 ثانية فقط",
            "excerpt": "حصلت Tosoh Bioscience على موافقة FDA 510(k) لمحلل HLC-723 GR01 الجديد لفحص السكر التراكمي بدقة عالية.",
            "source": "FDA",
            "tag": "diagnostic"
        },
        {
            "title": "تخفيضات Medicare تصل إلى 15% تهدد المختبرات الطبية في 2026",
            "excerpt": "سارية المفعول: تخفيضات تصل إلى 15% في تعويضات Medicare للمختبرات بموجب قانون PAMA.",
            "source": "CMS",
            "tag": "guideline"
        },
        {
            "title": "60% من كوادر المختبرات مؤهلة للتقاعد في 2026",
            "excerpt": "تحذير عاجل: وفقاً لجمعية ASCLS، سيصل 60% من workforce المختبرات الطبية إلى سن التقاعد بحلول 2026.",
            "source": "ASCLS",
            "tag": "tech"
        },
        {
            "title": "الذكاء الاصطناعي يتحول من مساعد إلى شريك تشخيصي في 2026",
            "excerpt": "تقرير Mayo Clinic: AI في المختبرات لم يعد مجرد دعم للقرار بل أصبح شريكاً تشخيصياً فعالاً.",
            "source": "Mayo Clinic",
            "tag": "tech"
        },
        {
            "title": "اختبارات الدم لمرض ألزهايمر تدخل الرعاية الأولية في 2026",
            "excerpt": "FDA تعتمد اختبارات دم جديدة للكشف عن ألزهايمر في الرعاية الأولية. اختبارات p-tau217 وp-tau181 متاحة الآن.",
            "source": "FDA",
            "tag": "diagnostic"
        },
        {
            "title": "CDC تدعو إلى الاستعداد لتفشيات جديدة في 2026",
            "excerpt": "تحديثات CDC لعام 2026: ترقب لتفشيات جديدة من الأنفلونزا والفيروسات التنفسية. توصيات بزيادة سعة الاختبارات.",
            "source": "CDC",
            "tag": "outbreak"
        }
    ]
    
    # Select 4 random news items
    selected = random.sample(news_database, 4)
    
    # Format with IDs and dates
    formatted_news = []
    today = datetime.now().strftime("%d %B %Y")
    
    tag_names = {
        "outbreak": "وبائي",
        "tech": "تقني",
        "diagnostic": "تشخيصي",
        "guideline": "إرشادات"
    }
    
    for i, item in enumerate(selected, 1):
        formatted_news.append({
            "id": i,
            "title": item["title"],
            "excerpt": item["excerpt"],
            "source": item["source"],
            "sourceClass": f"source-{item['source'].lower().replace(' ', '-')}",
            "date": today,
            "tag": item["tag"],
            "tagClass": f"tag-{item['tag']}",
            "tagName": tag_names[item["tag"]],
            "url": "#"
        })
    
    return formatted_news

def main():
    print("Generating daily news...")
    
    news = generate_daily_news()
    
    with open("news.json", "w", encoding="utf-8") as f:
        json.dump(news, f, ensure_ascii=False, indent=2)
    
    print(f"Generated {len(news)} news items for {datetime.now().strftime('%d %B %Y')}")

if __name__ == "__main__":
    main()
