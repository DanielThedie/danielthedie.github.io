from generators.site_generator import SiteGenerator


def main():
    gen = SiteGenerator(
        content_folder="content",
        templates_folder="templates",
        docs_folder="docs"
    )
    gen.create_page("index", page_title="about")
    gen.create_page("publications")
    gen.create_page("software")


if __name__ == "__main__":
    main()
