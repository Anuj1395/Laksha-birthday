import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path
# ============================================================
# STREAMLIT CONFIG
# ============================================================
st.set_page_config(
    page_title="A Very Important Birthday",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# ============================================================
# PROJECT / ASSET PATHS
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "Assets"
# ============================================================
# FIND FILE
# ============================================================
def find_asset(stem, extensions=None):
    if not ASSETS_DIR.exists():
        return None
    # Exact filename first
    exact = ASSETS_DIR / stem
    if exact.exists():
        return exact
    # Try common extensions
    if extensions is None:
        extensions = [
            ".mp4",
            ".mov",
            ".webm",
            ".mp3",
            ".mpeg",
            ".wav",
            ".m4a",
            ".jpg",
            ".jpeg",
            ".png",
            ".webp"
        ]
    for extension in extensions:
        candidate = ASSETS_DIR / f"{stem}{extension}"
        if candidate.exists():
            return candidate
        # Also try uppercase extension
        candidate_upper = ASSETS_DIR / f"{stem}{extension.upper()}"
        if candidate_upper.exists():
            return candidate_upper
    # Case-insensitive fallback
    for file in ASSETS_DIR.iterdir():
        if file.is_file():
            if file.stem.lower() == Path(stem).stem.lower():
                return file
    return None
# ============================================================
# MIME TYPES
# ============================================================
def get_mime_type(file_path):
    extension = file_path.suffix.lower()
    mime_types = {
        ".mp4": "video/mp4",
        ".mov": "video/quicktime",
        ".webm": "video/webm",
        ".mp3": "audio/mpeg",
        ".mpeg": "audio/mpeg",
        ".wav": "audio/wav",
        ".m4a": "audio/mp4",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp"
    }
    return mime_types.get(
        extension,
        "application/octet-stream"
    )
# ============================================================
# CONVERT ASSET TO DATA URI
# ============================================================
def load_asset(stem, extensions=None):
    file_path = find_asset(
        stem,
        extensions
    )
    if file_path is None:
        return None
    data = file_path.read_bytes()
    encoded = base64.b64encode(data).decode("utf-8")
    mime = get_mime_type(file_path)
    return f"data:{mime};base64,{encoded}"
# ============================================================
# INTRO PAGE
# ============================================================
def intro_page():
    INTRO = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>
<link rel="preconnect"
      href="https://fonts.googleapis.com">
<link rel="preconnect"
      href="https://fonts.gstatic.com"
      crossorigin>
<link
href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=Playfair+Display:wght@500;600;700&display=swap"
rel="stylesheet"
>
<style>
* {
    box-sizing: border-box;
}
html,
body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
}
body {
    overflow: hidden;
    font-family: "DM Sans", sans-serif;
    background: #eee5d8;
}
/* ============================================================
   BACKGROUND
============================================================ */
.page {
    position: relative;
    width: 100%;
    min-height: 100vh;
    overflow: hidden;
    background:
        radial-gradient(
            circle at 82% 15%,
            rgba(244, 190, 155, 0.55),
            transparent 28%
        ),
        radial-gradient(
            circle at 12% 90%,
            rgba(224, 174, 145, 0.35),
            transparent 30%
        ),
        #eee5d8;
}
.orb {
    position: absolute;
    width: 420px;
    height: 420px;
    border-radius: 50%;
    background:
        rgba(255,255,255,0.25);
    right: -160px;
    bottom: -160px;
}
/* ============================================================
   SMALL DETAILS
============================================================ */
.top-left {
    position: absolute;
    top: 42px;
    left: 55px;
    font-size: 12px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(50,38,32,0.55);
}
.top-right {
    position: absolute;
    top: 42px;
    right: 55px;
    font-size: 12px;
    color: rgba(50,38,32,0.45);
}
/* ============================================================
   MAIN CONTENT
============================================================ */
.content {
    position: relative;
    z-index: 5;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-left: 9vw;
    max-width: 900px;
    animation: appear 1.2s ease forwards;
}
.hello {
    font-size: 15px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #8a6658;
    margin-bottom: 22px;
}
h1 {
    font-family: "Playfair Display", serif;
    font-size: clamp(46px, 6vw, 82px);
    line-height: 0.98;
    font-weight: 600;
    letter-spacing: -2px;
    color: #302522;
    margin: 0;
    max-width: 750px;
}
.subtitle {
    margin-top: 25px;
    font-family: "Playfair Display", serif;
    font-size: 23px;
    font-style: italic;
    color: #75584c;
}
/* ============================================================
   BUTTONS
============================================================ */
.buttons {
    display: flex;
    flex-direction: column;
    gap: 13px;
    margin-top: 58px;
    width: min(560px, 80vw);
}
.birthday-button {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    padding: 18px 22px;
    border: 1px solid rgba(75,55,47,0.18);
    border-radius: 4px;
    background: rgba(255,255,255,0.30);
    color: #382a25;
    text-decoration: none;
    font-size: 15px;
    transition:
        transform 0.25s ease,
        background 0.25s ease,
        border-color 0.25s ease;
}
.birthday-button:hover {
    transform: translateX(8px);
    background: rgba(255,255,255,0.65);
    border-color: rgba(75,55,47,0.35);
}
.number {
    font-family: "Playfair Display", serif;
    font-size: 24px;
    font-weight: 600;
    margin-right: 20px;
}
.arrow {
    font-size: 18px;
    opacity: 0.45;
    transition:
        transform 0.25s ease;
}
.birthday-button:hover .arrow {
    transform: translateX(5px);
    opacity: 0.8;
}
/* ============================================================
   FOOTER
============================================================ */
.footer {
    position: absolute;
    bottom: 38px;
    left: 55px;
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(50,38,32,0.4);
}
/* ============================================================
   ANIMATION
============================================================ */
@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
/* ============================================================
   MOBILE
============================================================ */
@media (max-width: 700px) {
    .content {
        padding-left: 28px;
        padding-right: 28px;
    }
    .top-left {
        left: 28px;
    }
    .top-right {
        right: 28px;
    }
    h1 {
        font-size: 48px;
    }
    .subtitle {
        font-size: 19px;
    }
    .buttons {
        width: 100%;
        margin-top: 42px;
    }
    .footer {
        left: 28px;
    }
}
</style>
</head>
<body>
<div class="page">
    <div class="orb"></div>
    <div class="top-left">
        Birthday Department
    </div>
    <div class="top-right">
        01 / 01
    </div>
    <main class="content">
        <div class="hello">
            Hello Laksha!!
        </div>
        <h1>
            Welcome to your
            worst gift ever.
        </h1>
        <div class="subtitle">
            But first, we need to establish something.
        </div>
        <div class="buttons">
            <a
                class="birthday-button"
                href="?page=edit"
            >
                <span>
                    <span class="number">
                        01
                    </span>
                    Click if today is your birthday
                </span>
                <span class="arrow">
                    →
                </span>
            </a>
            <a
                class="birthday-button"
                href="?page=edit"
            >
                <span>
                    <span class="number">
                        02
                    </span>
                    Click if today is your birthday
                </span>
                <span class="arrow">
                    →
                </span>
            </a>
            <a
                class="birthday-button"
                href="?page=edit"
            >
                <span>
                    <span class="number">
                        03
                    </span>
                    And surprise, surprise...
                    click if it is your birthday.
                </span>
                <span class="arrow">
                    →
                </span>
            </a>
        </div>
    </main>
    <div class="footer">
        Made with questionable intentions ♡
    </div>
