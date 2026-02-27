from __future__ import annotations

import html

import pandas as pd
import streamlit.components.v1 as components


def render_cinematic_top10(top10: pd.DataFrame) -> None:
    rows_html = []
    for idx, row in top10.reset_index(drop=True).iterrows():
        rank = idx + 1
        top3_class = "top3" if rank <= 3 else ""
        rating = float(row["Rating"])
        # Absolute 0-10 scale: 5 -> 50%, 8 -> 80%, 10 -> 100%.
        width_pct = max(0.0, min(100.0, (rating / 10.0) * 100.0))

        safe_title = html.escape(str(row["Title"]).upper())
        safe_genre = html.escape(str(row["Genre"]))
        safe_year = int(row["Year"]) if pd.notna(row["Year"]) else "-"

        rows_html.append(
            (
                f'<div class="cinema-item {top3_class}" style="animation-delay:{0.03 * rank:.2f}s;">'
                f'<div class="cinema-rank-bg">{rank:02d}</div>'
                f'<div class="cinema-name">{safe_title}</div>'
                f'<div class="cinema-meta">{safe_year} &bull; {safe_genre}</div>'
                '<div class="cinema-row">'
                f'<div class="cinema-bar-track"><div class="cinema-bar-fill" style="width:{width_pct:.1f}%"></div></div>'
                f'<div class="cinema-rating">{rating:.1f} &#9733;</div>'
                "</div></div>"
            )
        )

    html_block = f"""
    <style>
      body {{
        margin: 0; background: transparent; font-family: "Segoe UI", Arial, sans-serif;
      }}
      .cinema-board {{
        position: relative;
        background:
          radial-gradient(circle at 50% 40%, rgba(198,164,55,0.12) 0%, rgba(13,13,13,0.95) 45%, #0D0D0D 75%),
          repeating-linear-gradient(0deg, rgba(255,255,255,0.012) 0px, rgba(255,255,255,0.012) 1px, transparent 2px, transparent 4px);
        border: 1px solid rgba(198,164,55,0.25);
        border-radius: 16px;
        padding: 20px 22px 16px 22px;
        overflow: hidden;
        color: #F5F5F5;
      }}
      .cinema-board:before {{
        content: "";
        position: absolute; left: 12px; top: 14px; bottom: 14px; width: 2px;
        background: linear-gradient(180deg, #7E6410 0%, #C6A437 45%, #E4C85F 100%);
        opacity: 0.85;
      }}
      .cinema-title-main {{ margin-left: 16px; line-height: 1.06; }}
      .cinema-top {{ color: #C6A437; font-size: 1.25rem; font-weight: 800; letter-spacing: 0.08em; }}
      .cinema-movies {{ color: #F5F5F5; font-size: 1.0rem; font-weight: 650; letter-spacing: 0.04em; margin-top: 2px; }}
      .cinema-sub {{ color: #9A9A9A; font-size: 0.8rem; margin-top: 2px; letter-spacing: 0.03em; }}
      .cinema-rule {{
        margin-left: 16px; margin-top: 9px; margin-bottom: 12px;
        width: 180px; height: 1px;
        background: linear-gradient(90deg, #C6A437 0%, rgba(198,164,55,0.15) 100%);
      }}
      .cinema-item {{
        position: relative;
        margin-left: 16px;
        padding: 10px 10px 10px 18px;
        border-radius: 12px;
        animation: fadeSlide .45s ease both;
      }}
      .cinema-item.top3 {{
        padding-top: 13px; padding-bottom: 13px; margin-top: 5px; margin-bottom: 5px;
        box-shadow: inset 0 0 0 1px rgba(198,164,55,0.20), 0 0 18px rgba(198,164,55,0.07);
      }}
      .cinema-rank-bg {{
        position: absolute; left: 2px; top: 1px;
        font-size: 2.7rem; font-weight: 800;
        background: linear-gradient(180deg, rgba(198,164,55,0.72) 0%, rgba(245,197,24,0.20) 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        letter-spacing: 0.02em; line-height: 1;
      }}
      .cinema-item.top3 .cinema-rank-bg {{
        font-size: 3.05rem;
        background: linear-gradient(180deg, rgba(198,164,55,0.95) 0%, rgba(245,197,24,0.42) 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
      }}
      .cinema-name {{
        color: #F5F5F5; font-size: 0.96rem; font-weight: 720; letter-spacing: 0.07em;
        text-transform: uppercase; margin-left: 56px; margin-bottom: 3px;
      }}
      .cinema-meta {{ color: #9A9A9A; font-size: 0.78rem; margin-left: 56px; margin-bottom: 7px; }}
      .cinema-row {{ display: flex; align-items: center; margin-left: 56px; gap: 10px; }}
      .cinema-bar-track {{
        flex: 1; height: 8px; border-radius: 999px; background: rgba(255,255,255,0.12); overflow: hidden;
      }}
      .cinema-item.top3 .cinema-bar-track {{ height: 10px; }}
      .cinema-bar-fill {{
        height: 100%; border-radius: 999px;
        background: linear-gradient(90deg, #7A6110 0%, #C6A437 45%, #F5C518 100%);
        box-shadow: 0 1px 6px rgba(198,164,55,0.35);
      }}
      .cinema-rating {{
        min-width: 68px; text-align: center; color: #111111; font-size: 0.8rem; font-weight: 760;
        background: linear-gradient(180deg, #E2C150 0%, #C6A437 100%);
        border-radius: 999px; padding: 3px 8px; box-shadow: 0 2px 8px rgba(198,164,55,0.33);
      }}
      @keyframes fadeSlide {{
        from {{ opacity: 0; transform: translateY(7px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
    </style>
    <div class="cinema-board">
      <div class="cinema-title-main">
        <div class="cinema-top">TOP 10</div>
        <div class="cinema-movies">MOVIES</div>
        <div class="cinema-sub">by IMDb Rating</div>
      </div>
      <div class="cinema-rule"></div>
      {''.join(rows_html)}
    </div>
    """

    # Dynamic height avoids dead vertical space when filters return fewer rows.
    n = max(1, len(top10))
    top3_count = min(3, n)
    regular_count = n - top3_count
    # Conservative sizing to avoid clipping the last row across different fonts/OS.
    header_px = 154
    top3_row_px = 96
    regular_row_px = 80
    container_padding_px = 44
    dynamic_height = header_px + (top3_count * top3_row_px) + (regular_count * regular_row_px) + container_padding_px
    dynamic_height = max(280, min(1200, dynamic_height))

    # Dedicated HTML component prevents markdown escaping issues.
    components.html(html_block, height=dynamic_height, scrolling=False)
