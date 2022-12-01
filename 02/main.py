import pandas as pd

import matplotlib.pyplot as plt


def main():
    df = pd.read_csv('data.csv')
    print(df.to_string())


if __name__ == '__main__':
    main()


