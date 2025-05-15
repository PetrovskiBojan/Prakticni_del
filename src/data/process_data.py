import pandas as pd
import os

csv_df = pd.read_csv("../../data/raw/students_scores.csv")
xlsx_df = pd.read_excel("../../data/raw/students.xlsx", engine="xlrd")

df = pd.concat([csv_df, xlsx_df], axis=1)

if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])
df["MIN_subject"] = df[["STEM_subjects", "H_subjects"]].min(axis=1)

output_path = "../../data/processed/current_data.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

df.to_csv(output_path, index=False)