import os
#import zipfile

DIR_DATA = "data"
DIR_DATA_PATH = os.path.join(os.getcwd(), DIR_DATA)
DIR_RAW = "raw"
DIR_RAW_PATH = os.path.join(os.getcwd(), DIR_DATA, DIR_RAW)
DIR_PROCESSED = "processed"
DIR_PROCESSED_PATH = os.path.join(os.getcwd(), DIR_DATA, DIR_PROCESSED)


def download_data() -> None:
    # Download dataset
    os.system(f'kaggle datasets download -d blastchar/telco-customer-churn -p "{DIR_RAW_PATH}" --unzip -o')

    for filename in os.listdir(DIR_RAW_PATH):
        if filename.lower().endswith("telco-customer-churn.csv"):
            os.rename(os.path.join(DIR_RAW_PATH, filename), os.path.join(DIR_RAW_PATH, "telco-customer-churn-dataset.csv"))
    # Unzip
    #with zipfile.ZipFile(os.path.join(DIR_RAW_PATH, "telco-customer-churn.zip"), "r") as zip_ref:
    #    zip_ref.extractall(DIR_RAW_PATH)

if __name__ == "__main__":
    #print(DIR_RAW_PATH)
    download_data()