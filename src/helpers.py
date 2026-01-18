def fill_html_template(template_path, **kwargs):
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    return template.format(**kwargs)


def inject_html_section(target_html_path,
                        marker_start,
                        marker_end,
                        insert_html):
    with open(target_html_path, "r", encoding="utf-8") as f:
        content = f.read()
    start_idx = content.find(marker_start)
    end_idx = content.find(marker_end)
    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        raise ValueError("Markers not found or in wrong order")
    new_content = (
        content[: start_idx + len(marker_start)]
        + "\n" + insert_html + "\n"
        + content[end_idx:]
    )
    with open(target_html_path, "w", encoding="utf-8") as f:
        f.write(new_content)
