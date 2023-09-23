---
title: Headline and Framing Experiment
date: 2023-09-23
summary: Using generative AI, I explore the possibility of reshaping news content to enhance accessibility and understand diverse reporting perspectives. The results? Mixed.
---

As a data guy and a journalist, I'm fascinated by the potential of generative AI
to repackage the news in ways that make it more accessible.

I'm always interested in better understanding who is covering what, and how
they're covering it. So I decided to ask Claude-2, with its expansive 100K token
context window, to help me out.

## The Experiment

Using feeds from two popular news aggregators, I asked the model to generate a
list of the top 10 stories. Then, I asked Claude-2 to give me a nice digest,
with easy-to-read headlines, summaries--and bullet points capturing the
different framings from different outlets.

As a quick aside, it's worth noting: We really haven't had access to tools like
this for very long. Claude-2 was
[announced](https://www.anthropic.com/index/claude-2) by Anthropic on July 11,
and its
[100,000 token context window](https://www.anthropic.com/index/100k-context-windows)
is unlike anything else easily accessible today. According to Anthropic, it can
process _hundreds of pages_ of content at once.

So this gives us an opportunity to really survey the day's news landscape in a
way that wasn't possible before. While GPT-4 may be superior to Claude-2 in a
lot of respects, its context windows are
[much smaller](https://help.openai.com/en/articles/7127966-what-is-the-difference-between-the-gpt-4-models)
(8K for most people; 32K for a lucky few).

What follows is a brief experiment using [Claude-2], which has a 100K token
context window, to generate headlines and framing for news stories from two news
aggregators.

## The Experiment

Using input from [BizToc](/assets/data/2023-09-23-headlines-biztoc.html) and
[AllTop](/assets/data/2023-09-23-headlines-alltop.html), I asked the Claude-2 to
generate a list of the top 10 stories and then to generate headlines, summaries,
and bullet points for each of those stories.

**Prompt #1**

```md
What are the 10 biggest stories happening right now?
```

**Prompt #2**

```md
Now, for each of these events, please write an easy-to-read headline, a summary,
and a sequence of bullet points capturing the framing of the story in different
sources (but only if the framing is meaningfully different across different
outlets).

Please follow this format:

## Headline

Summary

- Framing #1
- Framing #2 ...

For example:

## United Auto Workers Strike Expands to 38 More Facilities

The UAW expanded strikes to additional GM and Stellantis plants, raising the
total to around 150 facilities, as contract negotiations continue.

- CNBC focuses on the economic impacts of the growing strike.
- The Detroit Free Press emphasizes union solidarity behind the strikes.
- The Wall Street Journal says the strike threatens production of popular truck
  models.

Do not add any additional text to your output (no intro, no conclusion, no
commentary, etc.). Just the headlines, summaries, and bullet points.
```

The example here was taken from an earlier iteration of the process that I
thought did a good job of capturing the essence of the task.

I had tried to include links to the original stories, but the model struggled
with getting them right, so I removed them. I think GPT-4 would likely have been
able to handle this, but the length of the input file was far too long and I
didn't feel like figuring out a way to split it up.

---

## Model Output

### Prompt #1: The ten biggest stories happening right now.

Based on reviewing major news outlets, here are 10 of the biggest news stories
at the moment:

1. Russia-Ukraine War: Ukraine continues counteroffensive operations, targeting
   Russian forces in Crimea and the Donbas region. Russia vows to respond
   "harshly."
2. U.S. Politics: Senator Bob Menendez was indicted on federal corruption
   charges related to allegedly accepting bribes. This could impact Democrats'
   slim Senate majority.
3. U.S. Economy: The UAW auto workers strike expanded, threatening to disrupt
   auto production. The government faces a potential shutdown if Congress
   doesn't pass a funding bill.
4. U.K. Politics: Prime Minister Liz Truss defended her economic plan amid
   criticism and turmoil in financial markets. The pound hit a record low
   against the dollar.
5. Iran Protests: Demonstrations continue over the death of Mahsa Amini, who
   died in police custody after being detained for allegedly violating headscarf
   rules.
6. NASA: The space agency revealed new images of Jupiter taken by the James Webb
   Space Telescope showcasing auroras and weather patterns.
7. China: Authorities imposed lockdowns and other restrictions in Chengdu, a
   city of 21 million, amid a COVID-19 outbreak.
8. Climate: World leaders gather at the UN General Assembly to discuss climate
   change, energy, and sustainability issues.
9. Tech: India delayed a plan to require registration for laptop imports after
   pushback. EU fined Intel $400 million over antitrust practices.
10. Sports: The Ryder Cup golf tournament teed off, NFL and college football are
    in full swing, baseball playoffs near, and the FIFA World Cup is upcoming.

### Prompt #2: Headlines, summaries, and bullet points

> Here are the top 10 news stories with headlines, summaries, and framings:
>
> #### Russia Steps Up Attacks on Ukraine, Vowing Harsh Response
>
> Russia launched new missile strikes on Ukraine and threatened further
> escalation after Ukrainian forces struck targets in Crimea.
>
> - The New York Times focuses on Russia's pledge of retaliation for the Crimea
  > strikes.
> - BBC highlights Russia's claims that the strikes killed civilians in
  > Sevastopol.
> - The Wall Street Journal emphasizes Ukraine's targeting of Russian military
  > infrastructure.
>
> #### Senator Menendez Indicted on Corruption Charges
>
> U.S. Senator Bob Menendez was indicted on federal corruption charges related
> to allegedly accepting bribes from a doctor in exchange for political favors.
>
> - Politico says the charges could impact Democrats' Senate majority before
  > midterms.
> - CNN points out this is the second time Menendez has been indicted on
  > corruption charges.
> - Fox News highlights calls for Menendez to resign from office.
>
> #### UAW Strike Spreads as Government Shutdown Looms
>
> The UAW auto workers strike expanded to over 150 facilities, threatening
> further disruption, as Congress faces a shutdown if it doesn't pass a funding
> bill.
>
> - NPR focuses on the spreading labor action across GM, Ford, and Stellantis
  > plants.
> - The Washington Post emphasizes the high political stakes around a potential
  > shutdown.
> - Business Insider says the strike could raise car prices and repair delays.
>
> #### UK Prime Minister Defends Economic Plan Amid Criticism
>
> UK Prime Minister Liz Truss defended her controversial economic growth plan
> that cut taxes for the wealthy but sent the pound plunging.
>
> - BBC says Truss insists her plan is the right course despite financial
  > turmoil.
> - Bloomberg notes Truss faces discontent within her own Conservative Party
  > over the plan.
> - The Guardian reports the plan benefits the rich far more than the poor.
>
> #### Protests Persist in Iran Over Woman's Death in Police Custody
>
> Protests continue in Iran over the death of Mahsa Amini after she was detained
> by morality police for allegedly violating headscarf rules.
>
> - Al Jazeera focuses on spreading unrest and internet disruptions.
> - France24 highlights women defiantly removing their hijabs in protest.
> - FRANCE 24 English notes a harsh government crackdown on demonstrations.
>
> #### NASA Releases Stunning New Images of Jupiter from Webb Telescope
>
> NASA revealed remarkable photos of Jupiter's northern and southern lights,
> weather patterns, and rings taken by the James Webb Space Telescope.
>
> - Space.com marvels at Webb's capacity to photograph details never seen
  > before.
> - CNET showcases the images' views of auroras and moon shadows.
> - Scientific American describes what Webb reveals about Jupiter's atmospheric
  > composition.
>
> #### Chengdu Imposes Lockdown Amid COVID-19 Surge
>
> The major Chinese city of Chengdu imposed a lockdown on its 21 million
> residents due to a spike in COVID-19 cases.
>
> - Al Jazeera says the lockdown reflects China's continued zero-COVID approach
  > despite costs.
> - NPR reports residents are only allowed to leave home once every few days for
  > groceries and supplies.
> - The Wall Street Journal notes the move disrupts production at major Apple
  > supplier Foxconn.
>
> #### EU Slaps Intel with $400 Million Antitrust Fine
>
> The EU imposed a $400 million fine on Intel for antitrust violations related
> to restricting competitors through loyalty rebates.
>
> - TechCrunch says the fine ends a decade-long dispute between Intel and
  > regulators.
> - The Verge points out this is the latest in a series of EU antitrust
  > decisions against U.S. tech giants.
> - Reuters notes Intel is challenging the fine and says the case is outdated.
>
> #### Ryder Cup Golf Tournament Starts with U.S. Favored
>
> The Ryder Cup golf tournament between the U.S. and Europe teed off in Italy,
> with the Americans favored after a dominating win last time.
>
> - ESPN previews the elite American squad led by Scottie Scheffler and Justin
  > Thomas.
> - The Guardian says Europe is an underdog but points to encouraging play by
  > some veterans.
> - Golf Digest thinks the Europeans may rally around honoring the late Queen
  > Elizabeth II.
>
> #### FIFA World Cup Looms as Teams Finalize Preparations
>
> With the FIFA World Cup starting in November, teams are finalizing their
> rosters and strategies in remaining tune-up matches.
>
> - Sports Illustrated highlights injuries impacting prominent players like
  > Neymar.
> - Fox Sports suggests France is the favorite with its diverse talent pool.
> - Bleacher Report thinks Brazil's roster depth makes it hard to top in Qatar.

Looks great, right?

Err, except one thing: the FIFA World Cup happened last year.

Purely out of curiousity, I asked the model why it thought the FIFA World Cup
would be happening soon, to which it responded:

> There are a few key reasons the FIFA World Cup is happening in
> November-December this year:
>
> - Timing: The World Cup usually takes place during the summer months. However,
  > for the 2022 edition, FIFA selected Qatar as the host country. Qatar
  > experiences extremely hot summer temperatures, routinely over 100°F (38°C).
  > So for the first time, FIFA moved the event to cooler fall/winter months
  > instead.
> - Logistics: By holding the World Cup in November-December, venues can
  > maintain comfortable playing conditions. The shift avoids the worst of
  > Qatar's summer heat. Stadiums have cooling technology to maintain suitable
  > temperatures.
> - Competition schedule: Major domestic football leagues take a break during
  > the World Cup to allow players to participate. Scheduling it in
  > November-December fits best with European leagues' calendars after starting
  > seasons in August-September.
> - Global audience: While the timing is challenging for leagues in Europe and
  > the Americas, it allows fans in many other parts of the world to tune in at
  > favorable hours. The schedule maximizes the overall global TV audience.
> - Controversy: Some leagues have complained about the disruption caused by
  > rescheduling their seasons around the World Cup dates. But FIFA selected the
  > November-December timeframe to make the event workable given Qatar's
  > climate.
>
> In summary, the unusual fall scheduling for this World Cup accommodates
> playing conditions in Qatar and the availability of worldwide talent and fans.
> But it has proven controversial given its impacts on normal league schedules.
