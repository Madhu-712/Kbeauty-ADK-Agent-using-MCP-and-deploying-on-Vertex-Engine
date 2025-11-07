## Kbeauty-ADK-Agent-using-MCP-and-deploying-on-Vertex-Engine
This project develops an ADK (Agent Development Kit) agent for the K-Beauty domain, utilizing Model context protocol (MCP) for custom processing and deploying on Google Cloud's Vertex AI.
## Introduction

The K-Beauty ADK Agent is designed to provide intelligent responses to user queries related to Korean beauty products, routines, and trends. By integrating custom processing capabilities via Model context Protocol(MCP), agent handles query execution effortlessly . The solution is built for scalability and reliability on Google Cloud's Vertex AI platform.

## Project Overview and structure

init.py-initialization of ADK Agent
agent.py-core logic
kbeautymcpserver.py-custom mcp integrations

This repository contains the necessary components to build, run, and deploy the K-Beauty ADK Agent. Key aspects include:

-   **MCP Toolset Integration:** Custom MCP integrations to process and understand K-Beauty-related queries.(kbeautymcpserver.py)
-   **ADK Agent Logic:** Core logic for interpreting user input and formulating relevant responses.(agent.py)
-   **Vertex AI Deployment:** Infrastructure for deploying the agent as a scalable service.

## Functional Overview

The `kbeautymcpserver.py` file outlines the core functionalities of the K-Beauty ADK Agent. The agent is designed to:

1.  **Receive User Queries:** Accept natural language queries related to K-Beauty.
2.  **Process with MCP:** Utilize custom MCP to analyze the query. This could involve:
    *   **Keyword Extraction:** Identifying product names, ingredients, skin concerns, or routine steps.
    *   **Sentiment Analysis:** Understanding the user's intent or tone.
    *   **Contextual Understanding:** Relating queries to previous interactions.It can even read base64 encoded images to get visual understanding and suggest customized korean beauty products.
    *   (Future: Image analysis if a visual query is provided, e.g., identifying a product from a photo).
3.  **Generate Responses:** Formulate informative and helpful answers based on the processed query. Responses can include:
    *   Product recommendations.
    *   Skincare routine advice.
    *   Ingredient explanations.
    *   Trend insights.
4.  **Manage State:** Maintain conversational context for a more fluid user experience.

## Setup and Installation

Detailed steps to get the project up and running.
### Local Environment Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    ```
2.  **Install dependencies**
  pip install -r requirements.txt

3.  **Run locally**
   python kbeautymcpserver.py

### Google Cloud Project Setup
### Authentication

Ensure your local environment can authenticate with Google Cloud.

-   **Using `gcloud` (recommended for local development):**
    ```bash
    gcloud auth application-default login
    ```
    This will open a browser for you to log in.

1.  **Select or Create a Project:**
    ```bash
    gcloud projects create YOUR_PROJECT_ID --name="Your Project Name"
    gcloud config set project YOUR_PROJECT_ID
    ```
    (Replace `YOUR_PROJECT_ID` with your desired project ID.)

2.  **Enable APIs:**
    ```bash
    gcloud services enable cloudresourcemanager.googleapis.com \
                       servicenetworking.googleapis.com \
                       aiplatform.googleapis.com \
                       discoveryengine.googleapis.com
  
                           # Add other necessary APIs
    ```
3.   **Install ADK kit:**
       mkdir k-beauty-mcp
       cd  k-beauty-mcp
       python -m venv .venv
       source .venv/bin/activate
       pip install google-adk
       adk create k-beauty-mcp

4. **Create a .env file:**
    GOOGLE_GENAI_USE_VERTEXAI=1
    GOOGLE_CLOUD_PROJECT=YOUR_GOOGLE_PROJECT_ID
    GOOGLE_CLOUD_LOCATION=YOUR_GOOGLE_PROJECT_REGION

5. **Interacting with the Agent**
   Once the server is running, you can interact with the agent by sending HTTP POST requests to its endpoint. You can use tools like curl or a simple Python script.
   Example Queries:
   Here are some example queries and how you might send them:
   Query about a product category:
   "query": "What are the best K-Beauty cleansers for oily skin?"

   Query about a specific ingredient:
   "query": "Tell me about Centella Asiatica in skincare.

   Query about a routine step:
   "query": "What is the 10-step K-Beauty routine?"

   Query about a brand with external context:
   "query": "Do you have information on the latest products from COSRX and their reviews?

   The agent will process these queries using its MCP-driven logic, potentially augmenting its understanding with external data, and return a relevant response.

6.  **Setting up for deployment**
  **Create a Cloud Storage Bucket:**
    This bucket will be used for storing data, model artifacts, and pipeline outputs.
    ```bash
    gcloud storage buckets create gs://YOUR_BUCKET_NAME \
                              --project=YOUR_PROJECT_ID \
                              --location=YOUR_PROJECT_REGION
    ```
    (Replace `YOUR_BUCKET_NAME` with a unique bucket name.)

7. **Deploy the agent**
   adk deploy agent_engine \
    --project=YOUR_PROJECT_ID \
    --region=YOUR_PROJECT_REGION \
    --display_name "Doc Fact Checker" \
    --staging_bucket gs://YOUR_BUCKET_NAME \
    --requirements_file requirements.txt \
    docfactcheckeragent/

8. **Contributing**
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature-name).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature/your-feature-name).
Open a Pull Request.

9.**License**
This project is licensed under the [Your Chosen License, e.g., MIT License] - see the LICENSE file for details.

   
    



-   

