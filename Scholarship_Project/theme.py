# theme.py — The Diverging Dream
# Cost of Living, Inequality & Family Formation in America, 1960–2024
#
# ── COLOR PHILOSOPHY ──────────────────────────────────────────────────────────
#
#   BLUE   = wages, income, things that grew fairly (the hopeful story)
#   RED    = costs that exploded, fertility decline, unaffordability (the alarm)
#   GOLD   = reference lines, annotations, median benchmarks, highlights
#   GREEN  = things that got cheaper (apparel, food, electronics — the contrast)
#   GRAY   = neutral context: headline CPI, background series, grid lines
#   PURPLE = education / tuition specifically (distinct from other cost categories)
#
#   Rule: Red should feel like a warning. Green should feel like relief.
#         Gold is the narrator's voice — thresholds, baselines, callouts.
#         Blue is the worker's story. Red is the bill they can't pay.
#
# ── BACKGROUND PHILOSOPHY ────────────────────────────────────────────────────
#
#   We use a warm off-white (#F5F0E8) as the background, not pure white or black.
#   This gives the charts a journalistic, editorial quality — like the
#   Financial Times or The Economist. It reads as serious without being cold.
#   For "Act II — Inequality" we flip to a dark background (#0F0E0B) to signal
#   a tonal shift — the data gets darker, so does the canvas.
#
# ─────────────────────────────────────────────────────────────────────────────

