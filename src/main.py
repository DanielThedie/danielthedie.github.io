from timeline.timeline_generator import TimelineGenerator
from helpers import inject_html_section


def generate_website():
    tg = TimelineGenerator("content/timeline.yaml")
    html = tg.generate_timeline_html()
    inject_html_section(
        "docs/index.html",
        "<!-- TIMELINE_START -->",
        "<!-- TIMELINE_END -->",
        html
    )


if __name__ == "__main__":
    generate_website()
