def image_html(image_url, alt_text="", css_class=""):
    if image_url:
        return f'<img src="{image_url}" alt="{alt_text}" class="{css_class}"/>'
    return ""


def button_html(url, icon, label, css_class):
    if url:
        return (f'<a href="{url}" class="{css_class}" '
                f'rel="noopener">'
                f'<span class="{icon}" '
                f'style="margin-right:0.4em;"></span>{label}</a>')
    return ""


def button_html_rev(url, icon, label, css_class):
    if url:
        return (f'<a href="{url}" class="{css_class}" '
                f'rel="noopener">'
                f'{label}'
                f'<span class="{icon}" '
                f'style="margin-left:0.4em;"></span></a>')
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


def add_blog_buttons(page, blog_list, blog_number):
    if blog_number < len(blog_list) - 1:
        page['next-blog'] = ''
    else:
        next_blog = blog_list[blog_number - 1]
        title = get_blog_title(next_blog)  
        page['next-blog'] = button_html_rev(
            f'/blog/{next_blog.stem}.html',
            'fas fa-arrow-right',
            title,
            'button'
        )
        
    if blog_number == 0:
        prev_blog = blog_list[blog_number + 1]
        title = get_blog_title(prev_blog)
        page['previous-blog'] = button_html(
            f'/blog/{prev_blog.stem}.html',
            'fas fa-arrow-left',
            title,
            'button'
        )
    else:
        page['previous-blog'] = ''
        
    page['blog-list-menu'] = '' # Not implemented, could be added later


def get_blog_title(blog_post):
    with open(blog_post, 'r', encoding='utf-8') as f:
        md_text = f.read()
    return next(line[2:].strip() for line in md_text.splitlines() if line.startswith('# ')) 