THEME = {

    # ── Core Identity ──
    "background":       "#F5F0E8",   # Warm paper — default chart bg
    "background_dark":  "#0F0E0B",   # Deep ink — for inequality / dark-mode charts
    "surface":          "#FFFFFF",   # Pure white — chart plot area
    "surface_dark":     "#1A1917",   # Elevated dark surface

    # ── Text ──
    "text":             "#0F0E0B",   # Near-black ink — titles, labels
    "text_light":       "#FFFFFF",   # White — for dark bg charts
    "text_muted":       "#7A7468",   # Warm gray — subtitles, axis labels
    "text_muted_dark":  "#8A8480",   # Muted on dark bg

    # ── Grid & Borders ──
    "grid":             "#E0D9CE",   # Warm light rule — gridlines on light bg
    "grid_dark":        "#2A2825",   # Subtle dark rule — gridlines on dark bg
    "border":           "#D0C9BC",   # Slightly stronger than grid
    "border_dark":      "#3A3835",

    # ── BLUE — Wages, income, hopeful trend ──
    "blue":             "#2A6FAF",   # Main blue — bottom 90% wages, income lines
    "blue_light":       "#5B9BD5",   # Lighter blue — fills, areas
    "blue_dark":        "#1A4A7A",   # Dark blue — emphasis
    "blue_fill":        "rgba(42, 111, 175, 0.10)",  # Transparent fill

    # ── RED — Exploding costs, fertility decline, unaffordability ──
    "red":              "#B84A2E",   # Rust red — hospital, shelter cost lines
    "red_light":        "#D4714F",   # Soft red — fills, secondary
    "red_dark":         "#8A2E18",   # Deep rust — emphasis
    "red_fill":         "rgba(184, 74, 46, 0.10)",

    # ── GOLD — Annotations, medians, thresholds, reference lines ──
    "gold":             "#C8872A",   # Warm amber — THE narrator color
    "gold_light":       "#E0A84A",   # Light gold — fills
    "gold_dark":        "#9A6010",   # Deep gold — borders, strong emphasis
    "gold_fill":        "rgba(200, 135, 42, 0.10)",

    # ── GREEN — Things that got cheaper, good news ──
    "green":            "#2A7C6F",   # Teal-green — apparel, food, electronics
    "green_light":      "#4AA090",   # Lighter green
    "green_dark":       "#1A5248",
    "green_fill":       "rgba(42, 124, 111, 0.10)",

    # ── PURPLE — Education / tuition ──
    "purple":           "#7B4FA6",   # Muted purple — tuition & childcare CPI
    "purple_light":     "#A078C8",
    "purple_fill":      "rgba(123, 79, 166, 0.10)",

    # ── GRAY — Neutral context, headline CPI, background series ──
    "gray":             "#7A7468",   # Warm gray — headline CPI line
    "gray_light":       "#B0A898",   # Light gray — background context
    "gray_dark":        "#3D3830",
    "gray_fill":        "rgba(122, 116, 104, 0.08)",

    # ── ORANGE — Medical care (distinct from housing red) ──
    "orange":           "#C87028",   # Warm orange — medical care CPI
    "orange_light":     "#E09050",

    # ── Typography ──
    "font":             "Playfair Display, Georgia, serif",
    "font_sans":        "DM Sans, Helvetica Neue, Arial, sans-serif",
    "font_mono":        "DM Mono, JetBrains Mono, Courier New, monospace",

    # ── Font sizes (pt / px) ──
    "font_size": {
        "xs":    10,
        "sm":    12,
        "base":  14,
        "md":    16,
        "lg":    20,
        "xl":    28,
        "xxl":   42,
        "hero":  64,
    },

    # ── Font weights ──
    "font_weight": {
        "normal": 400,
        "medium": 500,
        "bold":   700,
        "black":  900,
    },

    # ── Chart defaults ──
    "chart_height":    480,
    "chart_height_sm": 320,
    "chart_height_lg": 600,
    "border_radius":   4,    # kept small for editorial look
    "line_width":      2.5,
    "marker_size":     7,

    # ─────────────────────────────────────────────────────────────────────────
    # SEMANTIC PALETTES
    # Use these by name — don't pick colors ad hoc.
    # ─────────────────────────────────────────────────────────────────────────

    # The Two Inflations chart — costs that rose vs fell
    # Red family = rising costs (bad); Green family = falling costs (good)
    "palette_cpi": {
        "hospital_services":  "#B84A2E",   # red    — scariest rise
        "medical_care":       "#C87028",   # orange — also rose a lot
        "shelter":            "#E0A030",   # amber  — housing
        "tuition_childcare":  "#7B4FA6",   # purple — education / kids
        "all_items":          "#7A7468",   # gray   — neutral baseline
        "avg_hourly_earnings":"#2A6FAF",   # blue   — wages (reference)
        "food_beverages":     "#2A7C6F",   # green  — got cheaper
        "transportation":     "#4AA090",   # lighter green
        "apparel":            "#27ae60",   # bright green — got way cheaper
    },

    # Wage inequality chart
    # Blue = workers; Red = top earners (alarm that they diverged)
    "palette_wages": {
        "bottom_90": "#2A6FAF",   # blue   — the vast majority
        "top_10":    "#5B9BD5",   # lighter blue
        "top_5":     "#E0A030",   # gold
        "top_1":     "#C87028",   # orange-red
        "top_0_1":   "#B84A2E",   # red    — most extreme
        "p10":       "#1A4A7A",   # dark blue — lowest percentile
        "p50":       "#2A6FAF",   # blue   — median
        "p90":       "#B84A2E",   # red    — 90th
    },

    # Fertility chart
    # Single gold line, red replacement threshold
    "palette_fertility": {
        "total_fertility_rate": "#C8872A",   # gold line
        "crude_birth_rate":     "#7A7468",   # gray secondary
        "replacement_line":     "#B84A2E",   # red dashed — 2.1 threshold
        "below_fill":           "rgba(184, 74, 46, 0.08)",  # red area below replacement
    },

    # Housing chart
    "palette_housing": {
        "price_to_income":  "#B84A2E",   # red — ratio going up is bad
        "mortgage_rate":    "#7B4FA6",   # purple
        "hpi_indexed":      "#C8872A",   # gold
    },

    # Gini / inequality chart
    "palette_inequality": {
        "gini":        "#B84A2E",   # red — rising inequality is the alarm
        "gini_fill":   "rgba(184, 74, 46, 0.10)",
        "top1_assets": "#C87028",   # orange
    },

    # Childcare / county map
    # Sequential: light cream → deep rust (more expensive = more alarming)
    "palette_map": [
        "#F5EDD8",   # very light — affordable
        "#EDD4A0",
        "#E0B06A",
        "#D08830",
        "#C06820",
        "#A84818",
        "#8A2A0A",   # deep rust — crisis level
    ],

    # General categorical (for any multi-category chart)
    "palette": [
        "#2A6FAF",   # blue
        "#B84A2E",   # red
        "#C8872A",   # gold
        "#2A7C6F",   # green
        "#7B4FA6",   # purple
        "#C87028",   # orange
        "#7A7468",   # gray
    ],
}


