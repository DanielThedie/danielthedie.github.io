from site_generator import SiteGenerator


def main():
    gen = SiteGenerator(
        content_folder="content",
        templates_folder="templates",
        docs_folder="docs"
    )
    gen.create_pages()
    gen.add_from_yaml("index")
    gen.add_from_yaml("publications")
    gen.add_from_yaml("software")
    gen.add_blog()


if __name__ == "__main__":
    main()
