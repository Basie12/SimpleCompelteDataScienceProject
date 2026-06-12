from dataclasses import dataclass
from pathlib import Path
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    ingested_train_dir: Path
    ingested_test_dir: Path
