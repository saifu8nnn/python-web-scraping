📚 Books to Scrape — Web Scraping Project (Python)

📌 Overview

This project is a Python-based web scraper built to extract structured book data from the **Books to Scrape** website.
It demonstrates real-world web scraping techniques using **BeautifulSoup**, including pagination handling, nested requests, data cleaning, and exporting results into a CSV file.

The scraper focuses on **logic-driven extraction** and **error-tolerant scraping**, making it suitable for hackathons and practical data extraction tasks.

---

🧠 What This Project Scrapes

For each book, the scraper extracts:

* **Book Title**
* **Price** (numeric, cleaned from currency symbols)
* **Availability Status**
* **Star Rating** (converted from text to numbers)
* **Product Page URL** (absolute link)
* **Category** (extracted from the product page breadcrumb)

---

🛠️ Technologies Used

* **Python**
* **Requests** — HTTP requests
* **BeautifulSoup (bs4)** — HTML parsing
* **Pandas** — Data structuring and CSV export
* **Regex (re)** — Robust data cleaning
* **Time & Random** — Request throttling

---

⚙️ How the Scraper Works (Logic Flow)

1. Sends HTTP requests to paginated listing pages
2. Parses book cards from each page
3. Extracts listing-level data (title, price, rating, availability)
4. Converts relative URLs into absolute product page URLs
5. Sends secondary requests to each product page to fetch category data
6. Handles missing or inconsistent data using defensive `try-except` logic
7. Cleans raw text data (currency symbols, whitespace, encodings)
8. Stores structured data in a Pandas DataFrame
9. Exports the final dataset to a CSV file

---

🧼 Data Cleaning Highlights

* Currency symbols and encoding artifacts are removed using **regex**
* Star ratings are mapped from words (`One`, `Two`, etc.) to integers
* Missing fields are safely handled without crashing the script

---

📂 Output

The scraper generates a CSV file:

```
Books_info.csv
```

Sample Columns:

* Book Title
* Price
* Availability
* Star Rating
* Product Page URL
* Category


🚀 How to Run the Project

1️⃣ Install dependencies

```bash
pip install requests beautifulsoup4 pandas
```

2️⃣ Run the script

```bash
python scrapper.py
```

⚠️ Notes

* The scraper intentionally limits pagination to a few pages to avoid overloading the server.
* A small delay is added between requests to ensure stable execution.
* Multithreading is **not used** to keep the logic simple and readable.

---

🎯 Project Purpose

This project was built to:

* Strengthen understanding of web scraping logic
* Handle real-world HTML inconsistencies
* Practice hackathon-style data extraction workflows
* Convert raw web data into clean, usable datasets

📌 Disclaimer

This project is intended for educational purposes only.
Always review and respect a website’s terms of service before scraping.
