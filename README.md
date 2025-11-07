## Kbeauty-ADK-Agent-using-MCP-and-deploying-on-Vertex-Engine


## Setup and Installation

Detailed steps to get the project up and running.
### Local Environment Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-project.git
    cd your-project
    ```
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

5.  **Setting up for deployment**
  **Create a Cloud Storage Bucket:**
    This bucket will be used for storing data, model artifacts, and pipeline outputs.
    ```bash
    gcloud storage buckets create gs://YOUR_BUCKET_NAME \
                              --project=YOUR_PROJECT_ID \
                              --location=YOUR_PROJECT_REGION
    ```
    (Replace `YOUR_BUCKET_NAME` with a unique bucket name.)

6. **Deploy the agent**
   adk deploy agent_engine \
    --project=YOUR_PROJECT_ID \
    --region=YOUR_PROJECT_REGION \
    --display_name "Doc Fact Checker" \
    --staging_bucket gs://YOUR_BUCKET_NAME \
    --requirements_file requirements.txt \
    docfactcheckeragent/
    



-   

