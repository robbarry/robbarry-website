---
title: "Thoughts on AI"
date: 2026-03-28
description: "We got a signal from outer space. Now we're trying to pull the alien intelligence all the way through a portal and onto Earth, and I'm not sure we're thinking hard enough about what happens when it arrives."
---

The most common question I get about AI is some version of "does it save time?" And I think that's the wrong question. It's not that AI makes existing work faster. It's that AI makes previously impossible work possible. That's a different thing entirely.

Over the summer we did a story on fume events — instances where engine exhaust leaks into aircraft cabins and makes people sick. The raw material was about a million FAA service difficulty reports, free-form text written by airline crews and maintenance staff. There's no structure to these documents. People describe the same problem a hundred different ways. They say it smells like dirty socks. They say passengers felt nauseous. They use technical language, colloquial language, every kind of language. Nobody was going to sit down and read a million of those reports. Not in weeks, not in months. It just wasn't going to happen.

But we could teach an AI what a fume event looks like — feed it technical documentation, give it examples — and have it classify every single document. And it was pretty accurate. We verified with other methods. That's a great AI problem: a clear objective applied against a large corpus of unstructured information. That story exists because of AI. It's not that we did it faster. We did it at all.

That's the baseline use case for my team. Large-scale processing of documents and information that would otherwise be impractical to touch. And AI is layered throughout the whole process — we use it to help build the tools, then distribute those tools with AI-readable instructions so other people in the newsroom can deploy them. None of that has an analog in the pre-AI world. There's no "before" version that took longer.

## Where it works and where it doesn't

A lot of people across a lot of organizations don't have any real perception of where AI is useful and where it's not. They just sense that it's a magic thing that's always maybe going to make something easier. So a lot of my job is refining that. Somebody says "can we use AI to scrape every social media post?" and the answer is: what's the question? What's the goal? AI doesn't just do that. You learn by doing where this technology pans out and produces useful stuff and where it spins wheels.

Classification against a clear objective — that works. Structured extraction from unstructured text — that works. Synthesizing large volumes of notes or interviews — that works. Freeform problems with no defined goal — that doesn't work. And I think the instinct to just throw AI at a vague problem because it feels productive is one of the bigger time traps that people fall into.

## The story-first filter

We have a simple rubric: is this moving toward a story? A story in whatever format — text, video, visual, interactive. When we're doing work, it needs to be generally in the service of that. As simple as that sounds, it's a surprisingly effective filter.

Newsrooms that develop technical capabilities have a tendency to drift. People build cool widgets that interest them. They pursue experiments that don't connect to anything the newsroom actually needs. And AI makes this worse, because the surface area of possible work expands enormously. When anything is possible, you have to be thoughtful about where to direct energy. The story-first filter kills the shiny-tool problem before it starts.

The first pass is always: is this a good story? Is this an important effort? Is this something people are going to read? Then layered on top of that: does the idea fit what AI is actually good at? If both answers are yes, we go. If either is no, we probably don't.

## The sensitivity problem

Here's something the public conversation about AI in newsrooms mostly ignores: investigative journalists generate material you fundamentally cannot send to a third-party API.

We don't record our internal meetings. We're careful about what notes we take on sensitive stories. We don't feed our reporting into the big AI providers because it's sensitive information — stories about government accountability, about the tech companies themselves, about a whole range of things where the downside risk of exposure is real.

Right now the closest thing we have to a safe option is Gemini, because it falls under the same data agreement as Google Docs and email. If it's safe enough to put in a Google Doc, it's safe enough for Gemini. But Gemini doesn't have standardized workflows for this kind of use. There's no sanctioned, repeatable process. Individual reporters might figure out gems or notebooks or whatever, but it's ad hoc.

One day maybe we'll get to on-prem models good enough to handle sensitive material. We're not there yet. So there's a natural ceiling on how deeply AI can integrate into newsroom operations, and it's not a technical ceiling — it's a trust and security ceiling.

## The correction I live in fear of

I live in fear of the AI-induced correction. Somebody relies on something an AI told them, it propagates all the way through a story, and it turns out to be false. It happened recently at another publication — a fabricated quote that an AI tool attributed to someone's website. They had to retract the article and issue an apology.

That's one of the worst-case scenarios and it's a big reason why legacy newsrooms like mine have moved slowly on this technology. The downside risk to reputation is enormous. You spend decades building credibility and one hallucination that slips through can blow a hole in it.

This is also why citation matters so much. A tool like NotebookLM is useful not just because it returns results, but because it shows you where those results come from. That lets the reporter check. But if the checking process is slower than just doing the research yourself, then skip the AI and do it yourself. That tradeoff is real and it depends on how much context you already carry in your own head on a given subject.

## How we roll things out

When [Brian Whitton](https://www.wsj.com/news/author/brian-whitton) built [Orca](https://www.inma.org/best-practice/Best-Use-of-Generative-AI/2026-713/Surfacing-the-Story-How-WSJs-ORCA-Unlocks-the-Podcast-Universe) — a podcast ingestion system that does transcription and a bunch of other things — we didn't just hand it to the newsroom. We started with a small group of people we trusted to be cautious, to understand the potential downsides, to give useful feedback. We iterated. We used it on a story. And then once it was solid, we made it broadly available — a button on the newsroom interface that anyone can click. We give trainings on it occasionally.

That's the ideal progression. Small group, iterate, broaden. It's not complicated but it requires patience, which is hard to come by in a newsroom where the pressure of the day never lets up. There's never a day when you can just focus on workflows. And as newsrooms have shrunk, the opportunity to have people step back from the daily grind and think about this stuff has only gotten smaller.

## Context switching

Does AI make it easier to juggle projects? A little. You can get back up to speed faster if the AI has good context. But all of it depends on the information the AI has. If you don't spend the time getting information into the system, the AI doesn't have complete context. And if it doesn't have complete context, you risk a game of telephone where you're trusting a machine to understand things it doesn't understand.

That process of maintaining context — of keeping the AI informed — takes time. And I think there's a real risk that people skip that step, trust incomplete outputs, and wind up wasting more time than they saved. The world has not come up with AI-first workflows that truly solve this. Certainly not in journalism.

## The alien signal

When people ask me to describe my relationship with AI, I think of it like this: we got a signal from outer space. There's a sign of possible intelligence in the signal. So we started working to draw more from it. We've been tightening the connection, pulling it closer, trying to bring this alien intelligence all the way through a portal and onto Earth.

That's essentially what AGI would be. And we have no idea what happens when it arrives. If it's benevolent, maybe that's good. If it's not, maybe it's a disaster. I don't think we're pursuing a wise path as a society. We should have focused much more attention on the potential disruptions — job loss as a starting point — and on the ramifications of the end goal, if it ever arrives. Both of those things are things we are not equipped to deal with and have not made any real effort to address. We're just focused on how to make money. That's how this country has always operated. It's not a surprise. But strategically, it feels misguided here.

I worry less about my own job in the short term and more about what happens when an entire class of white-collar workers gets disenfranchised. What does that mean politically? Economically? We have a baseline assumption in this country that work is good and you should work for a living. If you introduce something that does all the work, what happens to all the people who were told they had to work?

By the time journalists are losing their jobs to AI, a lot of other people will already be having the same problem. That's not comforting. That's the point.

## Where I land

I use AI every day. My team builds AI tools. And I'm still saying: I have no idea where this goes and I don't think we're being careful enough about finding out.

In the meantime, the work is good. We're doing journalism that wouldn't exist without this technology. We're being thoughtful about where we apply it and honest about where it falls short. That's about all you can do right now — use the thing, respect the thing, and keep your eyes open.
