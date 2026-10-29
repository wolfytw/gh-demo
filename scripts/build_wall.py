"""把 Issues（JSON）轉成一頁留言牆網頁。用法：python3 build_wall.py issues.json _site"""
import html
import json
import sys
from pathlib import Path

COLORS = ["#E0A33A", "#4FB3A9", "#E9E5DA", "#C9B48A", "#8FB7E0", "#E58F73"]


def card(i, issue):
    name = html.escape(issue.get("title") or "匿名")
    msg = html.escape((issue.get("body") or "").strip()[:140]) or "（沒有留言內容）"
    login = html.escape((issue.get("author") or {}).get("login", ""))
    color = COLORS[i % len(COLORS)]
    return (
        f'<article style="border-top:6px solid {color}">'
        f"<h2>{name}</h2><p>{msg}</p><small>@{login} · #{issue.get('number')}</small></article>"
    )


def build(issues):
    issues = sorted(issues, key=lambda x: x.get("createdAt", ""), reverse=True)
    cards = "\n".join(card(i, x) for i, x in enumerate(issues))
    return f"""<!doctype html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="refresh" content="20">
<title>說明會留言牆</title>
<style>
body{{margin:0;background:#11161D;color:#E9E5DA;font-family:"Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif}}
header{{padding:40px 48px 8px}}
h1{{margin:0;font-size:48px;color:#F4F1E8}}
header p{{color:#8C97A3;font-size:20px}}
main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:20px;padding:24px 48px 48px}}
article{{background:#1A222C;border-radius:12px;padding:20px 24px;animation:pop .6s ease}}
article h2{{margin:0 0 8px;font-size:26px;color:#F4F1E8}}
article p{{margin:0 0 12px;font-size:18px;line-height:1.5}}
article small{{color:#8C97A3}}
@keyframes pop{{from{{transform:scale(.8);opacity:0}}to{{transform:scale(1);opacity:1}}}}
</style></head><body>
<header><h1>說明會留言牆 · {len(issues)} 則</h1>
<p>開一個 Issue 就會出現在這裡：GitHub Actions 自動回覆、自動重建、自動上線。頁面每 20 秒自動重新整理。</p></header>
<main>
{cards}
</main></body></html>"""


def main():
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    issues = json.loads(src.read_text(encoding="utf-8"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(build(issues), encoding="utf-8")
    print(f"wrote {out / 'index.html'} with {len(issues)} cards")


if __name__ == "__main__":
    main()