</div>
</body>
</html>
"""
    components.html(
        INTRO,
        height=900,
        scrolling=False
    )
# ============================================================
# EDIT PAGE
# ============================================================
def edit_page():
    # --------------------------------------------------------
    # LOAD MEDIA
    # --------------------------------------------------------
    baby = load_asset(
        "baby",
        [".mp4", ".mov", ".webm"]
    )
    psych = load_asset(
        "psych",
        [".mp4", ".mov", ".webm"]
    )
    honorable = load_asset(
        "Honorable",
        [".mp4", ".mov", ".webm"]
    )
    birthday_audio = load_asset(
        "Happy birthday",
        [".mp3", ".mpeg", ".wav", ".m4a"]
    )
    image3 = load_asset(
        "3",
        [".jpg", ".jpeg", ".png", ".webp"]
    )
    image4 = load_asset(
        "4",
        [".jpg", ".jpeg", ".png", ".webp"]
    )
    image5 = load_asset(
        "5",
        [".jpg", ".jpeg", ".png", ".webp"]
    )
    image7 = load_asset(
        "7",
        [".jpg", ".jpeg", ".png", ".webp"]
    )
    # --------------------------------------------------------
    # ROAST EDIT MEDIA
    # --------------------------------------------------------
    roast_images = []
    for number in range(1, 7):
        roast_images.append(
            load_asset(
                f"Roast {number}",
                [".jpg", ".jpeg", ".png", ".webp"]
            )
        )
    roast_audio = load_asset(
        "we-on-go-bia_2OIPih8O",
        [".mp3", ".mpeg", ".wav", ".m4a"]
    )
    poster_image = load_asset(
        "end screen",
        [".jpg", ".jpeg", ".png", ".webp"]
    )
    # --------------------------------------------------------
    # CHECK REQUIRED FILES
    # --------------------------------------------------------
    missing = []
    if baby is None:
        missing.append("baby")
    if psych is None:
        missing.append("psych")
    if honorable is None:
        missing.append("Honorable")
    if birthday_audio is None:
        missing.append("Happy birthday")
    if image3 is None:
        missing.append("3")
    if image4 is None:
        missing.append("4")
    if image5 is None:
        missing.append("5")
    if image7 is None:
        missing.append("7")
    for number, roast_image in enumerate(roast_images, start=1):
        if roast_image is None:
            missing.append(f"Roast {number}")
    if roast_audio is None:
        missing.append("we-on-go-bia_2OIPih8O")
    if poster_image is None:
        missing.append("end screen")
    if missing:
        st.error(
            "Could not find these assets: "
            + ", ".join(missing)
        )
        st.write(
            "Assets folder being used:"
        )
        st.code(str(ASSETS_DIR))
        st.write("Files currently found:")
        if ASSETS_DIR.exists():
            st.code(
                "\n".join(
                    file.name
                    for file in ASSETS_DIR.iterdir()
                )
            )
        else:
            st.error(
                "The Assets folder itself could not be found."
            )
        st.stop()
    # ========================================================
    # EDIT HTML
    # ========================================================
    EDIT = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
>
<style>
* {{
    box-sizing: border-box;
}}
html,
body {{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    background: #000;
    overflow: hidden;
}}
body {{
    font-family: Arial, sans-serif;
}}
/* ============================================================
   MAIN SCREEN
============================================================ */
.screen {{
    position: relative;
    width: 100vw;
    height: 100vh;
    background: #000;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}}
/* ============================================================
   VIDEO FRAME
============================================================ */
.video-frame {{
    position: relative;
    width: 100%;
    height: 100%;
    background: #000;
    overflow: hidden;
}}
/* ============================================================
   BLURRED BACKGROUND
============================================================ */
.media-background {{
    position: absolute;
    inset: -40px;
    background: #000;
    background-size: cover;
    background-position: center;
    filter: blur(30px);
    transform: scale(1.15);
    opacity: 0;
    transition: opacity 0.5s ease;
    z-index: 0;
}}
.media-background.visible {{
    opacity: 0.55;
}}
/* ============================================================
   VIDEOS
============================================================ */
video {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: none;
    background: transparent;
    z-index: 5;
}}
video.active {{
    display: block;
}}
/* ============================================================
   BIRTHDAY SECTION
============================================================ */
.birthday-section {{
    position: absolute;
    inset: 0;
    display: none;
    align-items: center;
    justify-content: center;
    background: #000;
    z-index: 5;
}}
.birthday-section.active {{
    display: flex;
}}
/* ============================================================
   BIRTHDAY IMAGES
============================================================ */
.birthday-image {{
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: contain;
    opacity: 0;
    transform: scale(1.05);
    transition:
        opacity 0.8s ease,
        transform 3s ease;
    z-index: 2;
}}
.birthday-image.show {{
    opacity: 1;
    transform: scale(1);
}}
/* ============================================================
   BIRTHDAY PHOTO BACKGROUND
============================================================ */
.photo-background {{
    position: absolute;
    inset: -40px;
    background-size: cover;
    background-position: center;
    filter: blur(28px);
    transform: scale(1.1);
    opacity: 0.45;
    z-index: 1;
}}
/* ============================================================
   BLACK TRANSITION
============================================================ */
.black {{
    position: absolute;
    inset: 0;
    background: #000;
    z-index: 50;
    opacity: 1;
    pointer-events: none;
    transition:
        opacity 0.8s ease;
}}
.black.hide {{
    opacity: 0;
}}
/* ============================================================
   START SCREEN
============================================================ */
.start-screen {{
    position: absolute;
    inset: 0;
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background: #000;
    color: white;
    text-align: center;
    transition:
        opacity 0.6s ease;
}}
.start-screen.hidden {{
    opacity: 0;
    pointer-events: none;
}}
.start-small {{
    font-size: 11px;
    letter-spacing: 4px;
    text-transform: uppercase;
    opacity: 0.5;
    margin-bottom: 18px;
}}
.start-title {{
    font-family: Georgia, serif;
    font-size: 36px;
    margin-bottom: 28px;
}}
.start-button {{
    padding: 14px 28px;
    border: 1px solid rgba(255,255,255,0.45);
    background: transparent;
    color: white;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
    cursor: pointer;
    transition:
        background 0.2s ease,
        color 0.2s ease;
}}
.start-button:hover {{
    background: white;
    color: black;
}}
/* ============================================================
   END SCREEN
============================================================ */
.end-screen {{
    position: absolute;
    inset: 0;
    z-index: 80;
    display: none;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background: #000;
    color: white;
    text-align: center;
}}
.end-screen.active {{
    display: flex;
}}
.end-small {{
    font-size: 11px;
    letter-spacing: 4px;
    text-transform: uppercase;
    opacity: 0.45;
    margin-bottom: 20px;
}}
.end-title {{
    font-family: Georgia, serif;
    font-size: 42px;
}}
/* ============================================================
   ROAST EDIT — CINEMATIC
============================================================ */
.roast-section {{
    position: absolute;
    inset: 0;
    display: none;
    align-items: center;
    justify-content: center;
    background: #000;
    z-index: 20;
    overflow: hidden;
}}
.roast-section.active {{
    display: flex;
}}
.roast-image {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: contain;
    opacity: 0;
    transform: scale(1) translate3d(0,0,0) rotate(0deg);
    filter: contrast(1) saturate(1);
    will-change: transform, opacity, filter;
    z-index: 2;
}}
.roast-image.active {{
    opacity: 1;
}}
.roast-vignette {{
    position: absolute;
    inset: 0;
    z-index: 8;
    pointer-events: none;
    box-shadow: inset 0 0 180px rgba(0,0,0,0.82);
}}
.roast-flash {{
    position: absolute;
    inset: 0;
    background: #fff;
    opacity: 0;
    z-index: 20;
    pointer-events: none;
}}
.roast-flash.hit {{
    animation: roastFlash 0.12s linear;
}}
@keyframes roastFlash {{
    0% {{ opacity: 0; }}
    18% {{ opacity: 0.95; }}
    100% {{ opacity: 0; }}
}}
.roast-label {{
    position: absolute;
    left: 24px;
    bottom: 22px;
    z-index: 12;
    color: rgba(255,255,255,0.72);
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    opacity: 0;
    transition: opacity 0.25s ease;
}}
.roast-label.show {{
    opacity: 1;
}}
.roast-section.black-hit .roast-image {{
    opacity: 0;
}}
.roast-image.roast-intro {{
    animation: roastIntro 1.25s cubic-bezier(.16,.78,.22,1) forwards;
}}
@keyframes roastIntro {{
    0% {{
        opacity: 0;
        transform: scale(1.02);
        filter: brightness(0.35) contrast(1.15);
    }}
    18% {{ opacity: 1; }}
    100% {{
        opacity: 1;
        transform: scale(1.12);
        filter: brightness(1) contrast(1.08);
    }}
}}
.roast-image.zoom-in {{
    animation: roastZoomIn 0.52s cubic-bezier(.12,.9,.18,1) forwards;
}}
@keyframes roastZoomIn {{
    0% {{ transform: scale(1.00); }}
    32% {{ transform: scale(1.28); }}
    100% {{ transform: scale(1.10); }}
}}
.roast-image.zoom-out {{
    animation: roastZoomOut 0.48s cubic-bezier(.12,.9,.18,1) forwards;
}}
@keyframes roastZoomOut {{
    0% {{ transform: scale(1.22); }}
    38% {{ transform: scale(0.90); }}
    100% {{ transform: scale(1.08); }}
}}
.roast-image.punch {{
    animation: roastPunch 0.30s cubic-bezier(.08,.92,.16,1) forwards;
}}
@keyframes roastPunch {{
    0% {{ transform: scale(1.00); }}
    35% {{ transform: scale(1.38); }}
    100% {{ transform: scale(1.10); }}
}}
.roast-image.rotate-left {{
    animation: roastRotateLeft 0.46s cubic-bezier(.12,.9,.18,1) forwards;
}}
@keyframes roastRotateLeft {{
    0% {{ transform: scale(1.18) rotate(-6deg) translateX(-1%); }}
    100% {{ transform: scale(1.10) rotate(2deg) translateX(0); }}
}}
.roast-image.rotate-right {{
    animation: roastRotateRight 0.46s cubic-bezier(.12,.9,.18,1) forwards;
}}
@keyframes roastRotateRight {{
    0% {{ transform: scale(1.18) rotate(6deg) translateX(1%); }}
    100% {{ transform: scale(1.10) rotate(-2deg) translateX(0); }}
}}
.roast-image.slide-left {{
    animation: roastSlideLeft 0.42s cubic-bezier(.12,.9,.18,1) forwards;
}}
@keyframes roastSlideLeft {{
    0% {{ transform: scale(1.12) translateX(7%); }}
    100% {{ transform: scale(1.10) translateX(0); }}
}}
.roast-image.slide-right {{
    animation: roastSlideRight 0.42s cubic-bezier(.12,.9,.18,1) forwards;
}}
@keyframes roastSlideRight {{
    0% {{ transform: scale(1.12) translateX(-7%); }}
    100% {{ transform: scale(1.10) translateX(0); }}
}}
.roast-image.shake {{
    animation: roastShake 0.34s linear forwards;
}}
@keyframes roastShake {{
    0% {{ transform: scale(1.16) translate3d(0,0,0) rotate(0); }}
    12% {{ transform: scale(1.16) translate3d(-18px,7px,0) rotate(-1deg); }}
    25% {{ transform: scale(1.16) translate3d(17px,-8px,0) rotate(1deg); }}
    38% {{ transform: scale(1.16) translate3d(-14px,-6px,0) rotate(-1deg); }}
    51% {{ transform: scale(1.16) translate3d(13px,8px,0) rotate(1deg); }}
    64% {{ transform: scale(1.16) translate3d(-9px,3px,0) rotate(-0.5deg); }}
    78% {{ transform: scale(1.16) translate3d(7px,-3px,0) rotate(0.5deg); }}
    100% {{ transform: scale(1.12) translate3d(0,0,0) rotate(0); }}
}}
.roast-image.final-hit {{
    animation: roastFinal 0.72s cubic-bezier(.08,.92,.16,1) forwards;
}}
@keyframes roastFinal {{
    0% {{
        transform: scale(1.00);
        filter: brightness(0.8) contrast(1);
    }}
    22% {{
        transform: scale(1.45);
        filter: brightness(1.25) contrast(1.12);
    }}
    100% {{
        transform: scale(1.18);
        filter: brightness(1) contrast(1.1);
    }}
}}
@media (max-width: 700px) {{
    .roast-image {{ object-fit: contain; }}
    .roast-label {{
        left: 16px;
        bottom: 16px;
        font-size: 8px;
    }}
}}
/* ============================================================
   POST EDIT MCQ
============================================================ */
.mcq-screen {{
    position: absolute;
    inset: 0;
    z-index: 90;
    display: none;
    align-items: center;
    justify-content: center;
    background:
        radial-gradient(circle at 50% 35%, #181818 0%, #080808 45%, #000 100%);
    color: white;
    padding: 30px;
}}
.mcq-screen.active {{
    display: flex;
}}
.mcq-card {{
    width: min(720px, 92vw);
    text-align: center;
    animation: mcqAppear 0.7s ease forwards;
}}
@keyframes mcqAppear {{
    from {{
        opacity: 0;
        transform: translateY(25px) scale(0.97);
    }}
    to {{
        opacity: 1;
        transform: translateY(0) scale(1);
    }}
}}
.mcq-small {{
    font-size: 10px;
    letter-spacing: 4px;
    text-transform: uppercase;
    opacity: 0.45;
    margin-bottom: 14px;
}}
.mcq-progress {{
    font-size: 11px;
    letter-spacing: 3px;
    opacity: 0.35;
    margin-bottom: 35px;
}}
.mcq-question {{
    font-family: Georgia, serif;
    font-size: clamp(28px, 4vw, 48px);
    line-height: 1.15;
    margin-bottom: 42px;
}}
.mcq-options {{
    display: flex;
    flex-direction: column;
    gap: 10px;
}}
.mcq-option {{
    width: 100%;
    display: flex;
    align-items: center;
    gap: 18px;
    padding: 17px 20px;
    background: rgba(255,255,255,0.035);
    border: 1px solid rgba(255,255,255,0.16);
    color: white;
    cursor: pointer;
    text-align: left;
    font-family: Arial, sans-serif;
    font-size: 14px;
    transition:
        transform 0.2s ease,
        background 0.2s ease,
        border-color 0.2s ease;
}}
.mcq-option:hover {{
    transform: translateX(7px);
    background: rgba(255,255,255,0.10);
    border-color: rgba(255,255,255,0.45);
}}
.mcq-option span {{
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid rgba(255,255,255,0.25);
    font-size: 11px;
    flex-shrink: 0;
}}
.mcq-option.correct {{
    background: white;
    color: black;
    border-color: white;
    transform: scale(1.02);
}}
.mcq-option.wrong {{
    opacity: 0.25;
    transform: translateX(-4px);
}}
.mcq-message {{
    min-height: 30px;
    margin-top: 28px;
    font-size: 12px;
    letter-spacing: 2px;
    text-transform: uppercase;
    opacity: 0;
    transition: opacity 0.25s ease;
}}
.mcq-message.show {{
    opacity: 0.65;
}}
@media (max-width: 700px) {{
    .mcq-screen {{
        padding: 20px;
    }}
    .mcq-question {{
        font-size: 30px;
        margin-bottom: 30px;
    }}
    .mcq-option {{
        padding: 15px 16px;
    }}
}}
/* ============================================================
   FINAL POSTER SCREEN
============================================================ */
.poster-screen {{
    position: absolute;
    inset: 0;
    z-index: 95;
    display: none;
    align-items: center;
    justify-content: center;
    background: #000;
    overflow: hidden;
}}
.poster-screen.active {{
    display: flex;
}}
.poster-image {{
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    opacity: 0;
    transform: scale(1.035);
    animation: posterReveal 1.2s ease forwards;
}}
@keyframes posterReveal {{
    from {{
        opacity: 0;
        transform: scale(1.035);
    }}
    to {{
        opacity: 1;
        transform: scale(1);
    }}
}}
</style>
</head>
<body>
<div class="screen">
    <div class="video-frame">
        <!-- =================================================
             BLURRED MEDIA BACKGROUND
        ================================================== -->
        <div
            class="media-background"
            id="mediaBackground"
        ></div>
        <!-- =================================================
             BABY
        ================================================== -->
        <video
            id="baby"
            playsinline
            preload="auto"
        >
            <source
                src="{baby}"
                type="video/mp4"
            >
        </video>
        <!-- =================================================
             PSYCH
        ================================================== -->
        <video
            id="psych"
            playsinline
            preload="auto"
        >
            <source
                src="{psych}"
                type="video/mp4"
            >
        </video>
        <!-- =================================================
             BIRTHDAY AUDIO
        ================================================== -->
        <audio
            id="birthdayAudio"
            preload="auto"
        >
            <source
                src="{birthday_audio}"
                type="audio/mpeg"
            >
        </audio>
        <!-- =================================================
             BIRTHDAY PHOTOS
        ================================================== -->
        <div
            class="birthday-section"
            id="birthdaySection"
        >
            <div
                class="photo-background"
                id="photoBackground"
            ></div>
            <img
                id="image3"
                class="birthday-image"
                src="{image3}"
            >
            <img
                id="image4"
                class="birthday-image"
                src="{image4}"
            >
            <img
                id="image5"
                class="birthday-image"
                src="{image5}"
            >
            <img
                id="image7"
                class="birthday-image"
                src="{image7}"
            >
        </div>
        <!-- =================================================
             CHURCHILL / HONORABLE
        ================================================== -->
        <video
            id="honorable"
            playsinline
            preload="auto"
        >
            <source
                src="{honorable}"
                type="video/mp4"
            >
        </video>
        <!-- =================================================
             BLACK TRANSITION
        ================================================== -->
        <!-- =================================================
             ROAST AUDIO
        ================================================== -->
        <audio
            id="roastAudio"
            preload="auto"
        >
            <source
                src="{roast_audio}"
                type="audio/mpeg"
            >
        </audio>
        <!-- =================================================
             ROAST EDIT
        ================================================== -->
        <div
            class="roast-section"
            id="roastSection"
        >
            <img id="roast1" class="roast-image" src="{roast_images[0]}">
            <img id="roast2" class="roast-image" src="{roast_images[1]}">
            <img id="roast3" class="roast-image" src="{roast_images[2]}">
            <img id="roast4" class="roast-image" src="{roast_images[3]}">
            <img id="roast5" class="roast-image" src="{roast_images[4]}">
            <img id="roast6" class="roast-image" src="{roast_images[5]}">
            <div class="roast-vignette"></div>
            <div
                class="roast-flash"
                id="roastFlash"
            ></div>
            <div
                class="roast-label"
                id="roastLabel"
            >
                Birthday Department // evidence
            </div>
        </div>
        <div
            class="black"
            id="black"
        ></div>
        <!-- =================================================
             START SCREEN
        ================================================== -->
        <div
            class="start-screen"
            id="startScreen"
        >
            <div class="start-small">
                Birthday Department
            </div>
            <div class="start-title">
                We have something for you.
            </div>
            <button
                class="start-button"
                id="startButton"
            >
                Start
            </button>
        </div>
        <!-- =================================================
             END SCREEN
        ================================================== -->
        <!-- =================================================
             POST EDIT MCQ
        ================================================== -->
        <div
            class="mcq-screen"
            id="mcqScreen"
        >
            <div class="mcq-card">
                <div class="mcq-small">
                    Birthday Department // Feedback Form
                </div>
                <div
                    class="mcq-progress"
                    id="mcqProgress"
                >
                    01 / 02
                </div>
                <div
                    class="mcq-question"
                    id="mcqQuestion"
                >
                    Did you like the edit?
                </div>
                <div
                    class="mcq-options"
                    id="mcqOptions"
                ></div>
                <div
                    class="mcq-message"
                    id="mcqMessage"
                ></div>
            </div>
        </div>
        <!-- =================================================
             FINAL POSTER SCREEN
        ================================================== -->
        <div
            class="poster-screen"
            id="posterScreen"
        >
            <img
                class="poster-image"
                id="posterImage"
                src="{poster_image}"
                alt="Final birthday poster"
            >
        </div>
<div
            class="end-screen"
            id="endScreen"
        >
            <div class="end-small">
                That's enough for now
            </div>
            <div class="end-title">
                😌
            </div>
        </div>
    </div>
</div>
<script>
// ============================================================
// ELEMENTS
// ============================================================
const baby =
    document.getElementById("baby");
const psych =
    document.getElementById("psych");
const honorable =
    document.getElementById("honorable");
const birthdayAudio =
    document.getElementById("birthdayAudio");
const birthdaySection =
    document.getElementById("birthdaySection");
const black =
    document.getElementById("black");
const startScreen =
    document.getElementById("startScreen");
const startButton =
    document.getElementById("startButton");
const endScreen =
    document.getElementById("endScreen");
const photoBackground =
    document.getElementById("photoBackground");
const mediaBackground =
    document.getElementById("mediaBackground");
const roastAudio =
    document.getElementById("roastAudio");
const roastSection =
    document.getElementById("roastSection");
const roastFlash =
    document.getElementById("roastFlash");
const roastLabel =
    document.getElementById("roastLabel");
const mcqScreen =
    document.getElementById("mcqScreen");
const mcqQuestion =
    document.getElementById("mcqQuestion");
const mcqOptions =
    document.getElementById("mcqOptions");
const mcqProgress =
    document.getElementById("mcqProgress");
const mcqMessage =
    document.getElementById("mcqMessage");
const posterScreen =
    document.getElementById("posterScreen");
const roastImages = [
    document.getElementById("roast1"),
    document.getElementById("roast2"),
    document.getElementById("roast3"),
    document.getElementById("roast4"),
    document.getElementById("roast5"),
    document.getElementById("roast6")
];
const images = [
    document.getElementById("image3"),
    document.getElementById("image4"),
    document.getElementById("image5"),
    document.getElementById("image7")
];
let currentImage = 0;
let imageTimer = null;
// ============================================================
// SHOW VIDEO BACKGROUND
// ============================================================
function setMediaBackground(videoElement) {{
    try {{
        mediaBackground.style.backgroundImage =
            `url(${{videoElement.currentSrc}})`;
        mediaBackground.classList.add(
            "visible"
        );
    }} catch(error) {{
        console.log(
            "Background error:",
            error
        );
    }}
}}
// ============================================================
// HIDE ALL VIDEOS
// ============================================================
function hideVideos() {{
    baby.classList.remove("active");
    psych.classList.remove("active");
    honorable.classList.remove("active");
}}
// ============================================================
// SHOW BIRTHDAY IMAGE
// ============================================================
function showBirthdayImage(index) {{
    images.forEach(
        image => image.classList.remove("show")
    );
    if (
        index >= 0 &&
        index < images.length
    ) {{
        images[index].classList.add("show");
        photoBackground.style.backgroundImage =
            `url(${{images[index].src}})`;
    }}
}}
// ============================================================
// START BIRTHDAY SECTION
// ============================================================
function startBirthdaySection() {{
    hideVideos();
    mediaBackground.classList.remove(
        "visible"
    );
    black.classList.remove(
        "hide"
    );
    setTimeout(() => {{
        birthdaySection.classList.add(
            "active"
        );
        currentImage = 0;
        showBirthdayImage(
            currentImage
        );
        // Start audio
        birthdayAudio.currentTime = 0;
        birthdayAudio.play().catch(
            error => {{
                console.log(
                    "Birthday audio error:",
                    error
                );
            }}
        );
        // Four images across 10 seconds
        imageTimer = setInterval(() => {{
            currentImage++;
            if (
                currentImage < images.length
            ) {{
                showBirthdayImage(
                    currentImage
                );
            }}
        }}, 2500);
        setTimeout(() => {{
            black.classList.add(
                "hide"
            );
        }}, 400);
    }}, 700);
}}
// ============================================================
// START EXPERIENCE
// ============================================================
async function startExperience(){{
    startScreen.classList.add(
        "hidden"
    );
    black.classList.remove(
        "hide"
    );
    hideVideos();
    baby.classList.add(
        "active"
    );
    try {{
        await baby.play();
        setTimeout(() => {{
            black.classList.add(
                "hide"
            );
        }}, 400);
    }}
    catch(error) {{
        console.log(
            "Baby playback error:",
            error
        );
    }}
}}
// ============================================================
// START BUTTON
// ============================================================
startButton.addEventListener(
    "click",
    startExperience
);
// ============================================================
// BABY → PSYCH
// ============================================================
baby.addEventListener(
    "ended",
    () => {{
        console.log(
            "Baby finished"
        );
        black.classList.remove(
            "hide"
        );
        baby.classList.remove(
            "active"
        );
        setTimeout(() => {{
            psych.classList.add(
                "active"
            );
            try {{
                psych.currentTime = 0;
                psych.play();
            }}
            catch(error) {{
                console.log(
                    "Psych playback error:",
                    error
                );
            }}
            setTimeout(() => {{
                black.classList.add(
                    "hide"
                );
            }}, 350);
        }}, 600);
    }}
);
// ============================================================
// PSYCH → BIRTHDAY
// ============================================================
psych.addEventListener(
    "ended",
    () => {{
        console.log(
            "Psych finished"
        );
        psych.pause();
        startBirthdaySection();
    }}
);
// ============================================================
// BIRTHDAY → CHURCHILL
// ============================================================
birthdayAudio.addEventListener(
    "ended",
    () => {{
        console.log(
            "Birthday section finished"
        );
        clearInterval(
            imageTimer
        );
        birthdaySection.classList.remove(
            "active"
        );
        black.classList.remove(
            "hide"
        );
        setTimeout(() => {{
            honorable.classList.add(
                "active"
            );
            try {{
                honorable.currentTime = 0;
                honorable.play();
            }}
            catch(error) {{
                console.log(
                    "Churchill playback error:",
                    error
                );
            }}
            setTimeout(() => {{
                black.classList.add(
                    "hide"
                );
            }}, 350);
        }}, 700);
    }}
);
// ============================================================
// ============================================================
// ROAST EDIT — CINEMATIC
// ============================================================
let roastRunning = false;
let roastLastCut = -1;
let roastRaf = null;
const roastTimeline = [
    {{ time: 0.00, image: 0, effect: "roast-intro",  flash: false, black: false }},
    {{ time: 1.05, image: 1, effect: "zoom-in",       flash: false, black: false }},
    {{ time: 1.58, image: 2, effect: "rotate-left",   flash: true,  black: false }},
    {{ time: 2.10, image: 3, effect: "zoom-out",      flash: false, black: false }},
    {{ time: 2.62, image: 4, effect: "shake",         flash: true,  black: false }},
    {{ time: 3.08, image: 5, effect: "punch",         flash: false, black: false }},
    {{ time: 3.48, image: 0, effect: "punch",         flash: true,  black: true  }},
    {{ time: 3.82, image: 2, effect: "rotate-right",  flash: false, black: false }},
    {{ time: 4.16, image: 4, effect: "zoom-in",       flash: true,  black: false }},
    {{ time: 4.48, image: 1, effect: "shake",         flash: false, black: false }},
    {{ time: 4.80, image: 5, effect: "punch",         flash: true,  black: false }},
    {{ time: 5.10, image: 3, effect: "zoom-in",       flash: true,  black: true  }},
    {{ time: 5.38, image: 0, effect: "slide-left",    flash: false, black: false }},
    {{ time: 5.66, image: 4, effect: "rotate-right",  flash: true,  black: false }},
    {{ time: 5.94, image: 2, effect: "punch",         flash: false, black: false }},
    {{ time: 6.22, image: 5, effect: "zoom-out",      flash: true,  black: false }},
    {{ time: 6.50, image: 1, effect: "shake",         flash: false, black: true  }},
    {{ time: 6.76, image: 3, effect: "punch",         flash: true,  black: false }},
    {{ time: 7.02, image: 0, effect: "rotate-left",   flash: false, black: false }},
    {{ time: 7.28, image: 5, effect: "zoom-in",       flash: true,  black: false }},
    {{ time: 7.54, image: 2, effect: "shake",         flash: false, black: false }},
    {{ time: 7.80, image: 4, effect: "punch",         flash: true,  black: true  }},
    {{ time: 8.06, image: 1, effect: "rotate-right",  flash: false, black: false }},
    {{ time: 8.32, image: 5, effect: "zoom-in",       flash: true,  black: false }},
    {{ time: 8.58, image: 3, effect: "shake",         flash: false, black: false }},
    {{ time: 8.84, image: 0, effect: "punch",         flash: true,  black: false }},
    {{ time: 9.12, image: 4, effect: "zoom-out",      flash: false, black: true  }},
    {{ time: 9.40, image: 5, effect: "zoom-in",       flash: true,  black: false }},
    {{ time: 9.72, image: 5, effect: "punch",         flash: true,  black: false }},
    {{ time: 10.04, image: 5, effect: "final-hit",    flash: true,  black: false }},
    {{ time: 10.52, image: 5, effect: "final-hit",    flash: true,  black: false }}
];
function clearRoastEffects() {{
    roastImages.forEach((image) => {{
        image.className = "roast-image";
        image.style.transform = "scale(1) translate3d(0,0,0) rotate(0deg)";
        image.style.filter = "none";
    }});
}}
function triggerRoastFlash() {{
    roastFlash.classList.remove("hit");
    void roastFlash.offsetWidth;
    roastFlash.classList.add("hit");
}}
function blackRoastHit(duration) {{
    roastSection.classList.add("black-hit");
    setTimeout(() => {{
        if (roastRunning) {{
            roastSection.classList.remove("black-hit");
        }}
    }}, duration);
}}
function showRoastCut(cut) {{
    clearRoastEffects();
    const image = roastImages[cut.image];
    image.classList.add("active", cut.effect);
    if (cut.flash) {{
        triggerRoastFlash();
    }}
    if (cut.black) {{
        blackRoastHit(70);
    }}
    roastLabel.classList.add("show");
}}
function runRoastTimeline() {{
    if (!roastRunning) {{
        return;
    }}
    const currentTime = roastAudio.currentTime;
    let selectedIndex = -1;
    for (let i = 0; i < roastTimeline.length; i++) {{
        if (currentTime >= roastTimeline[i].time) {{
            selectedIndex = i;
        }} else {{
            break;
        }}
    }}
    if (selectedIndex >= 0 && selectedIndex !== roastLastCut) {{
        roastLastCut = selectedIndex;
        showRoastCut(roastTimeline[selectedIndex]);
    }}
    roastRaf = requestAnimationFrame(runRoastTimeline);
}}
function startRoastEdit() {{
    roastRunning = true;
    roastLastCut = -1;
    if (roastRaf) {{
        cancelAnimationFrame(roastRaf);
        roastRaf = null;
    }}
    roastSection.classList.add("active");
    roastSection.classList.remove("black-hit");
    clearRoastEffects();
    roastLabel.classList.remove("show");
    roastAudio.pause();
    roastAudio.currentTime = 0;
    roastAudio.play().catch((error) => {{
        console.log("Roast audio playback error:", error);
    }});
    roastRaf = requestAnimationFrame(runRoastTimeline);
}}
function finishRoastEdit() {{
    roastRunning = false;
    if (roastRaf) {{
        cancelAnimationFrame(roastRaf);
        roastRaf = null;
    }}
    roastAudio.pause();
    roastAudio.currentTime = 0;
    roastSection.classList.remove("active");
    roastSection.classList.remove("black-hit");
    clearRoastEffects();
    roastLabel.classList.remove("show");
    black.classList.remove("hide");
    setTimeout(() => {{
        startMCQ();
    }}, 450);
}}
// ============================================================
// POST EDIT MCQ
// ============================================================
let currentQuestion = 0;
let mcqLocked = false;
const mcqQuestions = [
    {{
        question: "Did you like the edit?",
        progress: "01 / 02",
        options: [
            ["A", "Yes"],
            ["B", "Yes"],
            ["C", "Yes"],
            ["D", "All four"]
        ],
        correct: "D"
    }},
    {{
        question: "What would you like to gift the creators?",
        progress: "02 / 02",
        options: [
            ["A", "₹10,000 each"],
            ["B", "PS5 along with GTA 6"],
            ["C", "Northrop B-2 Spirit Stealth Bomber"],
            ["D", "All of the above"]
        ],
        correct: "D"
    }}
];
function startMCQ() {{
    currentQuestion = 0;
    mcqLocked = false;
    mcqScreen.classList.add("active");
    black.classList.remove("hide");
    setTimeout(() => {{
        black.classList.add("hide");
        showMCQQuestion();
    }}, 300);
}}
function showMCQQuestion() {{
    const question = mcqQuestions[currentQuestion];
    mcqLocked = false;
    mcqQuestion.textContent = question.question;
    mcqProgress.textContent = question.progress;
    mcqMessage.textContent = "";
    mcqMessage.classList.remove("show");
    mcqOptions.innerHTML = "";
    question.options.forEach((option) => {{
        const button = document.createElement("button");
        button.className = "mcq-option";
        button.dataset.answer = option[0];
        const letter = document.createElement("span");
        letter.textContent = option[0];
        const label = document.createElement("div");
        label.textContent = option[1];
        button.appendChild(letter);
        button.appendChild(label);
        button.addEventListener("click", () => {{
            handleMCQAnswer(button, option[0]);
        }});
        mcqOptions.appendChild(button);
    }});
}}
function handleMCQAnswer(button, answer) {{
    if (mcqLocked) {{
        return;
    }}
    const question = mcqQuestions[currentQuestion];
    const allButtons =
        mcqOptions.querySelectorAll(".mcq-option");
    if (answer !== question.correct) {{
        button.classList.add("wrong");
        mcqMessage.textContent =
            "Incorrect. Please reconsider your priorities.";
        mcqMessage.classList.add("show");
        setTimeout(() => {{
            button.classList.remove("wrong");
            mcqMessage.classList.remove("show");
        }}, 900);
        return;
    }}
    mcqLocked = true;
    allButtons.forEach((option) => {{
        option.disabled = true;
    }});
    button.classList.add("correct");
    mcqMessage.textContent =
        currentQuestion === 0
            ? "Correct. We knew you had taste."
            : "Correct. Your generosity is appreciated.";
    mcqMessage.classList.add("show");
    setTimeout(() => {{
        if (currentQuestion < mcqQuestions.length - 1) {{
            currentQuestion++;
            showMCQQuestion();
        }} else {{
            finishMCQ();
        }}
    }}, 1300);
}}
function finishMCQ() {{
    mcqQuestion.textContent =
        "Thank you for your valuable contribution.";
    mcqProgress.textContent =
        "SUBMISSION ACCEPTED";
    mcqOptions.innerHTML = "";
    mcqMessage.textContent =
        "Your generosity has been formally documented.";
    mcqMessage.classList.add("show");
    setTimeout(() => {{
        mcqScreen.classList.remove("active");
        black.classList.remove("hide");
        setTimeout(() => {{
            posterScreen.classList.add("active");
            black.classList.add("hide");
        }}, 350);
    }}, 2200);
}}
roastAudio.addEventListener("ended", finishRoastEdit);
// ============================================================
// CHURCHILL → ROAST
// ============================================================
honorable.addEventListener(
    "ended",
    () => {{
        console.log("Churchill finished");
        honorable.pause();
        honorable.classList.remove("active");
        black.classList.remove("hide");
        setTimeout(() => {{
            startRoastEdit();
            setTimeout(() => {{
                black.classList.add("hide");
            }}, 300);
        }}, 500);
    }}
);
</script>
</body>
</html>
"""
    components.html(
        EDIT,
        height=900,
        scrolling=False
    )
# ============================================================
# ROUTING
# ============================================================
page = st.query_params.get(
    "page",
    "intro"
)
if page == "edit":
    edit_page()
else:
    intro_page()