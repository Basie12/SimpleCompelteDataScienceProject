import os
import zipfile
import urllib.request

from src.simple_mlops import logger
from src.simple_mlops.entity.config_entity import DataIngestionConfig
## data ingestion component
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    #download data from source url to local data file
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            print(f"Downloading from {self.config.source_URL} -> {self.config.local_data_file}")
            filename, headers = urllib.request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(f"Downloaded {filename} with headers:\n{headers}")
        else:
            logger.info(f"File already exists at {self.config.local_data_file}")
    #unzip data from local data file to unzip dir
    def unzip_data(self):
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)