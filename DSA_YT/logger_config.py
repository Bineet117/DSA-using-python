import logging

# Configure logging once here
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Export a logger
logger = logging.getLogger("my_app")


# Configure logging
# logging.basicConfig(
#     filename="app.log",  # log file name
#     level=logging.DEBUG,  # log all levels (DEBUG and above)
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# logging.debug("This is a debug message")     # For detailed info (developer use)
# logging.info("This is an info message")      # For general info
# logging.warning("This is a warning message") # For warnings
# logging.error("This is an error message")    # For errors
# logging.critical("This is a critical message") # For severe errors