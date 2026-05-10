import csv
from playwright.sync_api import sync_playwright

CSV_FILE = "Items.csv"
MAX_ROWS = 5


# ─────────────────────────────────────────────────────────────
# Read CSV
# ─────────────────────────────────────────────────────────────
def read_csv(file_path):
    with open(file_path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))[:MAX_ROWS]


# ─────────────────────────────────────────────────────────────
# Helper functions (Reusable)
# ─────────────────────────────────────────────────────────────
def fill_textbox(page, label, value):
    if value:
        page.get_by_role("textbox", name=label).click()
        page.get_by_role("textbox", name=label).fill(value)


def fill_placeholder(page, placeholder, value, index=0):
    if value:
        page.get_by_placeholder(placeholder).nth(index).click()
        page.get_by_placeholder(placeholder).nth(index).fill(value)


def select_dropdown(page, button_name, option_text):
    if option_text:
        page.get_by_role("button", name=button_name).click()
        page.locator(f"text={option_text}").first.click()


# ─────────────────────────────────────────────────────────────
# Main Form Filling Function
# ─────────────────────────────────────────────────────────────
def fill_item_form(page, row, row_num):
    print(f"\nProcessing Row {row_num}: {row.get('Product Name', '')}")

    # Open form
    page.get_by_role("button", name="Add Item").click()
    page.wait_for_load_state("networkidle")

    # 1. Product Name
    fill_textbox(page, "Enter product name", row.get("Product Name", ""))

    # 2. HSN Code (special handling)
    hsn = row.get("HSN Code", "")
    if hsn:
        page.get_by_role("button", name="Select HSN code").click()
        page.get_by_role("textbox", name="Type to search HSN codes, e.g.,").fill(hsn)
        page.locator(f"[role='option']:has-text('{hsn}')").first.click()

    # 3. Old ERP Code
    fill_textbox(page, "Enter old ERP code or", row.get("Old ERP Code", ""))

    # 4. Item Category (SKU)
    select_dropdown(page, "Select Item Category (SKU)", row.get("Item Categories (SKU)", ""))

    # 5. Description (rich text)
    desc = row.get("Product Description", "")
    if desc:
        editor = page.locator(".tiptap")
        editor.click()
        editor.fill(desc)

    # 6. Brand
    fill_textbox(page, "Brand name", row.get("Brand", ""))

    # 7. Model Number
    fill_textbox(page, "Manufacturer's model no.", row.get("Model/Part Number", ""))

    # 8. Stock Quantity
    fill_placeholder(page, "0.00", row.get("Stock Quantity", ""))

    # 9. Category + Sub-category (dynamic)
    category = row.get("Category", "Construction")  # fallback if not in CSV
    sub_cat = row.get("Sub-Category", "")

    page.get_by_role("button", name="Select category").click()
    page.locator(f"text={category}").first.click()

    if sub_cat:
        page.get_by_role("button", name="Select sub-category").click()
        page.locator(f"text={sub_cat}").first.click()

    # 10. Unit of Measure
    select_dropdown(page, "Select UoM", row.get("Unit of Measure", ""))

    # 11–13 Numeric fields
    fill_placeholder(page, "0", row.get("MoQ", ""), 2)
    fill_placeholder(page, "0", row.get("Reorder Level", ""), 3)
    fill_placeholder(page, "0", row.get("Lead Time", ""), 4)

    # Submit
    page.get_by_role("button", name="Create Item").click()
    page.wait_for_load_state("networkidle")

    print(f"Row {row_num} submitted successfully")


# ─────────────────────────────────────────────────────────────
# Main Execution
# ─────────────────────────────────────────────────────────────
def main():
    rows = read_csv(CSV_FILE)
    print(f"Loaded {len(rows)} rows")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login flow
        page.goto("https://stg.proquro.ai/sign-in")
        page.get_by_role("button", name="Login").click()
        page.get_by_text("Securely Login With Email").click()

        input(">>> Login manually and press ENTER...")

        # Navigate to Item Master
        page.get_by_role("button").first.click()
        page.get_by_role("link", name="Item Master").click()
        page.wait_for_load_state("networkidle")

        # Process rows
        for i, row in enumerate(rows, start=1):
            try:
                fill_item_form(page, row, i)
            except Exception as e:
                print(f"Error in row {i}: {e}")
                page.keyboard.press("Escape")

        input(">>> Done. Press ENTER to close browser...")
        browser.close()


if __name__ == "__main__":
    main()