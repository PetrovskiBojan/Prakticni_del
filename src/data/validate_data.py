import great_expectations as ge
import pandas as pd
import sys

def validate(reference_path, current_path, report_path):
    df = pd.read_csv(reference_path)
    context = ge.get_context()
    ref_df = ge.dataset.PandasDataset(df)
    suite_name = "reference_suite"

    try:
        suite = context.get_expectation_suite(suite_name)
    except Exception:
        suite = context.create_expectation_suite(suite_name)

    batch = ge.dataset.PandasDataset(ref_df)
    batch.expect_column_to_exist("STEM_subjects")
    batch.expect_column_to_exist("H_subjects")

    context.save_expectation_suite(batch.get_expectation_suite(), suite_name)

    current_df = ge.read_csv(current_path)
    batch_to_validate = ge.dataset.PandasDataset(current_df, expectation_suite=suite)
    results = batch_to_validate.validate()

    with open(report_path, "w") as f:
        f.write(results.to_json_dict().__str__())

    print(results)

if __name__ == "__main__":
    validate(sys.argv[1], sys.argv[2], sys.argv[3])
