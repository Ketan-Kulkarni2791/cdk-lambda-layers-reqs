"""Module for checking whether pandas are installed or not."""
import logging
import os
import pandas as pd


def lambda_handler(event, _context):
    """Main lambda handler for testing pandas library."""
    
    print("PANDAS ARE INSTALLED SUCCESSFULLY !")