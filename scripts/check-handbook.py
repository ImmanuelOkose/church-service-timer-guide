"""Validate the generated public handbook, links, images and publication boundary."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
        self.duplicate_ids = []
        self.missing_alt = []
        self.h1s = 0
        self.main = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            if a["id"] in self.ids:
                self.duplicate_ids.append(a["id"])
            self.ids.add(a["id"])
        if tag == "h1":
            self.h1s += 1
        if tag == "main":
            self.main += 1
        if tag in {"a", "link", "script", "img"}:
            url = a.get("href") or a.get("src")
            if url:
                self.links.append(url)
        if tag == "img" and "alt" not in a:
            self.missing_alt.append(a.get("src"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", nargs="?", default="build/handbook")
    args = parser.parse_args()
    root = Path(args.folder).resolve()
    pages = {}
    errors = []
    for file in root.rglob("*.html"):
        page = Page()
        text = file.read_text(encoding="utf-8")
        page.feed(text)
        pages[file] = page
        if page.h1s != 1 or page.main != 1:
            errors.append(f"{file.name}: needs exactly one h1 and main")
        if page.duplicate_ids or page.missing_alt:
            errors.append(f"{file.name}: duplicate IDs {page.duplicate_ids} or missing image alt {page.missing_alt}")
        if re.search(r"BEGIN [A-Z ]*PRIVATE KEY|C:\\Users\\|CST1:|/home/kosenuel|id_rsa", text):
            errors.append(f"{file.name}: private-machine or credential material")
    for file, page in pages.items():
        for url in page.links:
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                if parsed.scheme not in {"https", "mailto"}:
                    errors.append(f"{file.name}: unexpected scheme {url}")
                continue
            destination = (file.parent / unquote(parsed.path)).resolve() if parsed.path else file
            if not destination.is_relative_to(root) or not destination.is_file():
                errors.append(f"{file.name}: missing or out-of-root target {url}")
            elif parsed.fragment and destination in pages and unquote(parsed.fragment) not in pages[destination].ids:
                errors.append(f"{file.name}: missing anchor {url}")
    index = json.loads((root / "search-index.json").read_text(encoding="utf-8"))
    if len(index) != 17 or len(pages) != 20:
        errors.append(f"Unexpected lesson/page count: {len(index)} / {len(pages)}")
    for item in index:
        if not (root / item["url"]).is_file() or not item["text"]:
            errors.append("Search result has missing page or text")
    if not (root / "teaching.md").is_file():
        errors.append("Missing downloadable teaching.md")
    for file in root.rglob("*"):
        if file.is_file() and file.suffix.lower() not in {".html", ".json", ".md", ".css", ".js", ".svg", ".png", ""} and file.name != ".nojekyll":
            errors.append(f"Unexpected publishable file: {file.relative_to(root)}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(pages)} HTML pages; 17 searchable lessons; internal links, anchors, image alt and public-output boundary checked.")


if __name__ == "__main__":
    main()
