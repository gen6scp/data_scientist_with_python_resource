import requests
import time
import os, re, argparse
import traceback
import random

import datetime
from bs4 import BeautifulSoup, element
import osint_sqlite


db = osint_sqlite.Database()
db.create_tables()  # Attempt to create table(s) if not exists already.


def traceback_maker(err):
    """ Make a traceback from the error """
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = ('{1}{0}: {2}').format(type(err).__name__, _traceback, err)
    return error


class Feed:
    def __init__(self, html_data):
        self.html = html_data
        self.info = html_data.find("div", {"class": "title"}).text
        self.id = html_data.attrs.get("data-id", None)
        self.extra = html_data.attrs.get("data-link", None)
        
    @property
    def video(self):
        """ Returns the video url if available """
        main_video = self.html.attrs.get("data-twitpic", None)
        if main_video and "video" in main_video:
            return main_video

        find_video = self.html.find("blockquote", {"class": "twitter-video"})
        if not find_video:
            return None
        return find_video.find("a").attrs.get("href", None)

    @property
    def image(self):
        """ Get the image of the feed """
        find_img = self.html.find("div", {"class": "img"})
        if not find_img:
            return None
        try:
            return find_img.find("img").attrs.get("src", None)
        except AttributeError:
            return None


class Article:
    def __init__(self, feed: Feed, html_data):
        self.html = html_data
        self.feed = feed

        self.image = feed.image
        self.info = feed.info
        self.id = feed.id
        self.extra = feed.extra
        self.video = feed.video
        self._setLocation()

    """
    A hacky implementation to extract the location (lat/lng)
    """
    def _setLocation(self):
        self.lat = 0
        self.lng = 0

        # Split the HTML content by lines and take the last 30 lines
        last_N_lines = "\n".join(str(self.html).splitlines()[-30:])

        # Use regex to extract lat and lng values from the script content
        lat_lng_pattern = r".*lat=([-+]?\d*\.\d+|\d+);\n.*lng=([-+]?\d*\.\d+|\d+);"

        # Search for the lat and lng in the last 30 lines
        match = re.search(lat_lng_pattern, last_N_lines)
        
        if match:
            self.lat = match.group(1)  # Latitude value
            self.lng = match.group(2)  # Longitude value
            print(f"* Latitude: {self.lat}, Longitude: {self.lng}")
        else:
            print("* No latitude and longitude found in the last 100 lines")

    @property
    def source(self):
        """ Get the source of the article """
        html = self.html.find("a", {"class": "source-link"})
        if not html:
            return None
        return html.attrs.get("href", None)



def debug_html(content: str, debug):
    if debug:
        if not os.path.exists("./debug"):
            os.mkdir("./debug")
        with open(f"./debug/debug_{int(time.time())}.html", "w", encoding="utf8") as f:
            html = BeautifulSoup(content, "html.parser")
            f.write(html.prettify())



def fetch(url: str, debug = False):
    """ Simply fetch any URL given, and convert from bytes to string """
    print("Fetching [" + url + "] ...")
    r = requests.get(
        url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
    )
    text = r.content.decode("utf-8")
    debug_html(text, debug)
    return text



def scrape(past, debug):
    start = datetime.datetime.today()
    dates = [start - datetime.timedelta(days=x)
             for x in range(0, past)]
    
    for date in dates:
        try:
            # Random wait time to not be too obvious
            # Since we are scraping the website, lol
            check_in_rand = random.randint(2, 10)
            
            BASE_URL = "https://liveuamap.com/en/time/"
            date_url = date.strftime("%d.%m.%Y")
            print(f"{date_url} - Checking for new articles")
            r = fetch(BASE_URL + date_url)
            html = BeautifulSoup(r, "html.parser")
            
            try:
                feeder = html.find("div", {"id": "feedler"})
                latest_news_sorted = sorted(
                    [g for g in feeder if isinstance(g, element.Tag)],
                    key=lambda g: g.attrs.get("data-time", 0), reverse=True
                )
            except TypeError:
                # For some weird reason, this website loves to crash with HTTP 5XX
                # So we just try again because the website encourages us to, really.
                print("Failed to get feeder, probably 500 error, trying again...")
                time.sleep(3)
                continue
        
            for entry in range(len(latest_news_sorted)):
                news = Feed(latest_news_sorted[entry])
                data = db.fetchrow("SELECT * FROM articles WHERE post_id=?", (news.id,))
                
                if not data:
                    print(f"[{entry}/{len(latest_news_sorted)}] New article found, checking article: ")
                    r_extra = fetch(news.extra, debug)
                    extra_html = BeautifulSoup(r_extra, "html.parser")
                    article = Article(news, extra_html)
                    date_sql = date.strftime("%Y-%m-%d")
                
                    db.execute(
                        "INSERT INTO articles (date, post_id, url, text, source, lat, lng, video, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (date_sql, article.id, news.extra, article.info, article.source, article.lat, article.lng, article.video, article.image)
                    )

                    print(f"* Extarcted: {date_sql}, {article.id}, {news.extra}, {article.info}, {article.source}, {article.lat}, {article.lng}, {article.video}, {article.image}")
                    time.sleep(check_in_rand)
                    
        except Exception as e:
            print(traceback_maker(e))
        



def main():
    parser = argparse.ArgumentParser(description='Scraper for up-to-date data from Liveuamap website.')
    parser.add_argument('-p', '--past', type=int, default=1, help='Specify the past days you want to scrape')
    parser.add_argument('-d', '--debug', action='store_true', help='Debug Option. When specified, put html into debug')

    args = parser.parse_args()
    scrape(args.past, args.debug)


try:
    main()
except KeyboardInterrupt:
    print("Exiting...")
