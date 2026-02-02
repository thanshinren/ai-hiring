import logging

logging.basicConfig(
    filename="logs/ai_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



from utils.logger import logger

def parse_resume(text):
    logger.info("Parsing resume")
    return {"skills": ["Python", "ML"], "experience": 2}

