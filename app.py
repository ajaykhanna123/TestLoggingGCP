import logging
from flask import Flask, jsonify

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()  # Log to the console
    ]
)

# Create a logger
logger = logging.getLogger("app_logger")

# Flask app for demonstration
app = Flask(__name__)

@app.route("/")
def home():
    logger.info("Home endpoint was accessed.")
    return jsonify({"message": "Welcome to the Logging Demo App!"})

@app.route("/process")
def process():
    logger.debug("Processing started.")
    try:
        # Simulate a process
        result = {"status": "success", "data": "Processed successfully"}
        logger.info("Processing completed successfully.")
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error occurred during processing: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/error")
def error():
    logger.warning("This endpoint is designed to raise an error.")
    try:
        raise ValueError("This is a simulated error!")
    except ValueError as e:
        logger.error(f"Simulated error occurred: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    logger.info("Starting the application.")
    app.run(host="0.0.0.0", port=5000)  # Run the Flask app
