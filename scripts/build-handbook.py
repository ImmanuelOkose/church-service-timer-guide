"""Build only public training content from teaching.md. No app source is copied."""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.18.0"
UPDATED = "21 October 2026"
GROUPS = [(0, 3, "Begin here"), (3, 6, "Connect the room"),
          (6, 11, "Run the service"), (11, 15, "Review & maintain"),
          (15, 17, "Train your team")]
SUMMARIES = [
    "Know the four tabs, the operator clock and what a display acknowledgement really means.",
    "Practice the complete service workflow in the simulator, without touching the stage.",
    "Create a reusable plan with segments, speakers, notes and its own end screen.",
    "Understand when to choose Simulator, LED sign, or Phone or tablet.",
    "Join the right Wi-Fi, authenticate the supported W2 and understand its limits.",
    "Approve stage screens and operators, assign layouts, and manage saved devices.",
    "Start, pause, adjust, advance and blank with clear control of the service.",
    "Prepare one-tap instructions and configure warnings based on time remaining.",
    "Target a mobile stage screen, format the message and request explicit Seen.",
    "Review future timing changes and learn from comparable completed services.",
    "End once, save the report and recover cleanly from a saving failure.",
    "Read the record, export it, and print the right copy with notes kept private.",
    "Set the church profile, banner and appearance; understand shared defaults.",
    "Diagnose a stale screen, lost connection, missing warning or rejected command.",
    "Back up your setup and understand the boundaries of LED administration.",
    "Coach a new operator through a practical session and a readiness checklist.",
    "Look up terms, check your understanding and review the current scope.",
]


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="build/handbook")
    args = parser.parse_args()
    out = (ROOT / args.output).resolve()
    if out == ROOT or out in ROOT.parents or not out.is_relative_to(ROOT):
        raise SystemExit("Output must be a subdirectory inside the checkout.")
    source = (ROOT / "teaching.md").read_text(encoding="utf-8")
    parts = re.split(r"(?m)^## (\d{2}) — (.+)\n", source)
    chapters = []
    for i in range(1, len(parts), 3):
        number, title, body = parts[i:i + 3]
        chapters.append({"number": number, "title": title, "body": body,
                         "slug": slug(title), "anchor": number + "-" + slug(title)})
    if len(chapters) != len(SUMMARIES):
        raise SystemExit("Update chapter summaries and grouping when adding lessons.")
    for chapter, summary in zip(chapters, SUMMARIES):
        chapter["summary"] = summary
    out.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT / "site/assets", out / "assets", dirs_exist_ok=True)
    (out / ".nojekyll").write_text("", encoding="utf-8")
    (out / "teaching.md").write_text(source.replace("site/assets/", "assets/"), encoding="utf-8")
    anchors = {c["anchor"]: c["slug"] + ".html" for c in chapters}

    def render(body, whole=False):
        body = body.replace("site/assets/", "assets/")
        if not whole:
            for anchor, destination in anchors.items():
                body = body.replace("](#" + anchor + ")", "](" + destination + ")")
        converter = markdown.Markdown(extensions=["tables", "fenced_code", "toc"])
        content = converter.convert(body)
        content = re.sub(r"<table>(.*?)</table>", r'<div class="table-scroll" role="region" aria-label="Reference table" tabindex="0"><table>\1</table></div>', content, flags=re.S)
        def image_figure(match):
            alt, src = match.group(1), match.group(2)
            return ('<figure class="app-figure"><a class="zoom-image" href="' + src +
                    '" aria-label="Enlarge: ' + alt + '"><img src="' + src +
                    '" alt="' + alt + '" loading="lazy" decoding="async"></a><figcaption>' +
                    alt + '<span>Example app preview · tap to enlarge</span></figcaption></figure>')
        content = re.sub(r'<p><img alt="([^"]*)" src="([^"]*)" /></p>', image_figure, content)
        return content, converter.toc_tokens

    def navigation(active):
        rows = ['<a class="nav-home' + (' selected' if active == "index" else '') +
                '" href="index.html">Handbook overview</a>']
        for start, end, label in GROUPS:
            rows.append('<p class="nav-group">' + label + '</p>')
            for c in chapters[start:end]:
                selected = c["slug"] == active
                rows.append('<a href="' + c["slug"] + '.html" data-lesson="' + c["slug"] +
                            '"' + (' aria-current="page" class="selected"' if selected else "") +
                            '><span class="lesson-number">' + c["number"] + '</span><span>' +
                            html.escape(c["title"]) + '</span><span class="lesson-check" aria-hidden="true"></span></a>')
        return "\n".join(rows)

    def shell(title, active, body, description):
        return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · Church Service Timer Handbook</title>
