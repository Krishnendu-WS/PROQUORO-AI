from playwright.sync_api import sync_playwright
 
with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False,slow_mo=500)
    page = browser.new_page()
 
    # ── Step 1: Go to login page ───────────────────────────────────────────────
    page.goto("https://stg.proquro.ai/sign-in?redirect=%2Fcompany-admin%2Frole-management")
 
    # ── Step 2: Login ──────────────────────────────────────────────────────────
    page.get_by_role("button", name="Login").click()
    page.get_by_text("Securely Login With Email").click()
 
    # Pause
    page.pause()

    #*manual credential entry
    # input("Do your manual steps, then press Enter...")

    #Dashboard
    page.get_by_role("button").first.click()

    #RFQ Management
    page.get_by_role("link", name="RFQ Management").click()


    #Search By RFQ IDS
    # page.get_by_role("textbox", name="Search RFQs...").click()
    # page.get_by_role("textbox", name="Search RFQs...").fill("RFQ-2026-00010")

    page.wait_for_load_state("networkidle")

    row = page.locator("tr").filter(has_text="RFQ-2026-00015")
    row.get_by_role("link", name="View").click()


    

    #confirm
    page.get_by_role("button", name="Confirm").click()
    page.get_by_role("button",name="Confirm & Generate POs").click()

    input("Press Enter to close browser...")
    browser.close()