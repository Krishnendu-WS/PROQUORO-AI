from playwright.sync_api import sync_playwright
 
with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
 
    # ── Step 1: Go to login page ───────────────────────────────────────────────
    page.goto("https://stg.proquro.ai/sign-in?redirect=%2Fcompany-admin%2Frole-management")
 
    # ── Step 2: Login ──────────────────────────────────────────────────────────
    page.get_by_role("button", name="Login").click()
    page.get_by_text("Securely Login With Email").click()
 
    # Pause
    # page.pause()

    #*manual credential entry
    input("Do your manual steps, then press Enter...")
 
    page.get_by_role("button").first.click()
    page.get_by_role("link", name="Need Identification").click()
    page.get_by_role("button", name="New Requirement").click()

    #Requestor Mobile
    page.wait_for_load_state("networkidle")
    textbox = page.get_by_role("textbox", name="For SMS alerts")
    textbox.wait_for(state="visible")
    textbox.type("9856784466",delay=100)

    #Department
    page.get_by_role("button", name="Department").click()
    page.get_by_text("MOBILE PARK - Departments").click()

    #Cost Centre
    page.get_by_role("button", name="Cost Centre").click()
    page.get_by_text("Global Digital Marketing").click()

    #Request Type
    page.get_by_role("button", name="Request Type").click()
    page.get_by_role("listbox").get_by_text("Product").click()

    #priority
    page.get_by_role("button", name="Priority").click()
    page.get_by_role("listbox").get_by_text("Medium").click()


    #date
    page.get_by_role("textbox").nth(5).fill("2026-06-06")


    #justification
    page.get_by_role("textbox", name="State the business need — why").click()
    page.get_by_role("textbox", name="State the business need — why").fill("This item is required because i want it")

    #item code
    page.locator("button").filter(has_text="Search item…").click()
    page.get_by_role("listbox").get_by_text("Cutting Disc 230mm 3mm Variant").click()

    page.get_by_role("button", name="Add Item").click()


 
    input("Press Enter to close browser...")
    browser.close()
    