# Configuration settings for the project
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data directories
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
MODEL_DIR = os.path.join(BASE_DIR, 'models')

# Create directories if they don't exist
for directory in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, MODEL_DIR]:
    os.makedirs(directory, exist_ok=True)

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'database': 'finance_analytics',
    'user': 'your_username',
    'password': 'your_password'
}

# Model parameters
MODEL_PARAMS = {
    'kmeans': {
        'n_clusters': 5,
        'random_state': 42
    },
    'random_forest': {
        'n_estimators': 100,
        'random_state': 42
    }
}

# Reporting configuration
REPORT_CONFIG = {
    'output_dir': os.path.join(BASE_DIR, 'reports'),
    'template_dir': os.path.join(BASE_DIR, 'templates')
} 