from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---

current_dif = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"



# --- GENERAL SETTINGS ---
PAGE_TITLE = "Mio CV | Mark Gelvoleo"
PAGE_ICON  = ":wave:"
NAME = "Mark Gelvoleo"
DESCRIPTION = """
BUILD BUILD Project.
"""

EMAIL = "mgelvoleo@gmail.com"
SOCIAL_MEDIA = {
    "YouTube" : "https://www.youtube.com/channel/UCONPJsv7l0sS53SukFuInfQ ",
    "LinkedIn": "https://www.linkedin.com/in/markgelvoleo",
    "GitHub"  : "https://github.com/mgelvoleo",
}

PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


st.title("Hello there!")
