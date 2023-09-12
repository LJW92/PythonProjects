from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrom_options)
# driver.get("https://www.amazon.com.au/Philips-Technology-Champagne-HD9870-20/dp/B09T656FPB/ref"
#            "=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=obK7h&content-id=amzn1.sym.a9ee0d91-6c12-4994-a4cb-a9802f05e73c%3Aamzn1"
#            ".symc.409c7fce-cbd2-4cf4-a6cb-824c258c8778&pf_rd_p=a9ee0d91-6c12-4994-a4cb-a9802f05e73c&pf_rd_r"
#            "=NVDQ3YD1ECD2WJWEZ92Z&pd_rd_wg=r8ksj&pd_rd_r=27c3e107-5f3d-4dbd-8a20-01253acf60f2&pd_rd_i=B09T656FPB")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"The price is {price_dollar.text}.{price_cents.text}")
# # driver.close()  closes the tab
# driver.quit()   # quit the entire browser
driver = webdriver.Chrome(options=chrom_options)
driver.get("https://www.python.org/")
times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

for n in range(len(times)):
    events[n] = {
        "time": times[n].text,
        "name": events[n].text
    }
print(events)

