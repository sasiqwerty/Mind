---
aliases: 
tags: 
date created: Wednesday, August 16th 2023, 2:17:44 pm
date modified: Wednesday, August 16th 2023, 2:18:49 pm
---

## Mind Mapping with AI: An Accessible Approach for Neurodiverse Learners

[Mind Mapping with AI: An Accessible Approach for Neurodiverse Learners | by Elle Neal | Medium](https://medium.com/@elle.neal_71064/mind-mapping-with-ai-an-accessible-approach-for-neurodiverse-learners-1a74767359ff)  
Learn how to build your own AI generated mind map to support neurodiverse readers and learners.

![](https://miro.medium.com/v2/resize:fit:700/1*JtRDhbO6ObGI6u-SXzufvQ.png)

Generated using VisualLearner Mermaid AI: [NIMH » Attention-Deficit/Hyperactivity Disorder in Adults: What You Need to Know (nih.gov)](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know)

In this article, I will introduce [VisuaLearner Mermaid AI](https://databutton.com/v/jk9vrghc), a visual aid application built and deployed using Databutton using Cohere and OpenAI technology. I’ll **provide you with the code snippets and explanations** to help you follow along and build your own Mermaid AI application.

### **VisualLearner: User Journey**

![](https://miro.medium.com/v2/resize:fit:700/1*drjt-xWaP5gDXqQ7clYazw.png)

Generated using AI and Mermaid.js

## Introduction

Hello, readers! This blog post is a journey of discovery and innovation that began during my AI and Data Science apprenticeship. This was when I found out that I had [ADHD (Attention-Deficit/Hyperactivity Disorder)](https://www.adhdcentre.co.uk/adult-adhd-what-is-it-exactly/), a revelation that brought both understanding and relief. It wasn’t a setback but an opportunity for me to understand my unique learning needs and use them as a stepping stone towards finding effective solutions.

One such solution I found was visualization, particularly through mind maps and flowcharts. This visual approach to learning was a game-changer for me and countless others, as research shows that around 65% of people are visual learners​[1](https://www.edapp.com/blog/visual-learning-statistics/)​​[2](https://www.edapp.com/blog/visual-learning-statistics/)​​[3](https://www.edapp.com/blog/visual-learning-statistics/)​. Armed with this knowledge, I set out to build a tool that combines these visual aids with AI to enhance the learning process.

> This visual approach to learning was a game-changer for me and countless others, as research shows that around 65% of people are visual learners.

### The Journey

During my apprenticeship, I faced challenges such as maintaining focus on video calls, journaling activities, and reading research papers. I felt overwhelmed and began questioning my abilities. However, after learning that these struggles were symptoms of ADHD, a condition that affects over six million children and a significant number of adults in the U.S​[4](https://www.statista.com/topics/5079/attention-deficit-hyperactivity-disorder-adhd-in-the-us/)​​[5](https://www.statista.com/topics/5079/attention-deficit-hyperactivity-disorder-adhd-in-the-us/)​, I realized my brain simply processed information differently. It wasn’t that I couldn’t learn; I just needed to approach learning differently.

### The Solution

I started utilizing a large whiteboard in my workspace, where I could create mind maps and flowcharts to break down complex information into visually digestible chunks. This was particularly beneficial as ADHD has been linked to alterations in visual perception​[6](https://pubmed.ncbi.nlm.nih.gov/31479020/)​​[7](https://pubmed.ncbi.nlm.nih.gov/31479020/)​​[8](https://pubmed.ncbi.nlm.nih.gov/31479020/)​. Through these visual aids, I was able to understand and retain information more effectively, share my work with others, and create a reference for my learning journey.

### The Idea

Inspired by my own experience, I realized that AI language models could understand complex information and generate code. I wondered: could I use AI to generate mind maps and flowcharts automatically? I was eager to find out.

### The Plan

In this blog post, I’m excited to introduce you to an application I’ve built that leverages the power of AI to distil large amounts of information into visual formats. Through demos and code snippets, I’ll walk you through how this app can support neurodiverse learners and enhance learning efficiency and effectiveness. This application is not just a product of my training in AI and Data Science, but also of my personal journey with ADHD. My hope is that this tool can help others who, like me, have unique learning needs and strengths.

Stay tuned to discover a different way of learning, one that celebrates neurodiversity and harnesses it to create something truly empowering.

Lets dive in!

### How to Build Your Application

This app was built and deployed using [Databutton](https://www.databutton.io/). Databutton is an AI-powered workspace designed to facilitate the creation and sharing of data apps. It allows users to build and distribute AI and data applications by leveraging the entire Python ecosystem directly from their browser. Its user-friendly design makes it easy to turn ideas into functional applications, making it an efficient tool for both beginners and professionals​​.

Databutton has been a helpful tool in managing my ADHD during application development:

1. **Structured Workflow:** Its organized user interface reduces distractions, enhancing focus.
2. **Speedy Prototyping:** Rapid deployment keeps momentum, reducing interest loss.
3. **Visual Interface:** Aids visual learners, common in ADHD, to grasp complex concepts.
4. **Accessible Learning**: Intuitive design and clear documentation simplify skill acquisition.
5. **Interactive Experience:** Engaging, hands-on approach enhances interest and motivation.
6. **Easy Collaboration:** Facilitates teamwork and feedback, alleviating feelings of isolation.

In essence, Databutton’s features address ADHD challenges, making app development more engaging and productive.

Within a few clicks, I was able to deploy my application to the world!

### Adding the Code

### 1. Import Necessary Modules:

The application starts by importing the necessary Python modules: `requests`, `BeautifulSoup`, `databutton`, `openai`, `cohere`, and `streamlit`.

import databutton as db  
import requests  
from bs4 import BeautifulSoup  
import openai  
import cohere  
import streamlit as st

### 2. Scrape Text from a Webpage:

The `scrape_text` function sends a GET request to a provided URL and retrieves the text content of the webpage using [BeautifulSoup](https://pypi.org/project/beautifulsoup4/). It returns the text if the GET request is successful, or a failure message otherwise.

def scrape_text(url):  

## Send a GET Request to the URL

    response = requests.get(url)  
  
    # If the GET request is successful, the status code will be 200  
    if response.status_code == 200:  
        # Get the content of the response  
        page_content = response.content  
  
        # Create a BeautifulSoup object and specify the parser  
        soup = BeautifulSoup(page_content, "html.parser")  
  
        # Get the text of the soup object  
        text = soup.get_text()  
  
        # Return the text  
        return text  
    else:  
        return "Failed to scrape the website"

### 3. Create Mermaid.js Chart:

The `mermaid_chart` function generates the HTML for the [Mermaid.js](https://mermaid.js.org/intro/) diagram. This function takes the Mermaid.js code (representing the mindmap) as an input and returns the HTML code that can be used to display the mindmap.

def mermaid_chart(mindmap_code):  
    html_code = f"""  
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">  
    <div class="mermaid">{mindmap_code}</div>  
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>  
    <script>mermaid.initialize({{startOnLoad:true}});</script>  
    """  
    return html_code

_Example Mermaid.js code_

> Mermaid is a JavaScript based diagramming and charting tool that uses Markdown-inspired text definitions and a renderer to create and modify complex diagrams. The main purpose of Mermaid is to help documentation catch up with development.

mindmap  
  root(Cofinder)  
    (Introduction)  
      ::icon(fa fa-info-circle)  
      (Designed to help the Cohere Community find relevant content)  
      (Users can ask natural language questions)  
      (Semantic search tool that brings together information from multiple sources)  
    (Repository Contents)  
      ::icon(fa fa-folder-open)  
      (cohere_text_preprocessing.csv)  
      (preprocessing.ipynb)  
      (main.py)  
      (cohere_text_final.csv)  
      (search_index.ann)  
    (Five Steps to Building the Application)  
      ::icon(fa fa-list-ol)  
      (Data Sources)  
        (Pre-processing the article text into chunks)  
      (Embeddings & Search Index)  
        (Use co.embed to obtain a vector representation of data)  
        (Store embeddings in a vector database)  
      (Front End)  
        (Streamlit for user interaction)  
      (Search)  
        (Use co.embed to get vector representation of user query)  
        (Use nearest neighbours to return relevant content)  
      (Answer)  
        (Use co.generate to answer the query given the context from the search results and the question)  
    (Streamlit Application)  
      ::icon(fa fa-desktop)  
      (Load libraries, data and search index)  
      (Add functions to generate embeddings to search the Annoy index for the user’s query)  
      (Generate an answer from the context)  
      (Add Streamlit search input and button to run functions)

### 4. Set up OpenAI API:

The application then sets up the OpenAI API by specifying the API type, base URL, version, and key.

def run_models(input_text):  

## Note: Content is Hidden due to Length of Text, You Can Add User and Assistant Roles

    response = openai.ChatCompletion.create(  
        engine="GPT35turbo",  
        messages=[  
            {  
                "role": "system",  
                "content": "You are generating a mindmap for someone who has ADHD...",  
            },  
            {"role": "user", "content": input_text},  
        ],  
        temperature=0.2,  
        max_tokens=400,  
        top_p=0.95,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=None,  
    )  
  
    return response

### 5. Run GPT-3 Model:

The `run_models` function creates a completion using OpenAI's GPT-3 model. It takes the scraped text as input and generates a mindmap in the form of Mermaid.js code.

### 6. Summarize Text:

The `summarise` function uses the [Cohere summarise API](https://docs.cohere.com/reference/summarize-2) to generate a summary of the input text. Here's the code for this function:

def summarise(input_text):  
    co = cohere.Client(  
        db.secrets.get("COHERE_API_KEY")  
    )  
    response = co.summarize(  
        text=input_text,  
        length="long",  
        format="paragraph",  
        model="summarize-xlarge",  
        additional_command="What are th

### 7. Build UI with Databutton:

The application uses Databutton to create the user interface (UI) where the user can input a URL. The application then scrapes the text from the webpage at that URL, generates a summary, generates Mermaid.js code for a mindmap, and displays the mindmap.

import databutton as db  
import streamlit as st  
from streamlit.components.v1 import html  
from utils import scrape_text, mermaid_chart, run_models, summarise  
  

## UI

st.title("AI Generated Mermaid.js Mindmap")  
  

## Creating a Form for both Caching and Clean Input Box on Run

form = st.form("Form to run", clear_on_submit=True)  
  
url = form.text_input("Enter your URL below:", placeholder="Paste any URL of your choice")  
  
if form.form_submit_button("Generate Mermaid Mindmap Visual"):  
    text = scrape_text(url)  
    input_text = "Generate a Mermaid.js mindmap only using the text below:\n" + text  
    with st.expander("See full article"):  
        st.write(text)  
    with st.spinner("Generating Cohere AI Summary "):  
        summary = summarise(text)  
        st.write("### Cohere AI Generated Summary")  
        st.write(summary)  
  
    with st.spinner("Generating Mermaid Code"):  
        out = run_models(input_text)  
  
    mindmap_code = out["choices"][0]["message"]["content"][10:-3]  
    with st.expander("See OpenAI Generated Mermaid Code"):  
        st.code(mindmap_code)  
  
    # Use the html function to display the Mermaid.js diagram  
    html(mermaid_chart(mindmap_code), width=1500, height=1500)

### 8. User Input:

The user enters a URL in the form provided in the Streamlit UI. Once the URL is submitted, the application scrapes the text from the webpage, generates a summary using Cohere API, and generates a Mermaid.js mindmap using OpenAI’s GPT-3 model. The summary and the mindmap are then displayed in the UI.

## Conclusion

In conclusion, leveraging AI-generated mind maps and visual aids through VisuaLearner Mermaid AI and Databutton offers an accessible approach to support neurodiverse readers and learners.

By scraping text from websites, generating summaries, and creating mind maps, individuals with ADHD and other neurodiverse conditions can enhance their learning experience. This combination of AI and visual tools helps overcome feelings of overwhelm and promotes better understanding.

The goal is to celebrate neurodiversity, raise awareness of ADHD, and provide inclusive learning solutions. Expanding the application to incorporate various text sources and visualizations will further enrich the learning process for neurodiverse individuals, making learning more engaging and effective.

Embracing technology and empathy enables the creation of an inclusive learning environment for individuals with diverse learning needs.

Please let me know if you found this useful or would like to talk more about the development of the application to support either yourself or others and connect with me on [LinkedIn](https://www.linkedin.com/in/elle-neal-78994617/).