<meta name="description" content="{html.escape(description, quote=True)}">
<meta name="theme-color" content="#11271e">
<meta name="color-scheme" content="light">
<meta property="og:title" content="{html.escape(title, quote=True)} · Church Service Timer">
<meta property="og:description" content="{html.escape(description, quote=True)}">
<meta property="og:type" content="website">
<link rel="icon" href="assets/chapel.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/handbook.css">
<script defer src="assets/handbook.js"></script>
</head>
<body data-page="{active}">
<a class="skip-link" href="#main">Skip to content</a>
<header class="topbar">
<a class="brand" href="index.html"><img src="assets/chapel.svg" width="42" height="42" alt=""><span>Church Service Timer<small>THE OPERATOR HANDBOOK</small></span></a>
<div class="header-actions"><span class="version">ANDROID {VERSION}</span><a class="download" href="teaching.md" download>Download guide <span aria-hidden="true">↙</span></a>
<button class="menu-button" type="button" aria-controls="sidebar" aria-expanded="false">Lessons <span aria-hidden="true">☰</span></button></div>
</header>
<div class="layout">
<aside class="sidebar" id="sidebar" aria-label="Handbook navigation">
<div class="search-wrap"><label for="search">Find an answer</label><input id="search" type="search" placeholder="Try “pairing” or “watermark”" autocomplete="off" aria-controls="search-results"><p id="search-status" class="sr-only" role="status"></p><div id="search-results" hidden></div></div>
<nav aria-label="Lessons">{navigation(active)}</nav>
<div class="learning-progress"><p><strong id="progress-count">0 of 17</strong> lessons marked read</p><progress id="progress" max="17" value="0" aria-label="Lessons marked read"></progress><button type="button" id="reset-progress">Reset my progress</button><small>Saved only in this browser.</small></div>
<a class="full-guide-link" href="complete-guide.html">Full guide & printing <span aria-hidden="true">↗</span></a>
</aside>
<main id="main" tabindex="-1">{body}
<footer class="page-footer"><img src="assets/chapel.svg" width="30" height="30" alt=""><p><strong>Church Service Timer · I-Proton</strong><span>Handbook for {VERSION} · Updated {UPDATED}</span></p><a href="quick-reference-and-knowledge-check.html#current-scope">Scope & limitations</a></footer>
</main></div>
<dialog id="image-dialog" aria-label="Enlarged app screenshot"><button type="button" class="close-dialog" aria-label="Close enlarged screenshot">Close ✕</button><img alt=""><p></p></dialog>
<noscript><div class="noscript-note">All lessons and the full guide work without JavaScript. Search, progress tracking and the practice quiz need JavaScript.</div></noscript>
</body></html>'''

    search_items = []
    for idx, c in enumerate(chapters):
        content, toc = render(c["body"])
        minutes = max(2, round(len(c["body"].split()) / 180))
        subnav = "".join('<a href="#' + html.escape(t["id"], quote=True) + '">' +
                         html.escape(t["name"]) + '</a>' for t in toc)
        previous = chapters[idx - 1] if idx else None
        following = chapters[idx + 1] if idx + 1 < len(chapters) else None
        prev_link = ('<a href="' + previous["slug"] + '.html"><span>PREVIOUS LESSON</span>' +
                     html.escape(previous["title"]) + '</a>') if previous else '<a href="index.html"><span>START HERE</span>Handbook overview</a>'
        next_link = ('<a href="' + following["slug"] + '.html"><span>NEXT LESSON</span>' +
                     html.escape(following["title"]) + ' →</a>') if following else '<a href="index.html"><span>KEEP IT CLOSE</span>Return to handbook →</a>'
        body = f'''<div class="chapter-shell"><header class="chapter-header"><p class="eyebrow">LESSON {c["number"]} / 17 <span>{minutes} MIN READ</span></p>
