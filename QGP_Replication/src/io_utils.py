import pandas as pd

def save_fg2(temperature, fg2_values):

    df = pd.DataFrame({

        "T/Tc": temperature,
        "fg2": fg2_values

    })

    df.to_csv(
        "data/fg2_results.csv",
        index=False
    )