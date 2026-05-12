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

    #manual credential entry
    # input("Do your manual steps, then press Enter...")

    #Dashboard
    page.get_by_role("button").first.click()

    #Indent Management
    page.get_by_role("link", name="Indent Management").click()

    #create new indent 
    page.get_by_role("button", name="+ Create New Indent").click()

    #Indent Title
    page.get_by_role("textbox", name="e.g., IT Equipment - Q1").click()
    page.get_by_role("textbox", name="e.g., IT Equipment - Q1").fill("IT equipment-Q9")

    #Department
    page.get_by_role("button", name="Select Department").click()
    page.get_by_role("option", name="Data Aanalyst").click()

    #Cost Center
    page.get_by_role("button", name="Select Cost Center").click()
    page.get_by_role("textbox", name="Search…").fill("KOLKATA HUB")
    page.get_by_role("option", name="KOLKATA HUB").click()

    #Required Date
    next_5day = datetime.now()+ timedelta(days=5)
    next_5day = next_5day.day

    page.get_by_role("button", name="Select date").click()
    page.get_by_role("button", name=str(next_5day)).click()

    #Priority
    page.get_by_role("button", name="Normal").click()
    page.get_by_role("option", name="Urgent").click()

    #select Location
    page.get_by_role("button", name="Select Location").click()
    page.get_by_role("option", name="kolkata, kolkata, wb,").click()

    #Classification
    page.get_by_role("button", name="Product").click()
    page.get_by_role("option", name="Service").click()

    #Brief
    page.get_by_role("textbox", name="Brief justification for the").click()
    page.get_by_role("textbox", name="Brief justification for the").fill("This is Demo notes")
    #next
    page.get_by_role("button", name="Next →").click()

    #Item Name
    page.get_by_role("button", name="Search and select item...").click()
    page.get_by_role("textbox", name="Search…").fill("ABV")
    page.get_by_role("option", name="ABV fdbgdbgdf UoM: Pair HSN:").click()


    #Quantity
    page.get_by_role("textbox", name="1", exact=True).click()
    page.get_by_role("textbox", name="1", exact=True).fill("1")

    #Next
    page.get_by_role("button", name="Next →").click()

    #submit
    page.get_by_role("button", name="Submit").click()


    page.pause()

    input("Press Enter to close browser...")
    browser.close()