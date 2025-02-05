# parse_data

This Python script _cleans_ and joins together all files in a folder - intended to combine data tables in `.txt` files with vertical bar `|` delimiters of the following format:

```
|Method|Alpha ||Beta |
|Tau      |G2 Fit      |Error     |R-Size   |Prob 

|0    |0  |0  |0      |0  |
```

For all files, the results are joined horizontally with the name of the file added to the first column of that data. For instance, if there are two files in the folder, the result would become:

```
"Filename, Tau ",G2 Fit ,Error ,R-Size ,Prob ,"Filename2, Tau ",G2 Fit 1,Error 1,R-Size 1,Prob 1
5e-07    ,1.8538   ,0.002269  ,0.5      ,8.9879e-17  ,5e-07    ,1.8538   ,0.002269  ,0.5      ,8.9879e-17
```

This combined file is saved in a file called `combined.csv` to be easily accessible by Excel.

## To Run
Change line 4 in `masher.py` to the path to your folder containing the data.

Run in the command line: `python masher.py`

## Side Note
If you're sure that your data is already cleaned and ready to be merged, you would not need this script.

You can run the following in command line to concatenate your columns horizontally in the folder:
```
paste *.txt >> combined.txt
```

Or the following in command line to concatenate your columns vertically:
```
cat *.txt >> combined.txt
```
