import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://stg.proquro.ai/")

    page.get_by_role("link", name="Sign In").click()
    page.get_by_role("link", name="Securely Login With Email").click()

    page.get_by_role("textbox", name="Email").fill("hoyevo2924@gixpos.com")
    page.get_by_role("textbox", name="Password").fill("abcd@1234567")

    page.get_by_role("button", name="Log In").click()

    # GST Details
    page.get_by_role(
        "textbox",
        name="Enter 15-digit GSTIN (e.g.,"
    ).fill("37AAACI1681G2ZN")

    # ================= CAPTCHA PAUSE =================
    print("\nSolve the CAPTCHA manually.")
    print("After entering CAPTCHA, click Resume ▶ in Playwright Inspector.\n")
    page.pause()

    page.get_by_role("button", name="Verify GST").click()


    # Company Details
    page.get_by_role(
        "textbox",
        name="e.g., L01631KA2010PTC096843"
    ).fill("L01631KA2010PTC096843")

    page.locator("text=Select Category").click()
    page.get_by_role("textbox", name="Search…").fill("saf")
    page.get_by_role("option", name="Safety Equipment").click()

    page.get_by_role(
        "textbox",
        name="https://www.yourcompany.com"
    ).fill("https://www.tcs.com/home-page")

    page.get_by_role(
        "textbox",
        name="List your main product"
    ).fill("this is a service based company")

    page.get_by_role(
        "textbox",
        name="Describe your business,"
    ).fill("it offers software services.")

    page.get_by_role("button", name="Save as Draft").click()
    page.get_by_role("button", name="Next Step").click()

    page.get_by_role("button", name="Save as Draft").click()
    page.get_by_role("button", name="Next Step").click()

    page.get_by_role("button", name="Save as Draft").click()
    page.get_by_role("button", name="Next Step").click()

    # File Path
    file_path = r"C:\Users\User\OneDrive\Desktop\Proque testing\document\Azure data engineer certificate.pdf"

    # Upload Documents
    page.get_by_role("button", name="Choose File").first.set_input_files(file_path)
    page.get_by_role("button", name="Choose File").nth(1).set_input_files(file_path)
    page.get_by_role("button", name="Choose File").nth(2).set_input_files(file_path)

    page.get_by_role("button", name="Save as Draft").click()
    page.get_by_role("button", name="Save as Draft").click()
    page.get_by_role("button", name="Next Step").click()

    # Bank Details
    page.get_by_role(
        "textbox",
        name="e.g., KKBK0000123"
    ).fill("SBIN0006888")

    page.get_by_role(
        "textbox",
        name="Enter account number"
    ).fill("35422241461")

    page.get_by_role(
        "textbox",
        name="As per bank records"
    ).fill("Krishanu saha")

    page.get_by_role("combobox").click()
    page.get_by_role("option", name="Saving").click()

    page.get_by_role("combobox").click()
    page.get_by_role("option", name="Current").click()

    # Upload Bank Document
    page.get_by_role("button", name="Choose File").set_input_files(file_path)

    page.get_by_role("button", name="Save as Draft").click()
    page.get_by_role("button", name="Save as Draft").click()
    page.get_by_role("button", name="Next Step").click()

    # Agreements
    
    page.get_by_text("Supplier Terms & Conditions").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_text("Proquro Policies").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_role("checkbox", name="I agree to the Supplier Terms").click()
    page.get_by_role("checkbox", name="I consent to data processing").click()
    page.get_by_role("checkbox", name="I confirm all information").click()
    page.get_by_role("checkbox", name="I commit to maintaining").click()

    page.get_by_role("button", name="Save as Draft").click()
    page.get_by_role("button", name="Save as Draft").click()

    page.get_by_role("button", name="Next Step").click()

    page.get_by_role("button", name="Save as Draft").click()