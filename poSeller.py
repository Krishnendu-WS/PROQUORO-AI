from playwright.sync_api import sync_playwright
from datetime import datetime,timedelta
import re
 
with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
 
    # ── Step 1: Go to login page ───────────────────────────────────────────────
    page.goto("https://stg.proquro.ai/sign-in?redirect=%2Fcompany-admin%2Frole-management")
 
    # ── Step 2: Login ──────────────────────────────────────────────────────────
    page.get_by_role("button", name="Login").click()
    page.get_by_text("Securely Login With Email").click()
 

    #*manual credential entry
    input("Do your manual steps, then press Enter...")

    #Dashboard
    page.get_by_role("button").first.click()

    page.pause()


    input("Press Enter to close browser...")
    browser.close()