# ─────────────────────────────────────────────────────────────────────────────
# PLOTLY LAYOUT TEMPLATES
# Two versions: light (default) and dark (inequality section)
# ─────────────────────────────────────────────────────────────────────────────

def _base_layout(bg, surface, text, text_muted, grid, border):
    return {
        "paper_bgcolor": bg,
        "plot_bgcolor":  surface,
        "font": {
            "family": THEME["font_sans"],
            "color":  text,
            "size":   THEME["font_size"]["base"],
        },
        "title": {
            "font": {
                "family": THEME["font"],
                "color":  text,
                "size":   THEME["font_size"]["lg"],
            },
            "x": 0.0,
            "xanchor": "left",
            "pad": {"l": 0},
        },
        "xaxis": {
            "gridcolor":   grid,
            "linecolor":   border,
            "tickcolor":   border,
            "zerolinecolor": grid,
            "tickfont":    {"color": text_muted, "size": THEME["font_size"]["sm"],
                            "family": THEME["font_mono"]},
            "title_font":  {"color": text, "size": THEME["font_size"]["base"]},
        },
        "yaxis": {
            "gridcolor":   grid,
            "linecolor":   border,
            "tickcolor":   border,
            "zerolinecolor": grid,
            "tickfont":    {"color": text_muted, "size": THEME["font_size"]["sm"],
                            "family": THEME["font_mono"]},
            "title_font":  {"color": text, "size": THEME["font_size"]["base"]},
        },
        "legend": {
            "bgcolor":     "rgba(0,0,0,0)",
            "bordercolor": "rgba(0,0,0,0)",
            "font":        {"color": text, "size": THEME["font_size"]["sm"],
                            "family": THEME["font_sans"]},
        },
        "hoverlabel": {
            "bgcolor":     THEME["surface"] if bg == THEME["background"] else THEME["surface_dark"],
            "font":        {"family": THEME["font_sans"], "color": THEME["text"],
                            "size": THEME["font_size"]["sm"]},
            "bordercolor": border,
        },
        "colorway": THEME["palette"],
        "margin":   {"t": 60, "b": 50, "l": 60, "r": 30},
        "height":   THEME["chart_height"],
    }


# Light theme (Acts I, III, IV — default)
PLOTLY_LAYOUT = _base_layout(
    bg          = THEME["background"],
    surface     = THEME["surface"],
    text        = THEME["text"],
    text_muted  = THEME["text_muted"],
    grid        = THEME["grid"],
    border      = THEME["border"],
)

# Dark theme (Act II — Inequality)
PLOTLY_LAYOUT_DARK = _base_layout(
    bg          = THEME["background_dark"],
    surface     = THEME["surface_dark"],
    text        = THEME["text_light"],
    text_muted  = THEME["text_muted_dark"],
    grid        = THEME["grid_dark"],
    border      = THEME["border_dark"],
)


# ─────────────────────────────────────────────────────────────────────────────
# MATPLOTLIB STYLE DICT  (for static charts in notebooks)
# ─────────────────────────────────────────────────────────────────────────────

