import polars as pl
import time
import pathlib

s = time.time()

# read csv file
df = pl.scan_csv('D:/Benchmark/uSpace/1MillionRows.csv')
filter = df.filter((((pl.col('Ledger') >= "L10") & (pl.col('Ledger') <= "L15")) | ((pl.col('Ledger') >= "L50") & (pl.col('Ledger') <= "L55")) | ((pl.col('Ledger') >= "L82") & (pl.col('Ledger') <= "L88"))) & (((pl.col('Account') >= 12222) & (pl.col('Account') <= 12888)) | ((pl.col('Account') >= 15555) & (pl.col('Account') <= 16888))) & ((pl.col('Project') > "B28") | (pl.col('Project') < "B22")))

# write csv file
a = filter.collect()
print("Number of selected rows: {}", filter.select(pl.count()).collect());
path: pathlib.Path = "D:/Benchmark/uSpace/Polars-Filter1M.csv"
a.write_csv(path)

e = time.time()
print(f"Duration: {(e-s):.3f} seconds")







