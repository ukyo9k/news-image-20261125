# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/ukyo9k/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/ukyo9k/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-page newspaper poster summing up the world's news of Wednesday 25 November 2026, drawn from scratch with Python (PIL) — no stock photos, no copied artwork. The lead story is the launch of Shenzhou-24, carrying the first Pakistani and the first foreign astronaut ever to China's Tiangong space station; the other six stories span a cyberattack on the CIA and the US intelligence chief's office, an Australia–Solomon Islands security pact, Huawei's guilty verdict in a US trial, a Houthi drone strike on Riyadh's tallest tower, the evacuation of Ebola teams in DR Congo, and a huge lead-azide detonation planned in Iowa. Every claim on the poster is worded as reported, not as confirmed fact.

The seven stories, each verified against a real news source:

1. **Shenzhou-24 launches with a first for Pakistan** — China's Shenzhou-24 blasted off at 00:18 UTC carrying Pakistani pilot Muhammad Zeeshan Ali, the first Pakistani in orbit and the first foreign astronaut to visit the Tiangong station (Reuters; Xinhua; Nature).
2. **CIA and US intel office hit by hack** — the CIA and the Office of the Director of National Intelligence suffered an apparent cyberattack on an unclassified system; no classified data was affected, with early signs pointing to China (CNN; The New York Times).
3. **Australia–Solomon Islands security pact** — the two countries signed a security pact making Canberra the islands' defence partner of choice, replacing an earlier deal with China (Reuters).
4. **Huawei guilty in US secrets trial** — a New York jury found Huawei guilty on 10 of 12 counts, including bank fraud and conspiracy to steal trade secrets, after a three-month trial (US Department of Justice; AFP).
5. **Houthi drone hits Riyadh tower** — a drone struck the PIF tower in Riyadh's financial district, injuring 11 people, the second hit on the capital's tallest tower in under a week (Reuters; Saudi Civil Defence).
6. **Ebola teams evacuated after 3 days** — WHO staff and Congolese health workers were evacuated from a hospital in Akwe, DR Congo, after sheltering three days amid fierce fighting (WHO; IANS).
7. **Iowa braces for huge lead-azide blast** — the US Army will detonate 9,500 lbs of ageing lead azide at 9 a.m. in Middletown, Iowa, the largest such blast in nearly 50 years (Des Moines Register).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3, standard library only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` and verifies the copy's sha256 matches the bundled file. It is deterministic: two runs write byte-identical output. The poster itself is drawn by `draw_poster.py`, included in this repository, using only PIL primitives and DejaVu fonts.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
