#!/home/villares/thonny-env/bin/python

"""
createRSS.py
Reads index.html page and writes feed.xml (RSS 2.0) to the same directory.

Usage:
    createRSS.py   # by defaut reads …sketch-a-day/index.html, writes feed.xml.
    createRSS.py path/to/index.html path/to/feed.xml
"""

import re
import sys
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from html.parser import HTMLParser

DEFAULT_INDEX = Path('/home/villares/GitHub/sketch-a-day_build/index.html')
BASE_URL   = "https://abav.lugaralgum.com/sketch-a-day"
FEED_TITLE = "sketch-a-day – Alexandre B A Villares"
FEED_DESC  = "Coding a visual idea a day"
FEED_LANG  = "en"
MAX_ITEMS  = 1000          # how many recent sketches to include in the feed

# ── helpers ────────────────────────────────────────────────────────────────────

SKETCH_ID_RE = re.compile(r"^sketch_(\d{4})_(\d{2})_(\d{2})$")


def sketch_id_to_date(sketch_id: str) -> datetime:
    """Convert 'sketch_2026_04_26' → datetime(2026, 4, 26, tzinfo=UTC)."""
    m = SKETCH_ID_RE.match(sketch_id)
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return datetime(y, mo, d, 12, 0, 0, tzinfo=timezone.utc)


def xml_escape(text: str) -> str:
    return (text
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


# ── HTML parsing ───────────────────────────────────────────────────────────────

class SketchParser(HTMLParser):
    """
    Walks the HTML and collects sketch entries.

    Each entry:
        {
            "id":    "sketch_2026_04_26",
            "date":  datetime(...),
            "img":   "2026/sketch_2026_04_26/sketch_2026_04_26.png",
            "link":  "https://github.com/...",
            "desc":  "optional description text",
        }
    """

    def __init__(self):
        super().__init__()
        self.sketches: list[dict] = []
        self._current: dict | None = None   # entry being built
        self._in_h3 = False                 # inside <h3 id="sketch_…">
        self._p_index = 0                   # which <p> after the h3 we're in
        self._in_p = False
        self._p_text_buf: list[str] = []
        self._in_a = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "h3":
            sid = attrs.get("id", "")
            if SKETCH_ID_RE.match(sid):
                # commit previous entry if any
                self._commit()
                self._current = {"id": sid, "date": sketch_id_to_date(sid),
                                 "img": "", "link": "", "desc": ""}
                self._p_index = 0
                self._in_h3 = True
            return
        if tag == "p" and self._current:
            self._in_p = True
            self._p_index += 1
            self._p_text_buf = []
            return
        if tag == "img" and self._current and self._in_p and self._p_index == 1:
            self._current["img"] = attrs.get("src", "")
            return
        if tag == "a" and self._current and self._in_p:
            self._in_a = True
            if self._p_index == 2 and not self._current["link"]:
                href = attrs.get("href", "")
                # the first <a> in the second <p> is the source link
                if "github.com" in href or "codeberg.org" in href:
                    self._current["link"] = href
            return
        # a new h3 that isn't a sketch (e.g. a section header) resets state
        if tag == "h3" and self._current:
            self._commit()

    def handle_endtag(self, tag):
        if tag == "h3":
            self._in_h3 = False

        if tag == "a":
            self._in_a = False

        if tag == "p" and self._current and self._in_p:
            # third (and later) <p> tags are optional description text
            if self._p_index >= 3:
                txt = "".join(self._p_text_buf).strip()
                if txt:
                    self._current["desc"] = (self._current["desc"] + " " + txt).strip()
            self._in_p = False

        # <hr/> between entries: commit whatever is pending
        if tag == "hr" and self._current:
            self._commit()

    def handle_data(self, data):
        if self._in_p and self._current:
            self._p_text_buf.append(data)

    def _commit(self):
        if self._current and self._current["img"]:
            self.sketches.append(self._current)
        self._current = None
        self._in_h3 = False
        self._in_p = False
        self._p_index = 0

def build_rss(sketches: list[dict]) -> str:
    now_rfc = format_datetime(datetime.now(timezone.utc))
    items_xml = []
    for s in sketches[:MAX_ITEMS]:
        sid        = s["id"]
        page_url   = f"{BASE_URL}/#{xml_escape(sid)}"
        img_src    = s["img"]
        # make image URL absolute if it isn't already
        if not img_src.startswith("http"):
            img_src = f"{BASE_URL}/{img_src}"
        repo_url = xml_escape(s["link"]) if s["link"] else ""
        desc_text  = xml_escape(s["desc"]) if s["desc"] else ""
        pub_date   = format_datetime(s["date"])
        # build HTML description
        desc_html_parts = [f'<img src="{xml_escape(img_src)}" alt="{xml_escape(sid)}" style="max-width:100%"/>']
        if desc_text:
            desc_html_parts.append(f"<p>{desc_text}</p>")
        if repo_url:
            desc_html_parts.append(f'<p><a href="{repo_url}">linkt to source</a></p>')
        desc_html = "".join(desc_html_parts)

        items_xml.append(f"""
  <item>
    <title>{xml_escape(sid)}</title>
    <link>{xml_escape(page_url)}</link>
    <guid isPermaLink="true">{xml_escape(page_url)}</guid>
    <pubDate>{pub_date}</pubDate>
    <description><![CDATA[{desc_html}]]></description>
  </item>""")
    #  <enclosure url="{xml_escape(img_src)}" type="image/{'gif' if img_src.endswith('.gif') else 'png'}" length="0"/>
    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>{xml_escape(FEED_TITLE)}</title>
  <link>{xml_escape(BASE_URL)}</link>
  <description>{xml_escape(FEED_DESC)}</description>
  <language>{FEED_LANG}</language>
  <lastBuildDate>{now_rfc}</lastBuildDate>
  <atom:link href="{xml_escape(BASE_URL)}/feed.xml" rel="self" type="application/rss+xml"/>
{"".join(items_xml)}
</channel>
</rss>
"""
    return feed

if __name__ == "__main__":
    input_path  = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INDEX
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path.parent / "feed.xml"
    html = input_path.read_text(encoding="utf-8")
    parser = SketchParser()
    parser.feed(html)
    parser.handle_endtag("hr")   # flush last pending entry
    sketches = parser.sketches
    print(f"Found {len(sketches)} sketches... ", end='')
    if sketches:
        sketches.sort(key=lambda s: s["date"], reverse=True) # in case the HTML is reversed
        rss = build_rss(sketches)
        output_path.write_text(rss, encoding="utf-8")
        print(f"Wrote feed to {output_path}.")
        s = sketches[0]
        print(f"Latest:  {s['id']}  img={s['img']}  desc={s['desc']!r}")
    else:
        print(f'{output_path} was not touched.')
