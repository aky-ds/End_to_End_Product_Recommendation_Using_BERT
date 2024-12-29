import os
from pathlib import Path

list_of_files=[
    'requirements.txt',
    'setup.py',
    'src/components/data_ingest.py',
    'src/components/data_preprocessor.py',
    'src/components/model_training.py',
    'src/components/__init__.py',
    'src/__init__.py',
    'src/piplelines/training_pipeline.py',
    'src/piplelines/predictions_pipeline.py',
    'src/piplelines/__init__.py',
    'src/exception.py',
    'src/logger.py',
    'artifacts/data.py',
    'Prediction.py',
    'Model_loader.py',  
    'templates/index.html',
    'experiments/experiment.ipynb',
]

for file in list_of_files:
    file_path=Path(file)
    file_dir,file_name=os.path.split(file_path)
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
    
    if not os.path.exists(file_path):
        with open(file_path,'w') as f:
            pass
