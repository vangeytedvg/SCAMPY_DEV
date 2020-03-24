import logging

# Create a custom logger
logger = logging.getLogger("dannys-log")

# Create handlers
f_handler = logging.FileHandler('file.log')

# Create formatters and add it to handlers
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(f_handler)