<h1 id="{c["anchor"]}">{html.escape(c["title"])}</h1><p class="chapter-deck">{c["summary"]}</p></header>
{('<nav class="on-this-page" aria-label="On this page"><strong>In this lesson</strong>' + subnav + '</nav>') if subnav else ''}
<article class="prose">{content}</article>
<div class="lesson-complete"><div><strong>A moment to reflect.</strong><p>Could you explain this workflow to another operator?</p></div><button type="button" data-complete="{c["slug"]}" aria-pressed="false">Mark lesson as read</button></div>
<nav class="chapter-pagination" aria-label="Lesson pagination">{prev_link}{next_link}</nav></div>'''
        if idx == 16:
            body = body.replace('<div class="lesson-complete">', quiz_html() + '<div class="lesson-complete">')
        (out / (c["slug"] + ".html")).write_text(shell(c["title"], c["slug"], body, c["summary"]), encoding="utf-8")
        search_items.append({"title": c["title"], "number": c["number"], "url": c["slug"] + ".html",
                             "summary": c["summary"], "text": re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", content))})
    (out / "search-index.json").write_text(json.dumps(search_items, ensure_ascii=False), encoding="utf-8")
    full, _ = render(source, whole=True)
    full = re.sub(r'<h1.*?</h1>', "", full, count=1, flags=re.S)
    whole_body = '<div class="chapter-shell complete-guide"><header class="chapter-header"><p class="eyebrow">THE COMPLETE HANDBOOK</p><h1>One guide. Every workflow.</h1><p class="chapter-deck">Read every lesson here, or print this page for a training session.</p><button class="primary-button" type="button" id="print-guide">Print this handbook</button></header><article class="prose">' + full + '</article></div>'
    (out / "complete-guide.html").write_text(shell("Complete teaching guide", "complete", whole_body, "The full operator training guide, ready to read or print."), encoding="utf-8")
    lessons = "".join('<a class="chapter-row" href="' + c["slug"] + '.html"><span>' + c["number"] +
                      '</span><div><h3>' + html.escape(c["title"]) + '</h3><p>' + c["summary"] +
                      '</p></div><span aria-hidden="true">↗</span></a>' for c in chapters)
    homepage = f'''<section class="hero"><div class="hero-copy"><p class="eyebrow">THE OPERATOR HANDBOOK · {VERSION}</p><h1>Know the controls.<br><em>Care for the room.</em></h1><p>From your first rehearsal to the final report. A practical guide to timing the service and communicating clearly with the stage.</p><a class="primary-button" href="your-first-rehearsal.html">Start your first rehearsal <span aria-hidden="true">→</span></a><a class="hero-secondary" href="trainer-session-and-readiness-checklist.html">Teaching a team? Open the trainer checklist</a><div class="hero-facts"><span>17 focused lessons</span><span>Real app previews</span><span>No sign needed to begin</span></div></div>
