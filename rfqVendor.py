from playwright.sync_api import sync_playwright

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

    #RFQ recieved
    page.get_by_role("link", name="RFQ Received").click()

    page.get_by_role("button", name="Filter by status").click()
    page.locator("div").filter(has_text=re.compile(r"^Awaiting$")).click()


    view_quote_buttons = page.get_by_role("button", name="View & Quote")
    # Count total buttons
    count = view_quote_buttons.count()
    count1=1
    # print(count)

    #search by rfq title
    # page.get_by_role("textbox", name="Search by RFQ ID, title, or").click()
    # page.get_by_role("textbox", name="Search by RFQ ID, title, or").fill("RFQ-QWE-2026-92029")

    #view and Quote

    for i in range(count1):

        # Re-locate buttons each loop (IMPORTANT)
        page.get_by_role("button", name="View & Quote").nth(i).click()
        # page.get_by_role("button", name="View & Quote").click()
        page.get_by_role("button", name="Quote Now").click()
        page.get_by_role("button", name="Go to Quote Form →").click()

        #set Price
        page.get_by_placeholder("Price").click()
        page.get_by_placeholder("Price").fill("160")

        #Next
        page.get_by_role("button", name="Next →").click()

        #Quote Valid Until
        page.get_by_role("button", name="Quote Valid Until").click()
        page.get_by_role("button", name="15").click()

        #Additional rmark
        page.get_by_role("textbox", name="Add any additional remarks or").click()
        page.get_by_role("textbox", name="Add any additional remarks or").fill("Demo remark quote")

        #Next
        page.get_by_role("button", name="Next →").click()

        #file upload

        page.locator("input[type='file']").set_input_files(r"D:\Krishnendu Chatterjee\python\proquro AI\Mob_Park_Item_Master_Filled.xlsx")

        #Next
        page.get_by_role("button", name="Next →").click()

        #submit Quote
        page.get_by_role("button", name="Submit Quote").click()
        page.get_by_role("button", name="Back to Quote Dashboard").click()
        
        page.pause()

    

    

    input("Press Enter to close browser...")
    browser.close()