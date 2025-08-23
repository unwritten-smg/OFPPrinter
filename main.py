# Imports
from dotenv import load_dotenv
import os
import src.download_ofp as gsb
import src.print_data as stp
import src.check_data_exists as check_data

#Loading env file
load_dotenv()

#Variables
user_id = os.getenv("simbrief_id")
file_path = os.getenv("file_path")


def main():
    #Check if folder data exists
    check_data
    #Download Simbrief OFP
    gsb.downlaod_ofp(user_id)
    
    #Print file
    stp.print_text_file(file_path)
    
    
    
    
main()