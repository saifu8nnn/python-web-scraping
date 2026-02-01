from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup  # CORRECTION: Proper import syntax

# -------------------- SETUP --------------------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.welcometothejungle.com/en")

# -------------------- COOKIE POPUP --------------------
try:
   
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "axeptio_btn_acceptAll"))
    )
    accept_button.click()
    print(" Cookies accepted.")
except:
    print("Cookie pop-up not found or already closed.")

#------------------- Removing the popup ----------------------
try:
    # Targeting the button using the 'title' and 'data-dialog-dismiss' attributes
    close_popup = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="Close"][data-dialog-dismiss]'))
    )
    close_popup.click()
    print("Dialog popup closed successfully.")
except Exception as e:
    print("No extra dialog popup appeared to close.")

# -------------------- MANUAL SEARCH FLOW --------------------
try:
    search_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='query']"))
    )
    search_input.click()
    print("Clicked the search bar.")

    search_input.clear()
    search_input.send_keys("Business")
    time.sleep(1)
    search_input.send_keys(Keys.RETURN)
    print("Search submitted.")

    # Waiting for results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-testid='search-results-list-item-wrapper']"))
    )

except Exception as e:
    print(f"Manual search flow skipped: {e}")

# -------------------- SCRAPING LOOP --------------------
BASE_URL = "https://www.welcometothejungle.com/en/jobs"
QUERY = "Business"
COUNTRY = "US"

all_jobs = []
seen_links = set()
page = 1

while True:
    
    url = f"{BASE_URL}?query={QUERY}&refinementList%5Boffices.country_code%5D%5B%5D={COUNTRY}&page={page}"
    print(f"\nLoading page {page}...")
    driver.get(url)

    try:
        
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-testid='search-results-list-item-wrapper']"))
        )
        time.sleep(2) 
    except:
        print("No more jobs found or page failed to load.")
        break

    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    
    job_cards = soup.find_all("li", {"data-testid": "search-results-list-item-wrapper"})

    if not job_cards:
        print("No job cards found on this page.")
        break

    new_jobs_on_page = 0

    for job in job_cards:
        # 1. LINK & TITLE
        h2_tag = job.find("h2")
        link_tag = h2_tag.find_parent("a") if h2_tag else None
        
        if not link_tag or not link_tag.get("href"):
            continue

        job_link = "https://www.welcometothejungle.com" + link_tag["href"]
        if job_link in seen_links:
            continue
            
        seen_links.add(job_link)
        new_jobs_on_page += 1

        job_title = h2_tag.get_text(strip=True) if h2_tag else "N/A"

        # 2. COMPANY NAME (Targeting the specific span class from your HTML)
        company_tag = job.find("span", class_="ewxOXb") 
        company_name = company_tag.get_text(strip=True) if company_tag else "N/A"

        # 3. LOCATION
        location = "N/A"
        loc_icon = job.find("i", attrs={"name": "location"})
        if loc_icon:
            location = loc_icon.parent.get_text(strip=True)

        # 4. CONTRACT TYPE
        job_type = "N/A"
        contract_icon = job.find("i", attrs={"name": "contract"})
        if contract_icon:
            job_type = contract_icon.parent.get_text(strip=True)

        # 5. POSTED DATE
        date_tag = job.find("time")
        posted_date = date_tag.get_text(strip=True) if date_tag else "N/A"

        all_jobs.append({
            "Title": job_title,
            "Company": company_name,
            "Location": location,
            "Type": job_type,
            "Posted": posted_date,
            "Link": job_link
        })

    print(f" Extracted {new_jobs_on_page} new jobs.")
    
    if new_jobs_on_page == 0:
        break

    page += 1
    time.sleep(2)

# -------------------- SAVE --------------------
driver.quit()
import pandas as pd
df = pd.DataFrame(all_jobs)
df.to_csv("wttj_results.csv", index=False)
print(f"\n Done! Total unique jobs saved: {len(df)}")
