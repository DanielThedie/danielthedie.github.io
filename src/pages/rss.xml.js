import rss, { pagesGlobToRssItems } from '@astrojs/rss';

export async function GET(context) {
  return rss({
    title: 'Daniel Thedie | Blog',
    description: 'Personal blog of Daniel Thedie - Research Software Engineer at the University of Edinburgh',
    site: context.site,
    items: await pagesGlobToRssItems(import.meta.glob('./**/*.md')),
    customData: `<language>en-gb</language>`,
  });
}