<div class="hero-visual"><div class="visual-caption"><span class="live-dot"></span> ONE SERVICE. ONE CLEAR PLAN.</div><img class="hero-phone" src="assets/images/live.png" width="420" height="900" alt="Church Service Timer Live example showing a one-minute rehearsal countdown"><div class="visual-note"><span>FIRST THING TO KNOW</span><strong>The timer and the output<br>are different checks.</strong><a href="understand-the-workspace.html">Learn the workspace →</a></div></div></section>
<section class="start-paths"><div class="section-intro"><p class="eyebrow">FIND YOUR STARTING POINT</p><h2>Your role. Your route.</h2></div><div class="path-list">
<a href="your-first-rehearsal.html"><span class="path-symbol">01</span><div><h3>I’m a new operator</h3><p>Learn the workspace, rehearse safely, then run a service.</p></div><span aria-hidden="true">→</span></a>
<a href="pair-a-phone-or-tablet.html"><span class="path-symbol">02</span><div><h3>I’m setting up the screens</h3><p>Choose the output, pair devices and confirm who has control.</p></div><span aria-hidden="true">→</span></a>
<a href="trainer-session-and-readiness-checklist.html"><span class="path-symbol">03</span><div><h3>I’m training the team</h3><p>Use the session plan, drills and readiness checklist.</p></div><span aria-hidden="true">→</span></a></div></section>
<section class="three-truths"><p class="eyebrow">THREE IDEAS THAT PREVENT CONFUSION</p><div><article><span>01 / PLAN</span><h3>A program is reusable.<br>A service is one run.</h3><p>Live adjustments don’t rewrite your saved plan or old reports.</p></article><article><span>02 / OUTPUT</span><h3>Pause stops time.<br>Blank hides the screen.</h3><p>A moving arc alone doesn’t prove the physical sign is current.</p></article><article><span>03 / PEOPLE</span><h3>Synced is delivery.<br>Seen is a person.</h3><p>Ask for explicit acknowledgement when an instruction needs it.</p></article></div></section>
<section class="curriculum"><div class="section-intro"><p class="eyebrow">THE COMPLETE LEARNING PATH</p><h2>From preparation to handover.</h2><p>Read in order, or use search to find the answer you need during a rehearsal.</p></div>{lessons}</section>
<section class="ready-strip"><div><p class="eyebrow">KEEP A COPY AT THE DESK</p><h2>Your next operator starts here.</h2><p>Download teaching.md, print the complete handbook, or share this site with your team.</p></div><a class="primary-button" href="complete-guide.html">Open the complete guide →</a></section>'''
    (out / "index.html").write_text(shell("Learn to run a service", "index", homepage, "The practical Church Service Timer handbook: rehearse, connect screens, run the service and understand your reports."), encoding="utf-8")
    notfound = '<div class="chapter-shell"><header class="chapter-header"><p class="eyebrow">PAGE NOT FOUND</p><h1>Let’s get you back to the desk.</h1><p>This lesson may have moved. Use the navigation or search to find it.</p><a class="primary-button" href="index.html">Open the handbook</a></header></div>'
    (out / "404.html").write_text(shell("Page not found", "404", notfound, "Return to the Church Service Timer handbook."), encoding="utf-8")
    print(f"Built {len(chapters)} lessons, overview, full guide, search index and 404 in {out}")


def quiz_html():
    return '''<section class="quiz" aria-labelledby="quiz-title"><p class="eyebrow">PRACTICE WITHOUT THE PHONE</p><h2 id="quiz-title">Three quick scenarios.</h2>
<form id="knowledge-quiz">
<fieldset><legend>1. You blank the stage screen. What happens to time?</legend><label><input type="radio" name="q1" value="pause" required> The service pauses.</label><label><input type="radio" name="q1" value="continue"> The service keeps counting.</label></fieldset>
<fieldset><legend>2. An approved operator reconnects. Who has control?</legend><label><input type="radio" name="q2" value="peer" required> The returning operator automatically.</label><label><input type="radio" name="q2" value="host"> The host until it explicitly grants control.</label></fieldset>
<fieldset><legend>3. You need to know an instruction was read. What should you look for?</legend><label><input type="radio" name="q3" value="synced" required> A Synced status alone.</label><label><input type="radio" name="q3" value="seen"> The recipient’s explicit Seen acknowledgement.</label></fieldset>
<button type="submit" class="primary-button">Check my answers</button><p id="quiz-result" role="status"></p></form></section>'''


if __name__ == "__main__":
    main()
