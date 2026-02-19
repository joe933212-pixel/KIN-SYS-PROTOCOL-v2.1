# Deployment Instructions for KIN-SYS-PROTOCOL

## Prerequisites
- An account with Render.
- A PostgreSQL database instance.
- Gunicorn installed.

## Step-by-Step Deployment Instructions

### 1. Set Up PostgreSQL Database
1. Log in to your Render account.
2. Create a new PostgreSQL database instance:
   - Go to the Databases section and select "Create Database".
   - Choose the plan that suits your needs.
   - Note the connection URL and credentials (username, password, database name).

### 2. Configure Environment Variables
In your Render service settings, set the following environment variables:

- `DATABASE_URL`: The connection string for your PostgreSQL database.
- `SECRET_KEY`: A secret key for your application.
- `DEBUG`: Set to `False` for production.
- `POLYGON_TESTNET_URL`: The URL for Polygon testnet (if applicable).
- `POLYGON_MAINNET_URL`: The URL for Polygon mainnet (if applicable).

### 3. Prepare Your Application
- Ensure your application is configured to use the provided environment variables.
- Requirements for Gunicorn and any other dependencies should be listed in your `requirements.txt`.

### 4. Deploy to Render
1. Go to the Services section in your Render account.
2. Create a new service and select "Web Service".
3. Connect to your GitHub repository (`joe933212-pixel/KIN-SYS-PROTOCOL-v2.1`).
4. Choose the branch you wish to deploy from (e.g., `main`).
5. Configure the build command and start command:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Finally, click on "Create Web Service" to start the deployment.

### 5. Verify Deployment
- Once deployed, visit the assigned URL to verify that your application is running as expected.
- Check the logs in Render for any errors or issues.
