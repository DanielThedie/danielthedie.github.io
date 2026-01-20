def image_html(image_url, alt_text="", css_class=""):
    if image_url:
        return f'<img src="{image_url}" alt="{alt_text}" class="{css_class}"/>'
    return ""


def button_html(url, icon, label, css_class):
    if url:
        return (f'<a href="{url}" class="{css_class}" '
                f'target="_blank" rel="noopener">'
                f'<span class="{icon}" '
                f'style="margin-right:0.4em;"></span>{label}</a>')
    return ""


def format_image(event, page_title):
    if 'image' in event:
        event['image'] = image_html(
            event['image'],
            event.get('title', ''),
            f'{page_title}-image'
            )


def format_buttons(event):
    if 'github' in event:
        event['github'] = button_html(
            event['github'],
            'fab fa-github',
            'Code',
            'button'
        )
    if 'app' in event:
        event['app'] = button_html(
            event['app'],
            'fa fa-globe',
            'App',
            'button'
        )
    if 'docs' in event:
        event['docs'] = button_html(
            event['docs'],
            'fa fa-book-open',
            'Docs',
            'button'
        )
    if 'doi' in event:
        event['doi'] = button_html(
            event['doi'],
            'fa fa-link',
            'DOI',
            'button'
        )
