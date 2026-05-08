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
    date: z.string().optional(),
    description: z.string().optional(),
  }),
});

export const collections = { presentations };
