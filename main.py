# Imports
from dotenv import load_dotenv
import os
import src.download_ofp as gsb

#Loading env file
load_dotenv()


def main():
    user_id = os.getenv("SIMBRIEF_ID")
    gsb.downlaod_ofp(user_id)

main()