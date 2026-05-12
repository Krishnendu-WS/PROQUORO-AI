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

    #purchase Order
    page.get_by_role("link", name="Purchase Orders").click()


    page.get_by_role("button", name="+ Create Stand Alone PO").click()

    #Date
    day = datetime.now().day
    page.get_by_role("button", name="PO Date").click()
    page.get_by_role("button", name=str(day)).click()

    #priority
    page.get_by_role("button", name="Priority").click()
    page.get_by_role("option", name="High").click()

    #Supplier Name
    page.locator("div").filter(has_text=re.compile(r"^Search and select supplier\.\.\.$")).nth(2).click()
    page.get_by_role("textbox", name="Search suppliers...").fill("Tata consultancy")
    page.get_by_text("Tata consultancy").click()

    #Next
    page.get_by_role("button", name="Next Step →").click()

    #search item
    page.get_by_text("Search item...").click()
    page.get_by_role("textbox", name="Search items...").fill("ABV")
    page.get_by_text("ABV").click()

    

    #QTY
    page.get_by_placeholder("0").first.click()
    page.get_by_placeholder("0").first.fill("2")

    #next
    page.get_by_role("button", name="Next Step →").click()
    #next
    page.get_by_role("button", name="Next Step →").click()

    #Pricing Basis
    page.get_by_role("button", name="Pricing Basis").click()
    page.get_by_role("option", name="Delivered(Door Delivery)").click()

    #Payment Terms
    page.get_by_role("button", name="Payment Terms").click()
    page.get_by_role("textbox", name="Search payment terms…").fill("Cash on Delivery")
    page.get_by_role("option", name="Cash on Delivery").click()

    #payment mode
    page.get_by_role("button", name="Payment Mode").click()
    page.get_by_role("option", name="Cheque").click()

    #date
    next_5day = datetime.now()+ timedelta(days=5)
    next_5day = next_5day.day
    page.get_by_role("button", name="Delivery Date").click()
    page.get_by_role("button", name=str(next_5day)).click()

    #place of supply
    page.get_by_role("button", name="Place of Supply").click()
    page.get_by_role("option", name="IPL Technology - Bengaluru").click()

    #Freight
    page.get_by_role("button", name="Freight").click()
    page.get_by_role("option", name="Extra (To Pay)").click()


    #terms and condition
    page.get_by_role("textbox", name="Enter terms and conditions...").click()
    page.get_by_role("textbox", name="Enter terms and conditions...").fill("This is terms and Condition")
    page.get_by_role("checkbox", name="I have read and agree to the").check()

    #next
    page.get_by_role("button", name="Next Step →").click()

    #for pre
    page.get_by_role("checkbox").first.check()

    #for post
    # page.get_by_role("checkbox").nth(1).click()

    #next
    page.get_by_role("button", name="Next Step →").click()

    page.pause()
    #submit
    # page.get_by_role("button", name="Submit PO for Approval →").click()

    


    input("Press Enter to close browser...")
    browser.close()