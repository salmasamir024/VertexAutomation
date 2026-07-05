import pandas as pd


def read_excel(excel_path):

    if excel_path.name.startswith("~$"):
        raise Exception(
            "Excel file is currently open. Please close it first."
        )

    print("\n")
    print("=" * 50)
    print("Reading Excel...")
    print("=" * 50)

    df = pd.read_excel(excel_path, header=None)

    print(f"Rows    : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    return df