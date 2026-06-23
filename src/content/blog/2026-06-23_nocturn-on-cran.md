---
title: 'nocturn published on CRAN!'
pubDate: 2026-06-23
author: 'Daniel Thedie'
---

nocturn just got published on [CRAN](https://cran.r-project.org/package=nocturn)!

nocturn is an online app and R package for sleep data analysis. It allows loading any type of data that is based on sleep sessions, whether it was produced by a radar device, actigraphy, sleep diary, or other.

You can access the nocturn app online at [nocturn.bio.ed.ac.uk](https://nocturn.bio.ed.ac.uk) (no installation required). And if you want to write your own R scripts using nocturn, you can now install it directly from CRAN with:

```r
install.packages("nocturn")
```

To use the package, load functions:

```r
library(nocturn)
```

And display the package manual:

```r
help(package = "nocturn")
```

## Next steps

The current nocturn version on CRAN is 1.1.3. I am currently working on version 1.2.0, with some exciting updates to come:

- Comparison tool
  - Load multiple sessions files and compare them, e.g. with a [Bland-Altman plot](https://en.wikipedia.org/wiki/Bland%E2%80%93Altman_plot)
- New sleep reports
  - Dataset comparison report
  - Report for actigraphy data
  - More customisation of text fields
- Save and load filter sets
  - Quickly apply a precise set of filters
  - Share with collaborators
  - Include with your data as documentation of your analysis process
- Enhanced in-app documentation
  - More tooltips explaining plots and options

Interested in using nocturn with your own data? Let me know in [Discussions](https://github.com/chronopsychiatry/AMBIENT-BD-nocturn/discussions)!

Found a bug in the app or R functions; or need help with a specific point? [Open an issue](https://github.com/chronopsychiatry/AMBIENT-BD-nocturn/issues)
