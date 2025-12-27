from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        executable_path="/usr/bin/chromium",  # tương đương binary_location
        args=[
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
        ]
    )

    context = browser.new_context(
        viewport={"width": 1920, "height": 1200}
    )

    page = context.new_page()
    page.goto("https://www.cgv.vn/default/cinox/site/cgv-celadon-tan-phu", wait_until="domcontentloaded")

    print(page.title())

    browser.close()
