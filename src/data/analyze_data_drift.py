
import pandas as pd


def validate_data(data_path, reference_path):
    data = pd.read_csv(data_path)
    reference = pd.read_csv(reference_path)

    if len(data.columns) != len(reference.columns):
        print("Validation Error: Number of columns in data not same reference.")
        return False

    if not all(data.columns == reference.columns):
        print("Validation Error: Column names in data not same reference.")
        return False

    for column in data.columns:
        if data[column].dtype != reference[column].dtype:
            print(
                f"Validation Error: Data type of column '{column}' not same reference.")
            return False

    print("Validation successful: Data format matches reference.")
    return True


def main():
    data_path = "data/processed/current_data.csv"
    reference_path = "data/processed/reference_dataset.csv"

    validate_data(data_path, reference_path)


if __name__ == "__main__":
    main()