from .timeline.timeline_generator import TimelineGenerator


def generate_website():
    tg = TimelineGenerator("timeline.yaml")
    html = tg.generate_timeline_html()
    with open("timeline.html", "w", encoding='utf-8') as f:
        f.write(html)


if __name__ == "__main__":
    generate_website()