MPL_STYLE = {
    # Figure
    "figure.facecolor":     THEME["background"],
    "axes.facecolor":       THEME["surface"],
    "savefig.facecolor":    THEME["background"],
    # Text
    "text.color":           THEME["text"],
    "axes.labelcolor":      THEME["text"],
    "xtick.color":          THEME["text_muted"],
    "ytick.color":          THEME["text_muted"],
    "axes.titlecolor":      THEME["text"],
    # Grid
    "axes.edgecolor":       THEME["border"],
    "grid.color":           THEME["grid"],
    "grid.linewidth":       0.8,
    "grid.alpha":           1.0,
    "axes.grid":            True,
    "axes.axisbelow":       True,
    # Lines & markers
    "lines.linewidth":      THEME["line_width"],
    "lines.solid_capstyle": "round",
    "patch.linewidth":      0.5,
    # Font
    "font.family":          "serif",
    "font.serif":           ["DejaVu Serif", "Georgia", "Palatino", "Times New Roman"],
    "axes.titlesize":       THEME["font_size"]["md"],
    "axes.titleweight":     "bold",
    "axes.labelsize":       THEME["font_size"]["base"],
    "xtick.labelsize":      THEME["font_size"]["sm"],
    "ytick.labelsize":      THEME["font_size"]["sm"],
    "legend.fontsize":      THEME["font_size"]["sm"],
    # Spines
    "axes.spines.top":      False,
    "axes.spines.right":    False,
    # Cycle
    "axes.prop_cycle":      f"cycler('color', {THEME['palette']})",
}


# ─────────────────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────

def apply_theme(fig):
    """Apply light theme to a Plotly figure (Acts I, III, IV)."""
    fig.update_layout(**PLOTLY_LAYOUT)
    return fig


def apply_dark_theme(fig):
    """Apply dark theme to a Plotly figure (Act II — Inequality)."""
    fig.update_layout(**PLOTLY_LAYOUT_DARK)
    return fig


def apply_mpl_style():
    """Apply the shared matplotlib style. Call once at top of each notebook.

    Usage:
        from theme import apply_mpl_style, THEME
        apply_mpl_style()
    """
    import matplotlib as mpl
    # axes.prop_cycle needs special treatment
    import matplotlib.pyplot as plt
    from cycler import cycler
    style = {k: v for k, v in MPL_STYLE.items() if k != "axes.prop_cycle"}
    mpl.rcParams.update(style)
    plt.rcParams["axes.prop_cycle"] = cycler("color", THEME["palette"])


def annotate_threshold(fig, y_val, label, color=None, dash="dash", row=1, col=1):
    """Add a horizontal threshold line to a Plotly figure.

    Usage:
        annotate_threshold(fig, y_val=2.1, label="Replacement rate (2.1)",
                           color=THEME['red'])
    """
    if color is None:
        color = THEME["gold"]
    fig.add_hline(
        y=y_val, line_dash=dash,
        line_color=color, line_width=1.5,
        annotation_text=label,
        annotation_position="top right",
        annotation_font_color=color,
        annotation_font_size=THEME["font_size"]["xs"],
        annotation_font_family=THEME["font_mono"],
        row=row, col=col,
    )
    return fig


def add_recession_bands(fig, row=1, col=1, dark=False):
    """Add NBER recession shading to a Plotly time-series figure.

    Covers major recessions from 1960 to 2024.
    """
    recessions = [
        (1960, 1961),  # Kennedy recession
        (1969, 1970),  # Nixon recession
        (1973, 1975),  # Oil shock
        (1980, 1980),  # Volcker I
        (1981, 1982),  # Volcker II
        (1990, 1991),  # Gulf War
        (2001, 2001),  # Dot-com
        (2007, 2009),  # Great Recession
        (2020, 2020),  # COVID
    ]
    fill_color = "rgba(122,116,104,0.10)" if not dark else "rgba(255,255,255,0.05)"
    for start, end in recessions:
        fig.add_vrect(
            x0=start, x1=end + 0.5,
            fillcolor=fill_color,
            line_width=0,
            layer="below",
            row=row, col=col,
        )
    return fig


