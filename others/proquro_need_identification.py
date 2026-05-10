from playwright.sync_api import sync_playwright
import json
from datetime import datetime

# ── Logger setup ───────────────────────────────────────────────────────────────
log_lines = []

def log(msg):
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    line = f"[{timestamp}] {msg}"
    print(line)
    log_lines.append(line)

def save_log():
    filename = f"proquro_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("\n".join(log_lines))
    print(f"\n📄 Log saved to: {filename}")

# ── Network error capture ──────────────────────────────────────────────────────
def on_response(response):
    if response.status >= 400:
        log(f"🔴 HTTP {response.status} — {response.url}")
        try:
            body = response.text()
            log(f"   Response body: {body[:300]}")
        except Exception:
            pass

def on_request_failed(request):
    log(f"❌ Request FAILED — {request.url}")
    log(f"   Failure: {request.failure}")

def on_console(msg):
    if msg.type in ("error", "warning"):
        log(f"🖥️  Console [{msg.type.upper()}]: {msg.text}")

# ──────────────────────────────────────────────────────────────────────────────

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Attach network + console listeners
    page.on("response", on_response)
    page.on("requestfailed", on_request_failed)
    page.on("console", on_console)

    try:
        # ── Step 1: Navigate to login ──────────────────────────────────────────
        log("🌐 Navigating to login page...")
        page.goto("https://stg.proquro.ai/sign-in?redirect=%2Fcompany-admin%2Frole-management")
        page.wait_for_load_state("networkidle")

        # ── Step 2: Login ──────────────────────────────────────────────────────
        log("🔐 Clicking Login button...")
        page.get_by_role("button", name="Login").click()

        log("📧 Clicking 'Securely Login With Email'...")
        page.get_by_text("Securely Login With Email").click()

        log("⏸️  Pausing for manual credential entry...")
        page.pause()

        page.wait_for_load_state("networkidle")
        log(f"✅ Logged in. URL: {page.url}")

        # ── Step 3: Click hamburger menu ───────────────────────────────────────
        log("🍔 Clicking hamburger menu...")
        page.get_by_role("button").first.click()
        page.wait_for_timeout(800)

        # ── Step 4: Navigate to Need Identification ────────────────────────────
        log("🔗 Clicking 'Need Identification' link...")
        page.get_by_role("link", name="Need Identification").click()
        page.wait_for_load_state("networkidle")
        log(f"📍 URL: {page.url}")

        # ── Step 5: Click New Requirement ─────────────────────────────────────
        log("🆕 Clicking 'New Requirement' button...")
        page.get_by_role("button", name="New Requirement").click()
        page.wait_for_timeout(1000)  # Wait for modal/form to appear

        # ── Step 6: Fill SMS textbox ───────────────────────────────────────────
        log("📱 Locating SMS number textbox...")

        sms_value = "9876543210"
        filled = False

        strategies = [
            lambda: page.get_by_placeholder("For SMS alerts").fill(sms_value),
            lambda: page.get_by_placeholder("SMS").fill(sms_value),
            lambda: page.get_by_placeholder("phone").fill(sms_value),
            lambda: page.get_by_label("For SMS alerts").fill(sms_value),
            lambda: page.locator("input[type='tel']").first.fill(sms_value),
            lambda: page.locator("input[placeholder*='SMS' i]").fill(sms_value),
            lambda: page.locator("input[placeholder*='phone' i]").fill(sms_value),
            lambda: page.locator("input[placeholder*='mobile' i]").fill(sms_value),
            lambda: page.get_by_role("textbox", name="For SMS alerts").fill(sms_value),
        ]

        for i, strategy in enumerate(strategies):
            try:
                strategy()
                log(f"✅ SMS field filled via strategy {i + 1}")
                filled = True
                break
            except Exception as e:
                log(f"   Strategy {i + 1} failed: {e}")

        if not filled:
            # Diagnostic: list all visible input fields in the form
            log("⚠️  Could not fill SMS field. Listing all visible inputs:")
            inputs = page.evaluate("""
                () => [...document.querySelectorAll('input, textarea')]
                    .filter(el => el.offsetParent !== null)
                    .map(el => ({
                        type: el.type,
                        name: el.name,
                        placeholder: el.placeholder,
                        label: el.labels?.[0]?.textContent?.trim() || '',
                        id: el.id
                    }))
            """)
            for inp in inputs:
                log(f"   input: type={inp['type']} | name={inp['name']} | "
                    f"placeholder='{inp['placeholder']}' | label='{inp['label']}' | id={inp['id']}")

        # ── Step 7: Verify value was entered ──────────────────────────────────
        if filled:
            page.wait_for_timeout(500)
            actual = page.evaluate("""
                () => {
                    const inputs = [...document.querySelectorAll('input')];
                    const sms = inputs.find(i =>
                        i.placeholder?.toLowerCase().includes('sms') ||
                        i.type === 'tel'
                    );
                    return sms ? sms.value : null;
                }
            """)
            if actual == sms_value:
                log(f"✅ Verified: SMS field contains '{actual}'")
            else:
                log(f"⚠️  SMS field value mismatch. Expected '{sms_value}', got '{actual}'")

    except Exception as e:
        log(f"💥 Script error: {e}")

    finally:
        save_log()
        page.wait_for_timeout(5000)
        browser.close()
