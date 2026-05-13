import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import sanitizeHtml from 'sanitize-html';
import MarkdownIt from 'markdown-it';
const parser = new MarkdownIt();

export async function GET(context) {
    const posts = await getCollection('blog')
    return rss({
	title: 'Daniel Thedie | Blog',
	description: 'Personal blog of Daniel Thedie - Research Software Engineer at the University of Edinburgh',
	site: context.site,
	items: posts.map((post) => ({
	    title: post.data.title,
	    pubDate: post.data.pubDate,
	    link: `/blog/${post.id}/`,
	    content: sanitizeHtml(parser.render(post.body), {
		allowedTags: sanitizeHtml.defaults.allowedTags.concat(['img'])
	    }),
	})),
	customData: `<language>en-gb</language>`,
	stylesheet: '/pretty-feed-v3.xsl',
    });
}
