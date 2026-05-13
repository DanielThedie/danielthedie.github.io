import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import sanitizeHtml from 'sanitize-html';
import MarkdownIt from 'markdown-it';
const parser = new MarkdownIt({ html: true });

function absolutiseHtmlUrls(html, site) {
    const origin = new URL(site).origin;
    html = html.replaceAll(/src="\/(.*?)"/g, `src="${origin}/$1"`);
    return html;
}

export async function GET(context) {
    const posts = await getCollection('blog')
    return rss({
	title: 'Daniel Thedie | Blog',
	description:
	'Personal blog of Daniel Thedie - Research Software Engineer at the University of Edinburgh',
	site: context.site,
	items: posts.map((post) => {
	    const rendered = parser.render(post.body);
	    const withAbsoluteUrls = absolutiseHtmlUrls(rendered, context.site);

	    return {
		title: post.data.title,
		pubDate: post.data.pubDate,
		link: `/blog/${post.id}/`,
		content: sanitizeHtml(withAbsoluteUrls, {
		    allowedTags: sanitizeHtml.defaults.allowedTags.concat(['img']),
		    allowedAttributes: {
			...sanitizeHtml.defaults.allowedAttributes,
			img: ['src', 'alt', 'title', 'width', 'height', 'loading', 'srcset', 'sizes', 'class'],
		    },
		}),
	    };
	}),
	customData: `<language>en-gb</language>`,
	stylesheet: '/pretty-feed-v3.xsl',
    });
}
