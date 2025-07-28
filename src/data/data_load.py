import os
import zipfile
from pandas import read_csv, DataFrame

def load_data():
    return read_csv("../../data/raw/Telco-Customer-Churn.csv")

def download_data() -> None:
    # Download dataset
    os.system("kaggle datasets download -d blastchar/telco-customer-churn -p ../../data/raw")

    # Unzip
    with zipfile.ZipFile('../../data/raw/telco-customer-churn.zip', 'r') as zip_ref:
        zip_ref.extractall('../../data/raw')
        
def check_data() -> bool:
    """
    Check if the dataset zip file exists in the raw data folder.

    This function checks for the presence of the 'telco-customer-churn.zip' file
    in the specified directory to determine if the dataset has been downloaded.

    Returns
    -------
    bool
        True if the zip file exists, False otherwise.
    """

    if os.path.exists('../../data/raw/telco-customer-churn.zip'):
        return True
    else:
        #print("Data not found. Run download_data() first or download it from https://www.kaggle.com/datasets/blastchar/telco-customer-churn.")
        return False
    
def load_data() -> DataFrame:
    """
    Load the Telco Customer Churn dataset from a CSV file.

    Returns:
        DataFrame: The dataset loaded into a pandas DataFrame.

    If the dataset file is not present, it will be downloaded first.
    """

    if check_data():
        return read_csv('../../data/raw/Telco-Customer-Churn.csv')
    else:
        print("Data not found. Downloading it...")
        download_data()
        return read_csv('../../data/raw/Telco-Customer-Churn.csv')
    
def save_data(df: DataFrame) -> None:
    """
    Save the dataframe to a CSV file in the raw data folder.

    This function will overwrite any existing file with the same name.

    Parameters
    ----------
    df : DataFrame
        The DataFrame to save to a CSV file.

    Returns
    -------
    None
    """
    
    df.to_csv('../../data/raw/Telco-Customer-Churn.csv', index=False)