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
 
    # Pause
    # page.pause()

    #*manual credential entry
    input("Do your manual steps, then press Enter...")

    #Dashboard
    page.get_by_role("button").first.click()


    page.get_by_role("link", name="RFQ Management").click()
    page.get_by_role("link", name="+ Create New RFQ").click()


    #RFx Type
    page.get_by_role("button", name="Select RFx Type").click()
    page.get_by_text("Request for Quotation").click()

    #RFQ Title
    page.get_by_role("textbox", name="Enter RFQ title- RFQ-QUO-YYYY-").click()
    page.get_by_role("textbox", name="Enter RFQ title- RFQ-QUO-YYYY-").fill("RFQ-QUO-YYYY-888888")

    #description
    page.get_by_role("textbox", name="Enter description").click()
    page.get_by_role("textbox", name="Enter description").fill("This is RFQ desc")

    #Procurement Type
    page.get_by_role("button", name="Indigenous").click()

    #Delivery Terms
    page.get_by_role("button", name="Select Delivery Terms").click()
    page.get_by_role("option", name="FOB (Free On Board)").click()


    #Department
    page.get_by_role("button", name="Search and select department").click()
    page.get_by_role("textbox", name="Search departments...").fill("Accounts & Finance Executive")
    page.get_by_role("option", name="Accounts & Finance Executive").click()

    #Cost Center
    page.get_by_role("button", name="Search and select cost center").click()
    page.get_by_role("textbox", name="Search cost centers...").fill("Accounts & Billing")
    page.get_by_role("option", name="Accounts & Billing").click()



    now = datetime.now()
    day, hour, minute, ampm = now.day, now.strftime("%I"), now.strftime("%M"), now.strftime("%p")


    #Publish Date
    page.get_by_role("button", name="Publish Date").click()
    page.get_by_role("button", name=str(day), exact=True).click()
    page.get_by_role("button", name="Hour").click()
    page.locator("div").filter(has_text=re.compile(f"^{hour}$")).click()
    page.get_by_role("button", name="Minute").click()
    minute_plus_one = f"{(int(minute) + 1) % 60:02d}"
    page.locator("div").filter(has_text=re.compile(f"^{minute_plus_one}$")).click()
    page.get_by_role("button", name="AM or PM").click()
    page.locator("div").filter(has_text=re.compile(f"^{ampm}$")).click()
    page.get_by_role("button", name="Apply").click()




    #Bid Start Date
    page.get_by_role("button", name="Bid Start Date").click()
    page.get_by_role("button", name=str(day), exact=True).click()
    page.get_by_role("button", name="Hour").click()
    page.locator("div").filter(has_text=re.compile(f"^{hour}$")).click()
    page.get_by_role("button", name="Minute").click()
    minute_plus_six = f"{(int(minute) + 6) % 60:02d}"
    page.locator("div").filter(has_text=re.compile(f"^{minute_plus_six}$")).click()
    page.get_by_role("button", name="AM or PM").click()
    page.locator("div").filter(has_text=re.compile(f"^{ampm}$")).click()
    page.get_by_role("button", name="Apply").click()


    next_day = datetime.now()+ timedelta(days=1)
    next_day = next_day.day

    # #Bid End Date
    page.get_by_role("button", name="Bid End Date").click()
    page.get_by_role("button", name=str(next_day),exact=True).click()
    page.get_by_role("button", name="Hour").click()
    page.locator("div").filter(has_text=re.compile(f"^{hour}$")).click()
    page.get_by_role("button", name="Minute").click()
    page.locator("div").filter(has_text=re.compile(f"^{minute_plus_one}$")).click()
    page.get_by_role("button", name="AM or PM").click()
    page.locator("div").filter(has_text=re.compile(f"^{ampm}$")).click()
    page.get_by_role("button", name="Apply").click()

    


    #Quote Validity (Days)
    page.get_by_placeholder("Enter number of days").click()
    page.get_by_placeholder("Enter number of days").fill("15")

    #Expected Delivery Date 
    page.get_by_role("button", name="Expected Delivery Date").click()
    page.get_by_role("button", name="30", exact=True).click()

    #Delivery Location
    page.get_by_role("button", name="Select delivery location").click()
    page.get_by_role("option", name="KARIK SMART PRESS-Registered").click()

    #Next
    page.get_by_role("button", name="Next").click()

    # page.wait_for_load_state("networkidle")
    page.pause()

    #Item Name
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()
    page.get_by_role("textbox", name="Search items...").fill("CONCRETE BREAKING FOR PUMP")
    page.get_by_role("option", name="CONCRETE BREAKING FOR PUMP").click()

    #Qty
    page.get_by_role("textbox", name="Qty").click()
    page.get_by_role("textbox", name="Qty").fill("20")

    #Payment Terms
    page.get_by_role("button", name="Payment Terms", exact=True).click()
    page.get_by_role("textbox", name="Search...").fill("90")
    page.get_by_role("option", name="% payment advance 90 %").click()


    
    #Negotiable
    page.get_by_role("switch", name="Negotiable").click()

    #Next
    page.get_by_role("button", name="Next").click()


    #deselect the HSN code
    page.get_by_role("button", name="38249990").click()

    #search vendor
    page.get_by_role("textbox", name="Search vendors...").click()
    page.get_by_role("textbox", name="Search vendors...").fill("jodico1744@exahut.com")
    page.get_by_text("jodico1744@exahut.com").click()

    #Next
    page.get_by_role("button", name="Next").click()

    

    input("Press Enter to close browser...")
    browser.close()