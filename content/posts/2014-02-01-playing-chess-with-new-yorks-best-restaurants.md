---
layout: post
title: Playing Chess with New York's Best Restaurants
summary: Or how I've spent several years figuring out where I like to eat.
math: true
date: 2014-02-01
---

I moved to New York City from Miami in the summer of 2011. The displacement was
immense, and while I had quite a few friends in the city, I missed my home.

To fend off homesickness and take advantage of my new environs, I decided to
become a connoisseur of New York's most famous attraction: restaurants. I began
keeping track of everywhere I ate.

When I talked about my restaurant tracking -- particularly to out-of-towners --
I'd always get the same questions: Where should I eat when I visit New York?
What's your favorite sushi spot? Can you recommend dumplings in the Lower East
Side?

I found myself fumbling to answer these questions. I like to be precise. If you
ask me to tell you the best restaurant I've been to, I want my response to be
rooted in something objective. I want to be able to support my assertion with
more than just a vague and fleeting hunch.

So I decided to try to rank my favorite restaurants. I created a spreadsheet,
filled it with dozens of spots around the city and started trying to assign
scores.

Initially, I decided I'd rank them on a scale ranging from 1 -- the absolute
worst place you can imagine -- to 100 -- exquisite deliciousness. To
[Daniel](http://danielnyc.com/), an elegant French bistro on the Upper East
Side, I assigned a 95. To
[St. Anselm](http://www.yelp.com/biz/st-anselm-brooklyn), a casual chophouse in
Brooklyn, I gave a 79. To [Mr. Fish](http://www.yelp.com/biz/mr-fish-new-york),
a sushi stand in a Koreantown cafeteria, I gave a 31.

As I diligently fleshed out the list, I ran into problems, and my scores began
falling out of whack. I started to use restaurants I'd already scored to rank
the new additions. [Locanda Verde](http://locandaverdenyc.com/) was a little
better than [Parish Hall](http://www.parishhall.net/) (68), but not as good as
[The Smith](http://www.thesmithnyc.com/) (77), so I gave it a 69. I liked
[Takahachi](http://www.takahachi.net/) more than
[Blue Ribbon Sushi](http://www.blueribbonrestaurants.com/rests_sushi_man_main.htm)
(51), but not as much as [Sushi Yasuda](http://www.sushiyasuda.com/) (65): it
got 61. And wait a minute -- what was Sushi Yasuda doing at 65, when it's better
than Parish Hall, which I'd already given a 68?

On top of that, I realized my tastes changed. On my first visit to
[Sushi of Gari](http://www.sushiofgari.com/), I wasn't all that impressed. On my
second visit, I got the omakase, and fell immediately in love. Did that mean I
needed to move Sushi of Gari up? And how did that affect Takahachi, if at all?

I was now more confused than when I first began my exploration. And that's when
it hit me.

#### Scoring the Game of Chess

What I was really doing was comparing restaurants against each other. Today,
[Aldea](http://aldearestaurant.com/) beats
[Supper](http://supperrestaurant.com/). Maybe tomorrow, Supper beats
[A Voce](http://www.avocerestaurant.com/). Then, along comes
[Marea](http://www.marea-nyc.com/index.php?action=page&id=1880), which beats all
three.

Rather than trying to assign arbitrary scores to each restaurant, I could simply
track which ones I liked better than others. Then I could look back on each
restaurant's record -- its wins and losses -- and tally up who consistently came
out on top.

Turns out, people have developed
[a number of techniques](http://en.wikipedia.org/wiki/Comparison_of_top_chess_players_throughout_history)
for rating players in head-to-head competitions. One of the best-known rating
systems is the one used to score chess players.

It's easiest to walk through an example. Imagine a chess tournament played by a
group of four people competing for the very first time.

Because they've never competed before, none of them have a track record, and,
going into the tournament, there's no way to tell which player is most likely to
win. Chess rating systems deal with that by assigning every newcomer the same
number. For our example's sake, let's give each of our four players an initial
score (usually called a "provisional" rating) of 1,200.

| Player       | Provisional Score |
| ------------ | ----------------- |
| Player One   | 1,200             |
| Player Two   | 1,200             |
| Player Three | 1,200             |
| Player Four  | 1,200             |

In the first round of our imaginary tournament, Player One, using the white
pieces, beats Player Two and Player Four, using black pieces, beats Player
Three.

| White        | Black       | Outcome |
| ------------ | ----------- | ------- |
| Player One   | Player Two  | 1-0     |
| Player Three | Player Four | 0-1     |

We can use the results of this round to update each of our players' ratings. For
the sake of our example, I'll use one of the simplest formulas for adjusting
scores: the [Elo rating system](http://en.wikipedia.org/wiki/Elo_rating_system),
developed by [Arpad Emrick Elo](http://en.wikipedia.org/wiki/Arpad_Elo).

The math isn't too bad, but if you're not interested, you can skip to the next
section.

#### The Math Behind Elo

The Elo system uses the player's starting scores to derive an expected outcome
of the game, and then changes each player's rating based on the probability of
the actual outcome. In English, if a player with an extremely high score beats a
player with an extremely low score, neither player's rating will change much,
because the outcome was expected. However, if the player with the high score
loses the match, then his or her rating drops significantly, and similarly, the
player with the low score who won sees a marked increase in his or her rating.

The math looks like this. For Player One and Player Two having ratings R1 and
R2:

$$
    \begin{aligned}
    Expected_1 &= \frac{1}{1 + 10^{(R_2 - R_1)/400}} \\\\
    Expected_2 &= \frac{1}{1 + 10^{(R_1 - R_2)/400}}
    \end{aligned}
$$

This expected outcome ranges from 0 (a loss) to 1 (a win). In our example,
because all our players have the same starting score, we wind up with equal
probabilities for the expected outcome:

$$
    \begin{aligned}
    Expected_1 &= \frac{1}{1 + 10^{(1200 - 1200)/400}} &= 0.5 \\\\
    Expected_2 &= \frac{1}{1 + 10^{(1200 - 1200)/400}} &= 0.5
    \end{aligned}
$$

Once we've calculated the expected outcome, we change the ratings according to
what actually happened. For Player One, the actual outcome (we'll call it S1) is
a win, which we denote as a 1; for Player Two, the actual outcome (S2) is a
loss, we'll denote it with a 0. K is simply a scaling factor which we'll set to
32 for the sake of our example:

$$
    \begin{aligned}
    R_1' &= R_1 + K(S_1 - Expected_1) &= 1200 + 32(1 - 0.5) &= 1216 \\\\
    R_2' &= R_2 + K(S_2 - Expected_2) &= 1200 + 32(0 - 0.5) &= 1184
    \end{aligned}
$$

And, viola, Player One's score goes up by 16 and Player Two's score decreases
by 16. And so we now have:

| Player       | Provisional Score | Score After Round 1 |
| ------------ | ----------------- | ------------------- |
| Player One   | 1,200             | 1,216               |
| Player Two   | 1,200             | 1,184               |
| Player Three | 1,200             | 1,184               |
| Player Four  | 1,200             | 1,216               |

Next time Player One goes up against Player Two, the expected outcome won't be
50/50. Because Player One's rating is now higher than Player Two's, his or her
odds of winning the game are slightly higher. Eventually, after enough players
complete in enough games,
[you wind up with lists like this one](http://ratings.fide.com/top.phtml) and --
even if one player has never played another on this list -- you know who is more
likely to win.

### Restaurant Ratings

And so I began a death match with my restaurants. I created a script that
plucked two restaurants from my list at random and smashed them head-to-head,
asking me which was best. If I couldn't decide, they tied (can you see how a tie
would work in the formulas above?)

Over time, I answered this question hundreds of times. Eventually, my favorites
began to emerge.

What's so fun about this -- and by fun, I mean incredibly nerdy and arduous --
is that these rankings develop with my tastes. As I begin favoring one
restaurant over another, that starts a shift that can moves scores of
restaurants up or down the list.

Here's my top 30 (bearing in mind, of course, that I haven't been to most
restaurants in New York!). I should warn you: I'm partial to pizza.
Additionally, some of these restaurants are rather new to my list and may have
soared a bit too high; after they play a few more matches, they'll find the
correct position. To calculate these ratings, I didn't use Elo. I used the
slightly more sophisticated
[Glicko rating system](http://en.wikipedia.org/wiki/Glicko_rating_system).

| Rank | Restaurant                 | Rating | Games | Wins | Draws | Losses |
| ---- | -------------------------- | ------ | ----- | ---- | ----- | ------ |
| 1    | Lucali                     | 1,739  | 58    | 58   | 0     | 0      |
| 2    | Daniel                     | 1,681  | 55    | 52   | 0     | 3      |
| 3    | Babbo Ristorante e Enoteca | 1,675  | 7     | 6    | 1     | 0      |
| 4    | Bar Room at The Modern     | 1,671  | 15    | 13   | 1     | 1      |
| 5    | Morimoto                   | 1,657  | 8     | 7    | 1     | 0      |
| 6    | Aldea                      | 1,639  | 58    | 54   | 0     | 4      |
| 7    | Marea                      | 1,612  | 58    | 52   | 0     | 6      |
| 8    | Gramercy Tavern            | 1,584  | 47    | 40   | 0     | 7      |
| 9    | Jane                       | 1,579  | 12    | 11   | 0     | 1      |
| 10   | Le Bernardin               | 1,572  | 7     | 6    | 1     | 0      |
| 11   | ABC Kitchen                | 1,571  | 10    | 7    | 3     | 0      |
| 12   | Frank Restaurant           | 1,565  | 53    | 44   | 0     | 9      |
| 13   | Keste Pizza & Vino         | 1,550  | 52    | 45   | 1     | 6      |
| 14   | St. Anselm                 | 1,516  | 56    | 47   | 0     | 9      |
| 15   | A Voce                     | 1,509  | 52    | 40   | 0     | 12     |
| 16   | Paulie Gee’s               | 1,499  | 59    | 45   | 0     | 14     |
| 17   | Wallsé                     | 1,497  | 57    | 44   | 1     | 12     |
| 18   | Lure Fishbar               | 1,492  | 51    | 40   | 0     | 11     |
| 19   | Supper Restaurant          | 1,484  | 52    | 38   | 0     | 14     |
| 20   | LIC Market                 | 1,474  | 52    | 38   | 0     | 14     |
| 21   | Giuseppina's               | 1,472  | 49    | 36   | 1     | 12     |
| 22   | Locanda Verde              | 1,466  | 56    | 45   | 1     | 10     |
| 23   | Peter Luger Steak House    | 1,458  | 6     | 3    | 2     | 1      |
| 24   | BLT Steak                  | 1,455  | 48    | 36   | 0     | 12     |
| 25   | Lombardi's Pizza           | 1,450  | 17    | 13   | 1     | 3      |
| 26   | Rubirosa                   | 1,443  | 9     | 6    | 0     | 3      |
| 27   | Murray's Cheese Bar        | 1,436  | 9     | 4    | 4     | 1      |
| 28   | The Smith                  | 1,427  | 43    | 32   | 0     | 11     |
| 29   | Reynard                    | 1,380  | 7     | 3    | 1     | 3      |
| 30   | Freemans Restaurant        | 1,371  | 52    | 32   | 1     | 19     |

#### Going Further

I imagine this data can be used for taste profiles. I'd like to build a
FourSquare app. If anyone has any other thoughts, I'd love to hear them in the
comments.
