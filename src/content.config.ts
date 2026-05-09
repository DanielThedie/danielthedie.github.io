import { defineCollection } from "astro:content";
import { z } from "zod";
import { glob } from "astro/loaders";

const presentations = defineCollection({
  loader: glob({ pattern: "**/*.{yml,yaml}", base: "./src/content/presentations" }),
  schema: z.object({
    title: z.string(),
    event: z.string(),
    slug: z.string(),
    file: z.string(),
    date: z.date(),
    description: z.string().optional(),
  }),
});

const blog = defineCollection({
  loader: glob({ pattern: '**/[^_]*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    pubDate: z.date(),
    author: z.string()
  })
})

export const collections = { presentations, blog };
