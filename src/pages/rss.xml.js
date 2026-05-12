import rss from '@astrojs/rss';
import { getCollection } from 'astro:content'

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
	})),
	customData: `<language>en-gb</language>`,
    });
}
