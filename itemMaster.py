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
 
    # page.pause()

    #*manual credential entry
    input("Do your manual steps, then press Enter...")

    page.get_by_role("button").first.click()
    page.get_by_role("link", name="Item Master").click()

    #add item
    page.get_by_role("button", name="Add Item").click()

    #product name
    page.get_by_role("textbox", name="Enter product name").click()
    page.get_by_role("textbox", name="Enter product name").fill("CONCRETE BREAKING FOR FURNACE FLOOR")

    #HSN Code
    page.get_by_role("button", name="Select HSN code").click()
    page.get_by_role("textbox", name="Type to search HSN codes, e.g.,").fill("995411")
    page.get_by_text("995411").click()
    
    #Old ERP Code
    page.get_by_role("textbox", name="Enter old ERP code or").click()
    page.get_by_role("textbox", name="Enter old ERP code or").fill("465")
    
    
    #SKU
    page.get_by_role("button", name="Select Item Category (SKU)").click()
    page.get_by_text("Heavy Duty Valves").click()

    #Product Desc
    page.locator(".tiptap").click()
    page.locator(".tiptap").fill("this is description")


    #Brand name
    page.get_by_role("textbox", name="Brand name").click()
    page.get_by_role("textbox", name="Brand name").fill("aaaa")

    #Model/Part Number
    page.get_by_role("textbox", name="Manufacturer's model no.").click()
    page.get_by_role("textbox", name="Manufacturer's model no.").fill("23")


    page.get_by_placeholder("0.00").click()
    page.get_by_placeholder("0.00").fill("9")

    #catagory
    page.get_by_role("button", name="Select category", exact=True).click()
    page.get_by_role("button", name="Electrical & Electronics").click()

    #sub catagory
    page.get_by_role("button", name="Select sub-category").click()
    page.get_by_role("button", name="CCTV & Surveillance").click()

    #Item Type
    page.get_by_role("combobox").nth(4).select_option("Non-Stock")


    # Unit of Measure
    page.get_by_role("button", name="Select UoM").click()
    page.get_by_role("button", name="Meter", exact=True).click()


    # MoQ
    page.get_by_placeholder("0").nth(2).click()
    page.get_by_placeholder("0").nth(2).fill("2")

    # Reorder Level
    page.get_by_placeholder("0").nth(3).click()
    page.get_by_placeholder("0").nth(3).fill("2")

    #Lead Time (Days)
    page.get_by_placeholder("0").nth(4).click()
    page.get_by_placeholder("0").nth(4).fill("2")

    #submit
    # page.get_by_role("button", name="Create Item").click()

    
    input("Press Enter to close browser...")
    browser.close()