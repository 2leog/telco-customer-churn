import os
from pandas import DataFrame, read_csv

DIR_DATA = "data"
DIR_DATA_PATH = os.path.join(os.getcwd(), DIR_DATA)
DIR_RAW = "raw"
DIR_RAW_PATH = os.path.join(os.getcwd(), DIR_DATA, DIR_RAW)
DIR_PROCESSED = "processed"
DIR_PROCESSED_PATH = os.path.join(os.getcwd(), DIR_DATA, DIR_PROCESSED)
DATASET_NAME_NEW = 'telco-customer-churn-dataset.csv'

def mk_data_dirs() -> None:

    if not os.path.exists(DIR_DATA_PATH):

        print(f"Nor the {DIR_DATA} directory nor it's subdirectories, {DIR_RAW} and {DIR_PROCESSED}, exists.")
        print(f"Creating the directories: {DIR_DATA}, {DIR_RAW}, {DIR_PROCESSED}...")

        os.mkdir(path=DIR_DATA_PATH)
        os.mkdir(path=DIR_RAW_PATH)
        os.mkdir(path=DIR_PROCESSED_PATH)

        print(f"The {DIR_DATA} directory and it's subdirectories, {DIR_RAW} and {DIR_PROCESSED}, were created.")

    elif not os.path.exists(DIR_RAW_PATH) and not os.path.exists(DIR_PROCESSED_PATH):

        print(f"Nor {DIR_RAW} and {DIR_PROCESSED} directories exists.")
        print(f"Creating {DIR_RAW} and {DIR_PROCESSED} directories...")

        os.mkdir(path=DIR_RAW_PATH)
        os.mkdir(path=DIR_PROCESSED_PATH)

        print(f"The {DIR_RAW} directory has been created.")

    elif os.path.exists(DIR_RAW_PATH) and not os.path.exists(DIR_PROCESSED_PATH):

        print(f"The {DIR_PROCESSED} directory doesn't exists.")
        print(f"Creating the {DIR_PROCESSED} directory...")

        os.mkdir(path=DIR_PROCESSED_PATH)

        print(f"The {DIR_PROCESSED} directory has been created.")

    elif not os.path.exists(DIR_RAW_PATH) and os.path.exists(DIR_PROCESSED_PATH):

        print(f"The {DIR_RAW} directory doesn't exists.")
        print(f"Creating the {DIR_RAW} directory...")

        os.mkdir(path=DIR_RAW_PATH)

        print(f"The {DIR_RAW} directory has been created.")

    else:

        print(f"The {DIR_DATA} directory and all it's subdirectories, {DIR_RAW} and {DIR_PROCESSED}, already exists.")

def download_data() -> None:
    # Download dataset
    os.system(f'kaggle datasets download -d blastchar/telco-customer-churn -p "{DIR_RAW_PATH}" --unzip -o')

def rename_data() -> None:

    for filename in os.listdir(DIR_RAW_PATH):
        if filename.lower().endswith("telco-customer-churn.csv"):
            os.rename(os.path.join(DIR_RAW_PATH, filename), os.path.join(DIR_RAW_PATH, DATASET_NAME_NEW))
        
def check_data_exists() -> bool:
    """
    Check if the dataset zip file exists in the raw data folder.

    This function checks for the presence of the 'telco-customer-churn.zip' file
    in the specified directory to determine if the dataset has been downloaded.

    Returns
    -------
    bool
        True if the zip file exists, False otherwise.
    """
    check = bool()
    for filename in os.listdir(DIR_RAW_PATH):
        if filename.endswith(".csv"):
            check = True
        else:
            #print("Data not found. Run download_data() first or download it from https://www.kaggle.com/datasets/blastchar/telco-customer-churn.")
            check = False
    
    return check
    
def load_data() -> DataFrame:
    """
    Load the Telco Customer Churn dataset from a CSV file.

    Returns:
        DataFrame: The dataset loaded into a pandas DataFrame.

    If the dataset file is not present, it will be downloaded first.
    """
    
    check = check_data_exists()
    if check:
        return read_csv(os.path.join(DIR_RAW_PATH, DATASET_NAME_NEW))
    else:
        print("Dataset not found.\nChecking if the data folders have already been created...")
        mk_data_dirs()
        print("Downloading dataset...")
        download_data()
        rename_data()
        return read_csv(os.path.join(DIR_RAW_PATH, DATASET_NAME_NEW))
    
def save_data(df: DataFrame, path: str, filename: str) -> None:
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
        
    df.to_csv(os.path.join(DIR_PROCESSED_PATH, filename), index=False)

if __name__ == "__main__":
    load_data()
