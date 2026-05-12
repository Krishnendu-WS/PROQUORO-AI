from playwright.sync_api import sync_playwright
from datetime import datetime,timedelta
 
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
    next_day = datetime.now()+ timedelta(days=5)
    next_day = next_day.day
    page.get_by_role("button", name="Select date").click()
    page.get_by_role("button", name=str(next_day)).click()


    #justification
    page.get_by_role("textbox", name="State the business need — why").click()
    page.get_by_role("textbox", name="State the business need — why").fill("This item is required because i want it")

    #item code
    page.locator("button").filter(has_text="Search item…").click()
    page.get_by_role("listbox").get_by_text("Cutting Disc 230mm 3mm Variant").click()


    #Add item
    page.get_by_role("button", name="Add Item").click()


    page.locator("button").filter(has_text="Search item…").click()
    page.get_by_role("textbox", name="Search item…").fill("ABV")
    page.get_by_role("option", name="ABV Item (SKU): SHY456 · HSN").click()

    
    page.get_by_role("button", name="Submit").click()

    #code for new item *****************************************************************


    #Submit
    # page.get_by_role("button", name="Submit").click()




 
    input("Press Enter to close browser...")
    browser.close()
    