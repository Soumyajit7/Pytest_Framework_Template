import os


def write_in_csv(df, filename):
    if not os.path.exists('Reports'):
        os.makedirs('Reports')
    df.to_csv(f'Reports/{filename}.csv', index=True)