import random
from playwright.sync_api import Page


def test_vendor_registration(page: Page) -> None:

    # ====================================================
    # GENERATE UNIQUE EMAIL
    # ====================================================

    random_number = random.randint(1000, 9999)

    email = f"krishanu{random_number}@gmail.com"

    password = "572000@Krish"

    # ====================================================
    # OPEN WEBSITE
    # ====================================================

    page.goto("https://stg.proquro.ai/")

    # ====================================================
    # SIGN UP
    # ====================================================

    page.get_by_role("link", name="Sign In").click()

    page.get_by_role("button", name="Sign Up", exact=True).click()

    page.get_by_role("checkbox", name="I agree to Trafasa's Terms &").check()

    page.get_by_role("button", name="Securely Signup With Email").click()

    page.get_by_role("textbox", name="Email").fill(email)

    page.get_by_role("textbox", name="Password").fill(password)

    page.get_by_role("button", name="Sign Up").click()

    page.get_by_role("button", name="Accept").click()

    print(f"\nAccount Created Successfully: {email}")

    # ====================================================
    # GST DETAILS
    # ====================================================

    page.get_by_role("textbox", name="Enter 15-digit GSTIN (e.g.,").fill(
        "22AAACI1681G1ZZ"
    )

    # ====================================================
    # CAPTCHA MANUAL STEP
    # ====================================================

    print("\n===================================")
    print("ENTER CAPTCHA MANUALLY")
    print("After entering CAPTCHA click RESUME in Playwright")
    print("===================================\n")

    page.pause()

    # Continue after clicking Resume

    page.get_by_role("button", name="Verify GST").click()

    # ====================================================
    # COMPANY DETAILS
    # ====================================================

    page.get_by_role("textbox", name="Enter Brand Name").fill("tata brand")

    page.get_by_role("textbox", name="Enter CIN (e.g.,").fill("L01631KA2010PTC096843")

    page.get_by_role("textbox", name="Enter Company Website").fill(
        "https://www.tcs.com/"
    )

    # ====================================================
    # INDUSTRY
    # ====================================================

    page.get_by_role("button", name="Select Industry").click()

    page.get_by_role("textbox", name="Search…").fill("so")

    page.get_by_text("Electronic Components,").click()

    # ====================================================
    # COMPANY SIZE
    # ====================================================

    page.get_by_role("button", name="Select Company Size").click()

    page.get_by_role("textbox", name="Search…").fill("ent")

    page.get_by_text("Enterprise (1000+)").click()

    # ====================================================
    # NATURE OF BUSINESS
    # ====================================================

    page.get_by_role("button", name="Select Nature Of Business").click()

    page.get_by_text("Manufacturing").click()

    # ====================================================
    # TRADE SCOPE
    # ====================================================

    page.get_by_role("button", name="Select Trade Scope").click()

    page.get_by_text("Domestic").click()

    # ====================================================
    # ABOUT COMPANY
    # ====================================================

    page.locator(".tiptap").fill("This is about tata company")

    page.get_by_role("button", name="Save Progress").click()

    page.get_by_role("button", name="Next").click()

    # ====================================================
    # CONTACT DETAILS
    # ====================================================

    page.get_by_role("textbox", name="Enter Contact Person Name").fill("Anish shaw")

    page.get_by_role("textbox", name="Enter Designation").fill("manager")

    page.get_by_role("textbox", name="Enter Primary Contact Number").fill("7364833882")

    page.get_by_role("checkbox", name="Same as Primary").click()

    page.get_by_role("textbox", name="Enter Alternate Phone Number").fill("1234567890")

    page.get_by_role("button", name="Save Progress").click()

    page.get_by_role("button", name="Next").click()

    # ====================================================
    # BUSINESS DETAILS
    # ====================================================

    page.get_by_role("button", name="Save Progress").click()

    page.get_by_role("button", name="Next").click()

    # ====================================================
    # CATEGORY DETAILS
    # ====================================================

    categories = [
        "Raw Materials",
        "Textiles",
        "Safety Equipment",
        "Chemicals",
        "Office Supplies",
        "Food & Beverages",
        "Machinery & Equipment",
        "Construction Materials",
        "Electronics",
        "Packaging Materials",
        "Automotive Parts",
        "Services",
    ]

    for category in categories:

        page.get_by_role("checkbox", name=category).click()

    # ====================================================
    # OTHER CATEGORY
    # ====================================================

    page.get_by_role("checkbox", name="Other Other").click()

    page.get_by_role("textbox", name="Category Name *").fill("unknown")

    page.get_by_role("button", name="Add Category").click()

    # ====================================================
    # RANGE
    # ====================================================

    page.get_by_role("button", name="Select Range").click()

    page.get_by_role("textbox", name="Search…").fill("Le")

    page.get_by_text("Less than 1 Lakh").click()

    # ====================================================
    # FREQUENCY
    # ====================================================

    page.get_by_role("button", name="Select Frequency").click()

    page.get_by_role("textbox", name="Search…").fill("an")

    page.get_by_text("Annually", exact=True).click()

    # ====================================================
    # REGIONS
    # ====================================================

    page.get_by_role("textbox", name="List cities or regions where").fill(
        "all over kolkata"
    )

    # ====================================================
    # REQUIREMENTS
    # ====================================================

    page.get_by_role("textbox", name="Any specific quality").fill(
        "no other requirements"
    )

    page.get_by_role("button", name="Save Progress").click()

    page.get_by_role("button", name="Next").click()

    # ====================================================
    # DOCUMENT UPLOAD MANUAL STEP
    # ====================================================



    import os

    current_dir = os.path.dirname(__file__)

    gst_file = os.path.join(current_dir, "documents", "7 july prescription.pdf")

    pan_file = os.path.join(current_dir, "documents", "7 july prescription.pdf")

    company_file = os.path.join(
        current_dir,
        "documents",
        "7 july prescription.pdf"
    )

    # ---------------- GST CERTIFICATE ---------------- #

    page.locator('input[type="file"]').nth(0).set_input_files(
        gst_file
    )

    # ---------------- PAN CARD ---------------- #

    page.locator('input[type="file"]').nth(1).set_input_files(
        pan_file
    )

    # ---------------- COMPANY CERTIFICATE ---------------- #

    page.locator('input[type="file"]').nth(2).set_input_files(
        company_file
    )

    print("\nDocuments Uploaded Successfully\n")

    # Continue after clicking Resume

    page.get_by_role("button", name="Save Progress").click()

    page.get_by_role("button", name="Next").click()

    # ====================================================
    # LANGUAGE
    # ====================================================

    page.get_by_role("checkbox").nth(1).click()

    page.get_by_role("checkbox").nth(5).click()

    page.get_by_role("button", name="Select Language").click()

    page.get_by_text("English").click()

    page.get_by_role("button", name="Save Progress").click()

    page.get_by_role("button", name="Next").click()

    # ====================================================
    # FINAL AGREEMENTS
    # ====================================================

    for i in range(4):

        page.get_by_role("checkbox").nth(i).click()

    page.get_by_role("button", name="Save Progress").click()

    print("\n===================================")
    print("VENDOR REGISTRATION COMPLETED")
    print("===================================\n")
