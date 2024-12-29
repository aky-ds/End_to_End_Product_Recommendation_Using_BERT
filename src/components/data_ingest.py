import os
import sys
from pathlib import Path
from abc import ABC,abstractmethod
import zipfile
from src.exception import CustomException
from src.logger import logging
import pandas as pd

class ZipDataIngester(ABC):
    """
    Abstract base class for ingesting data from a ZIP file.
    """
    @abstractmethod
    def ingest(self,data:str)->pd.DataFrame:
        """ An abstract base class for ingesting data 

        Args:
            data (str): a zip file containing the data to be ingested

        Returns:
            pd.DataFrame: returns a DataFrame
        """
        pass

class CsvZipDataIngester(ZipDataIngester):
    """
    Ingests data from a CSV file in a ZIP file.
    """
    def ingest(self, data: str)->pd.DataFrame:
        
        """ A method to ingest data from a CSV file

        Args:
            data (str): a zip file containing the data to be ingested

        Returns:
            pd.DataFrame: returns a DataFrame
        """
        logging.info("Ingesting data from CSV file in ZIP")
        try:
            if not data.endswith(".csv"):
                raise CustomException(e)
            logging.info("Extracting data from CSV file")
            with zipfile.ZipFile(data,'r') as zip_ref:
                zip_ref.extractall('artifacts')
                
            extracted_path=os.listdir('artifacts')
            logging.info("Locating the csv files")
            
            extracted_csvs = [path for path in extracted_path if path.endswith('.csv')]
            
            if len(extracted_csvs) > 0:
                raise ('Multiple csv files found')
            if len(extracted_csvs) == 0:
                
                raise ('No csv file found')
            csv_path = extracted_csvs[0]
            logging.info("Reading csv file")
            df=pd.read_csv(os.path.join('artifacts',csv_path))
            return df
        except Exception as e:
            raise CustomException(e)


if __name__ == '__main__':
    csv_ingest=CsvZipDataIngester()
    df=csv_ingest.ingest('artifacts/data')