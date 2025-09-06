import logging


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  
    format="%(asctime)s - %(levelname)s - %(message)s"
)

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


logging.debug("First way of doing it")
a = 3456789
for i in str(a):
    print(i)

logging.info("second way of doing it by convertint to string and reversing it")
a = 3456789
for i in str(a)[::-1]:
    print(i)

logging.debug("Second way of doing it")
a = 3456789
while a > 0:
    print(a%10)
    a = a//10

