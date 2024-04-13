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


![G2 Extension](https://github.com/Akatsuki49/deadlineDashers_Track3/assets/110471762/91d9a563-6873-4e7e-9e5d-c85c5e88a09d)

## How to Run

First you need to start a CORS server (We have used ngrok for that)

Open Command Prompt and run

```bash
ngrok http --host-header=rewrite 5000
```

Now, check the Forwarding Session Status and copy the .app url. This will be your `<your_ngrok_url>`

**Clone the GitHub Repository**

Open `manifest.json` and replace the existing value of `permissions` with `[<your_ngrok_url>/summarize]`

Also, replace the existing value of `content_security_policy` after `'self'` with `<your_ngrok_url>/summarize`

Now, Open `popup.js` and after `fetch` inside paranthesis, replace the existing url with `<your_ngrok_url>/summarize`

**Chrome extension settings > Toggle the Developer Mode > Load unpacked > Add the `deadlineDashers_Track3` (which is the clone GitHub Repository)**

If the steps are correctly followed, you should be able to see the **G2 logo** in your extensions bar.

```bash
cd G2_Backend
python app.py
```

Don't forget to add your own `.env` with **OpenAI API key** and the **secret token** in the `backend` folder.

If the `server.py` runs fine, you should be able to see `Running on http://127.0.0.1:5000` in the terminal.

Note: When testing our app we noticed that the scrapy module threw some unexpected exceptions in some machines. 
If you encounter any such error: please restart the server i.e the flask app

## Output
  1
  
  ![https://www.telesign.com/products/trust-engine](https://github.com/Akatsuki49/deadlineDashers_Track3/assets/95576716/d6de544a-b887-47aa-9584-852bbf108ddf)

  Our digital identity solutions utilize a fast, accurate trust engine to engage customers through secure channels and prevent fraud attacks. With our digital trust anchor and       
  consortium, we validate customers and ensure account integrity, providing a seamless and trustworthy experience for all transactions.

  2
  
  ![https://www.litzia.com/professional-it-services/](https://github.com/Akatsuki49/deadlineDashers_Track3/assets/95576716/77898c0b-165a-41b4-a178-82303e985c0e)
  
  Litzias VCIO services offer a preventative approach to network management, with a dedicated tech support staff and a variety of network installation and maintenance options. Our 
  virtual chief information officer services fulfill the role of a liaison with technology vendors, providing proactive monitoring and successful technology choices for your 
  business's specific requirements.

  3   
  
  ![https://www.chattechnologies.com/](https://github.com/Akatsuki49/deadlineDashers_Track3/assets/95576716/ba12c059-ac87-4c55-b121-7452122917f3)
  
  Revolutionize your recruiting process with our advanced collaboration platform, designed to supercharge your communications and streamline interactions between hiring managers and 
  candidates. Our cutting-edge technology liberates customers and candidates alike, providing real-time communication and transparency for seamless recruitment velocity.

  4
  
  ![https://inita.com/](https://github.com/Akatsuki49/deadlineDashers_Track3/assets/95576716/1d185edb-50df-41e7-9e00-e20e379382aa)
  
  Initas is a leading AI-powered marketing tool that streamlines content creation for small businesses. With our ready-to-use website and appointment payment systems, businesses can 
  easily generate engaging social media posts and online content in a matter of seconds, eliminating the need for constant manual input. Our AI model takes care of the basics, 
  allowing businesses to focus on their campaign goals and target audience.

  5 
  
  ![https://aim-agency.com/](https://github.com/Akatsuki49/deadlineDashers_Track3/assets/95576716/33445803-cf51-41ea-8eda-1eab28a66a15)
  
  Welcome to our boutique agency, where we provide bespoke PR services to our clients. With a strategic approach and creative problem-solving, we have built a reputation for 
  delivering exceptional results for senior executives, founders, and high-net-worth individuals. Our team of professionals has a proven track record of success, as showcased in our 
  case studies and client testimonials. Let us help you elevate your brand and reach



  ## Summary of Main Novelties

- **Full Stack Project:** We've developed a comprehensive solution comprising frontend (HTML, CSS, JS) and backend (Python, Flask, Scrapy, KeyBERT, GPT, NLTK), along with a proxy server (ngrok).

- **Scraping Capabilities:** Leveraging Python Scrapy as our primary scraper, we extract information from various URLs, including relevant pages such as "About Us".

- **Tokenization Techniques:** Employing techniques like **stop word removal**, **sentence, and word tokenization**, as well as **KeyBERT** for keyword extraction from text, to streamline input tokenization.

- **Summarization Process:** Utilizing **GPT 3.5 turbo**, we query a language model to summarize the final content based on our structured input prompt. We also tried a mixture of experts model called **Mistral 7B**

- **Prompt Engineered Output:** Our final output is engineered based on the input prompt provided to the model, defining the structure of the prompt for generating the summary.

