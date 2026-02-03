# Python Web Data Extraction & Scraping Projects

## 📌 Overview

This repository contains a collection of **Python-based web data extraction projects** built as part of my learning journey into **data extraction and data engineering fundamentals**.

The projects progress from **static websites** to **dynamic, JavaScript-rendered websites**, including handling **pagination, infinite scroll, animations, and slow-loading pages**.
The focus is on writing **reliable, structured, and reusable scrapers** for real-world scenarios.

---

## 🛠️ Tech Stack

* **Python**
* **Requests**
* **BeautifulSoup**
* **Selenium**
* **Pandas**
* **Chrome WebDriver**

---

## 📂 Projects Included

### 1️⃣ Static Website Scraping

* Scraped data from static HTML pages
* Extracted structured information such as text, authors, and links
* Stored data in CSV format for further analysis

**Key concepts learned:**

* HTTP requests
* HTML parsing
* Tag & class-based selection
* Data storage using pandas

---

### 2️⃣ Dynamic Website Scraping (JavaScript-rendered)

* Scraped dynamic websites where content loads after page render
* Used Selenium to interact with the browser
* Handled delays and animations to ensure data availability

**Example platforms:**

* Welcome to the Jungle
* Quotes to Scrape

**Key concepts learned:**

* Selenium automation
* Explicit waits
* Handling animations & slow-loading elements

---

### 3️⃣ Pagination & Infinite Scroll Handling

* Implemented logic to scrape multiple pages of data
* Handled **infinite scroll** by programmatically scrolling until no new data loads
* Added safeguards to prevent duplicate scraping or infinite loops

**Key concepts learned:**

* Scroll height detection
* Page state validation
* End-of-content checks

---

## ⚙️ Features

* Modular and readable Python scripts
* Handles:

  * Pagination
  * Infinite scroll
  * Dynamic content loading
  * Slow websites
* Clean data output using pandas
* Beginner-friendly but real-world oriented implementation

---

## ▶️ How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/saifu8nnn/python-web-scraping.git
cd python-web-scraping
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run a scraper script

```bash
python scraper.py
```

> Make sure you have **ChromeDriver** installed and added to your system PATH.

---

## 📊 Output

* Extracted data is saved in:

  * CSV format
  * Structured tabular form using pandas
* Easily extendable for databases or APIs

---

## 🎯 Learning Outcomes

Through this project, I gained hands-on experience in:

* Web data extraction fundamentals
* Working with both static and dynamic websites
* Handling real-world scraping challenges like infinite scroll and animations
* Writing maintainable and reusable scraping scripts

---

## ⚠️ Ethical & Legal Notice

These projects are created **strictly for educational purposes**.
Web scraping should always respect:

* Website terms of service
* Robots.txt rules
* Legal and ethical boundaries

---

## 📬 Contact

If you’re interested in collaboration, feedback, or data-related opportunities:

* **GitHub:** [https://github.com/saifu8nnn]
* **LinkedIn:** [www.linkedin.com/in/saifu8n]