def watermark(fig, text="Source: FRED, BLS, EPI, CDC, DOL", dark=False):
    """Add a source watermark annotation to a Plotly figure."""
    color = THEME["text_muted"] if not dark else THEME["text_muted_dark"]
    fig.add_annotation(
        text=text,
        xref="paper", yref="paper",
        x=0, y=-0.12,
        showarrow=False,
        font=dict(
            family=THEME["font_mono"],
            size=THEME["font_size"]["xs"],
            color=color,
        ),
        align="left",
    )
    return fig


# ─────────────────────────────────────────────────────────────────────────────
# QUICK-ACCESS COLOR SHORTCUTS
# Import these directly for clean code in notebooks:
#   from theme import C
#   fig.add_trace(..., line=dict(color=C.red, width=2.5))
# ─────────────────────────────────────────────────────────────────────────────

class _Colors:
    """Dot-access shortcuts for the most-used colors."""
    # Core
    bg          = THEME["background"]
    bg_dark     = THEME["background_dark"]
    text        = THEME["text"]
    muted       = THEME["text_muted"]
    grid        = THEME["grid"]
    # Semantic
    blue        = THEME["blue"]
    blue_light  = THEME["blue_light"]
    blue_fill   = THEME["blue_fill"]
    red         = THEME["red"]
    red_light   = THEME["red_light"]
    red_fill    = THEME["red_fill"]
    gold        = THEME["gold"]
    gold_light  = THEME["gold_light"]
    gold_fill   = THEME["gold_fill"]
    green       = THEME["green"]
    green_light = THEME["green_light"]
    green_fill  = THEME["green_fill"]
    purple      = THEME["purple"]
    orange      = THEME["orange"]
    gray        = THEME["gray"]
    gray_light  = THEME["gray_light"]
    # Palettes
    cpi         = THEME["palette_cpi"]
    wages       = THEME["palette_wages"]
    fertility   = THEME["palette_fertility"]
    housing     = THEME["palette_housing"]
    map_seq     = THEME["palette_map"]


C = _Colors()


# ─────────────────────────────────────────────────────────────────────────────
# NOTEBOOK USAGE GUIDE
# ─────────────────────────────────────────────────────────────────────────────
#
# ── In every notebook, at the top: ──
#
#   from theme import THEME, C, apply_theme, apply_dark_theme
#   from theme import apply_mpl_style, annotate_threshold, add_recession_bands, watermark
#   apply_mpl_style()   # sets matplotlib rcParams globally
#
# ── For Plotly charts: ──
#
#   import plotly.graph_objects as go
#   fig = go.Figure()
#   fig.add_trace(go.Scatter(x=years, y=vals, line=dict(color=C.red, width=2.5)))
#   apply_theme(fig)        # light bg  (Acts I, III, IV)
#   apply_dark_theme(fig)   # dark bg   (Act II)
#   annotate_threshold(fig, 2.1, "Replacement rate (2.1)", C.red)
#   add_recession_bands(fig)
#   watermark(fig)
#   fig.show()
#
# ── For Matplotlib static charts: ──
#
#   import matplotlib.pyplot as plt
#   apply_mpl_style()
#   fig, ax = plt.subplots(figsize=(12, 5))
#   ax.plot(years, vals, color=C.red, linewidth=2.5, label="Hospital Services")
#   ax.axhline(100, color=C.gold, linestyle="--", linewidth=1.2, label="1967 = 100")
#
# ── Color assignment rules: ──
#
#   Costs that ROSE faster than wages  → C.red, C.orange, C.purple
#   Costs that FELL or kept pace       → C.green, C.green_light
#   Wages / income                     → C.blue, C.blue_light
#   Reference / annotation lines       → C.gold  (always)
#   Background/neutral CPI             → C.gray
#   Gini, inequality, top 1% alarm     → C.red
#   Fertility below replacement        → C.red fill + C.gold line
#
# ─────────────────────────────────────────────────────────────────────────────
