# Imports
from dotenv import load_dotenv
import os
import src.download_ofp as gsb
import src.print_data as stp

#Loading env file
load_dotenv()

#Variables
user_id = os.getenv("SIMBRIEF_ID")
file_path = "data\placeholder.txt"



def main():
    #Download Simbrief OFP
    gsb.downlaod_ofp(user_id)
    
    #Print file
    stp.print_text_file(file_path)
    
    
    
    
main()