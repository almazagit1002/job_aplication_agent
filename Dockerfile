# Use the official Python image
FROM python:3.10-slim



# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .
COPY db/db_set_up.py ./db/
COPY db/models/ ./db/models/
COPY api/utils/users.py ./api/utils/
COPY api/users.py ./api/

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable
ENV MONGO_URL=mongodb://host.docker.internal:27017


# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
