"""Module for checking whether psycopg2 are installed or not."""
import logging
import os
import psycopg2 as pg


def lambda_handler(event, _context):
    """Main lambda handler for testing psycopg2 library."""
    
    print("psycopg2 ARE INSTALLED SUCCESSFULLY !")