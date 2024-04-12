## Summary of Main Novelties

- **Full Stack Project:** We've developed a comprehensive solution comprising frontend (HTML, CSS, JS) and backend (Python, Flask, Scrapy, KeyBERT, GPT, NLTK), along with a proxy server (ngrok).

- **Scraping Capabilities:** Leveraging Python Scrapy as our primary scraper, we extract information from various URLs, including relevant pages such as "About Us".

- **Tokenization Techniques:** Employing techniques like **stop word removal**, **sentence, and word tokenization**, as well as **KeyBERT** for keyword extraction from text, to streamline input tokenization.

- **Summarization Process:** Utilizing **GPT 3.5 turbo**, we query a language model to summarize the final content based on our structured input prompt. We also tried a mixture of experts model called **Mistral 7B**

- **Prompt Engineered Output:** Our final output is engineered based on the input prompt provided to the model, defining the structure of the prompt for generating the summary.
