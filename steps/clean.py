import numpy as np
from sklearn.impute import SimpleImputer


class Cleaner:
    def __init__(self):
        self.imputer = SimpleImputer(strategy="most_frequent", missing_values=np.nan)

    def clean_data(self, data):
        data.drop(
            ["id", "SalesChannelID", "VehicleAge", "DaysSinceCreated"],
            axis=1,
            inplace=True,
        )

        # Convert AnnualPremium with error handling
        try:
            data["AnnualPremium"] = (
                data["AnnualPremium"]
                .str.replace("£", "")
                .str.replace(",", "")
                .astype(float)
            )
        except (AttributeError, ValueError) as e:
            print(f"Error converting AnnualPremium: {e}")
            # If conversion fails, try to handle it differently or keep as is

        for col in ["Gender", "RegionID"]:
            data[col] = self.imputer.fit_transform(data[[col]]).flatten()

        data["Age"] = data["Age"].fillna(data["Age"].median())
        data["HasDrivingLicense"] = data["HasDrivingLicense"].fillna(1)
        data["Switch"] = data["Switch"].fillna(-1)
        data["PastAccident"] = data["PastAccident"].fillna("Unknown", inplace=True)

        Q1 = data["AnnualPremium"].quantile(0.25)
        Q3 = data["AnnualPremium"].quantile(0.75)
        IQR = Q3 - Q1
        upper_bound = Q3 + 1.5 * IQR
        data = data[data["AnnualPremium"] <= upper_bound]

        ## just to set the MLOPS working, nothing else
        data.fillna(0, inplace=True)
        return data
