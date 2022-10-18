from classes import crawler

def main():
    link_c = crawler.Link_crawler()
    link_c.get("https://www.google.com")

    photo_c = crawler.Photo_crawler()
    photo_c.get("https://www.google.com")

if __name__ == "__main__":
    main()
