import pandas as pd

df = pd.read_csv(
    "/home/scrad/Documents/globalterrorismdb_0718dist.csv",
    encoding="ISO-8859-1",
    low_memory=False
)

operation_type = input("Enter the type of operation to be performed (filter/groupby/mutation/join): ")

if operation_type == "filter":
    country = "United States"
    df = df[df.country_txt == country]
    df.to_csv("/home/scrad/Documents/rust_test/python_output_filtered.csv")
    print("Filtered data saved to python_output_filtered.csv file.")

elif operation_type == "groupby":
    df = df.groupby(by="country_txt", as_index=False).agg(
        {"nkill": "sum", "individual": "mean", "eventid": "count"}
    )
    df.to_csv("/home/scrad/Documents/rust_test/python_output_groupby.csv")
    print("Grouped data saved to python_output_groupby.csv file.")

elif operation_type == "mutation":
    df["computed_file"] = df["nkill"].map(lambda x: (x - 10) / 2 + x ** 2 / 3)
    df.to_csv("/home/scrad/Documents/rust_test/output_python_mutation.csv")
    print("Mutated data saved to output_python_mutation.csv file.")

elif operation_type == "join":
    df_country = pd.read_csv(
        "/home/scrad/Documents/WDICountry.csv"
    )

    df_merge = pd.merge(
        df, df_country, left_on="country_txt", right_on="Short Name"
    )
    df_merge.to_csv("/home/scrad/Documents/rust_test/python_output_merge.csv")
    print("Merged data saved to python_output_merge.csv file.")

else:
    print("Invalid operation type entered.")
