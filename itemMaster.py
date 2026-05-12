import sys
import pandas as pd
from playwright.sync_api import sync_playwright

# ── Usage: python itemMaster.py <csv_file> <number_of_rows>
# ── Example: python itemMaster.py Items.csv 10

CSV_FILE = sys.argv[1] if len(sys.argv) > 1 else "Items.csv"
NUM_ROWS = int(sys.argv[2]) if len(sys.argv) > 2 else 1

# ── Load CSV and clean column names
df = pd.read_csv(CSV_FILE)
df.columns = [col.strip().replace("\n", "") for col in df.columns]
df = df.fillna("")
df = df.head(NUM_ROWS)

print(f"Loaded {len(df)} rows from '{CSV_FILE}'")


def fill_item(page, row):
    # Product Name
    page.get_by_role("textbox", name="Enter product name").click()
    page.get_by_role("textbox", name="Enter product name").fill(str(row["Product Name"]))

    # HSN Code
    page.get_by_role("button", name="Select HSN code").click()
    
    page.get_by_role("textbox", name="Type to search HSN codes, e.g.,").fill(str(int(row["HSN Code"])))
    # page.get_by_text(str(row["HSN Code"])).first.click()

    # page.get_by_role("textbox", name="Type to search HSN codes, e.g.,").fill(str(row["HSN Code"]))
    page.get_by_role("listbox").get_by_text(str(int(row["HSN Code"]))).click()
    

    # Old ERP Code
    page.get_by_role("textbox", name="Enter old ERP code or").click()
    page.get_by_role("textbox", name="Enter old ERP code or").fill(str(row["Old ERP Code / Existing Series"]))

    # Item Category (SKU)
    page.get_by_role("button", name="Select Item Category (SKU)").click()
    page.get_by_text(str(row["Item Categories (SKU)"])).click()

    # Product Description
    page.locator(".tiptap").click()
    page.locator(".tiptap").fill(str(row["Product Description"]))

    # Brand
    page.get_by_role("textbox", name="Brand name").click()
    page.get_by_role("textbox", name="Brand name").fill(str(row["Brand"]))

    # Model / Part Number
    page.get_by_role("textbox", name="Manufacturer's model no.").click()
    page.get_by_role("textbox", name="Manufacturer's model no.").fill(str(row["Model/Part Number"]))

    # Unit Price
    page.get_by_placeholder("0.00").click()
    page.get_by_placeholder("0.00").fill(str(row["Unit Price"]))

    # Category
    page.get_by_role("button", name="Select category", exact=True).click()
    page.get_by_role("button", name=str(row["Category"])).click()

    # Sub-Category
    page.get_by_role("button", name="Select sub-category").click()
    page.get_by_role("textbox", name="Type to search...").fill(str(row["Sub-Category"]))
    page.get_by_role("button", name=str(row["Sub-Category"])).click()


    # page.get_by_role("button", name="Select sub-category").click()
    # page.get_by_role("button", name=str(row["Sub-Category"])).click()

    # Item Type
    page.get_by_role("combobox").nth(4).select_option(str(row["Item Type"]))

    # Unit of Measure
    page.get_by_role("button", name="Select UoM").click()
    page.get_by_role("button", name=str(row["Unit of Measure"]), exact=True).click()

    #Stock Quantity
    page.get_by_role("textbox", name="0").click()
    page.get_by_role("textbox", name="0").fill(str(row["Stock Quantity"]))

    # MoQ
    page.get_by_placeholder("0").nth(2).click()
    page.get_by_placeholder("0").nth(2).fill(str(int(row["MoQ"])))

    # Reorder Level
    page.get_by_placeholder("0").nth(3).click()
    page.get_by_placeholder("0").nth(3).fill(str(int(row["Reorder Level"])))

    # Lead Time (Days)
    page.get_by_placeholder("0").nth(4).click()
    page.get_by_placeholder("0").nth(4).fill(str(int(row["Lead Time (Days)"])))

    # Submit
    page.get_by_role("button", name="Create Item").click()
    page.wait_for_load_state("networkidle")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Login
    page.goto("https://stg.proquro.ai/sign-in?redirect=%2Fcompany-admin%2Frole-management")
    page.get_by_role("button", name="Login").click()
    page.get_by_text("Securely Login With Email").click()

    page.pause()

    # input("Complete login manually, then press Enter...")

    page.get_by_role("button").first.click()
    page.get_by_role("link", name="Item Master").click()

    # Loop through each row
    for i, row in df.iterrows():
        print(f"\n[{i+1}/{len(df)}] Adding: {row['Product Name']}")
        try:
            page.get_by_role("button", name="Add Item").click()
            fill_item(page, row)
            print(f"  ✅ Done")
        except Exception as e:
            print(f"  ❌ Error on row {i+1}: {e}")
            input("Fix manually, then press Enter to continue...")

    print(f"\nAll {len(df)} items processed.")
    input("Press Enter to close browser...")
    browser.close()