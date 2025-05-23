import requests
from bs4 import BeautifulSoup
import webbrowser

def search_google(phone_number):
    """ מבצע חיפוש בגוגל על מספר הטלפון """
    search_url = f"https://www.google.com/search?q={phone_number}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        results = [a.text for a in soup.find_all("h3")]
        return results if results else ["לא נמצאו תוצאות"]
    return ["שגיאה בחיפוש בגוגל"]

def search_socials(phone_number):
    """ פותח חיפושים ברשתות חברתיות ובאתרי מידע """
    urls = {
        "🔵 Facebook": f"https://www.facebook.com/search/top?q={phone_number}",
        "🔗 LinkedIn": f"https://www.linkedin.com/search/results/people/?keywords={phone_number}",
        "📸 Instagram": f"https://www.instagram.com/explore/tags/{phone_number}/",
        "💬 Telegram": f"https://t.me/{phone_number}",
        "☎️ Truecaller Web": f"https://www.truecaller.com/search/il/{phone_number}",
        "🟠 144 בזק": f"https://www.b144.co.il/search?type=phone&query={phone_number}",
        "📢 דפי זהב": f"https://www.d.co.il/lookup/{phone_number}/",
        "📌 לוח יד2": f"https://www.yad2.co.il/search?query={phone_number}",
        "🏪 זאפ דפי עסקים": f"https://www.zap.co.il/search.aspx?keyword={phone_number}",
        "📑 פורום FXP": f"https://www.fxp.co.il/search.php?query={phone_number}",
        "📚 Reddit": f"https://www.reddit.com/search/?q={phone_number}",
        "🌐 Whois חיפוש דומיינים": f"https://who.is/whois/{phone_number}",
        "📰 חיפוש חדשות גוגל": f"https://www.google.com/search?tbm=nws&q={phone_number}",
    }
    
    print("\n🔎 פותח דפי חיפוש ברשתות חברתיות ובאתרים נוספים...")
    for name, url in urls.items():
        print(f"📂 מחפש ב-{name}...")
        webbrowser.open(url)

if __name__ == "__main__":
    phone = input("📞 הזן מספר טלפון ישראלי: ")
    
    print("\n🔍 תוצאות מגוגל:")
    google_results = search_google(phone)
    for result in google_results:
        print(result)

    # פתיחת דפי חיפוש ברשתות חברתיות ואתרים ציבוריים
    search_socials(phone)
