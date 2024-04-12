# G2 Hackathon

## Problem Statement

G2 regularly updates its website with new products by creating new categories and refining existing ones. One crucial aspect of this process is ensuring that each product has a precise description and URL before it is added to the site. We are interested in automating the process of updating product descriptions in our database. We will provide you with a few product URLs, and your output will be a brief 3-4 lines description of each product.

## Proposed Solution

We built an end-to-end solution that encompasses a G2-themed extension where the user can enter the URL and, in turn, get a product summary.

The high-level approach involves:

1. The user enters a product URL in the G2 extension.
2. The extension sends a POST request to the backend server with the provided URL.
3. The backend server uses a web scraper (Scrapy) to extract the relevant product information from the given URL.
4. The extracted data is then cleaned and processed to generate a concise 3-4 line product summary.
5. The generated summary is returned to the extension and displayed to the user.

## How to Run

**Chrome extension settings > Toggle the Developer Mode > Load unpacked > Add the `dist` folder of this project**

If the steps are correctly followed, you should be able to see the **G2 logo** in your extensions bar.

![G2 Extension](https://github.com/Akatsuki49/deadlineDashers_Track3/assets/110471762/91d9a563-6873-4e7e-9e5d-c85c5e88a09d)

To run the server:

```bash
cd G2_Backend
python app.py
```

Don't forget to add your own `.env` with **OpenAI API key** and the **secret token** in the `backend` folder.

If the `server.py` runs fine, you should be able to see `Running on http://127.0.0.1:5000` in the terminal.

## Output

[Attach screenshot of the output]
