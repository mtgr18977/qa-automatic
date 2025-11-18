# Visual diff example using Playwright and Pillow
from playwright.sync_api import sync_playwright
from PIL import Image, ImageChops

def capture(url, path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=path, full_page=True)
        browser.close()

def compare(img1, img2, diff_out):
    a = Image.open(img1).convert('RGBA')
    b = Image.open(img2).convert('RGBA')
    diff = ImageChops.difference(a, b)
    diff.save(diff_out)

if __name__ == '__main__':
    capture('https://example.com', 'screenshot_a.png')
    capture('https://example.com', 'screenshot_b.png')
    compare('screenshot_a.png', 'screenshot_b.png', 'diff.png')
