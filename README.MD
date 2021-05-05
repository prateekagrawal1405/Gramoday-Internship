# Data Scraping

a.	Write a python script to fetch data of prices for the year 2020 (date wise from 1st Jan’2020 to 31st Dec’2020) for district “Agra” of Uttar Pradesh from the data sources mentioned in the data section (can take point b as a reference). Following is the output schema expected:

The following file `fetch_data_v1.py` downloads the required data and exports it in `fetch_data_v1.csv`.

## Dependencies

- pandas
- tqdm


# EDA

The file `EDA.py` does a basic exploratory data analysis and exports the trends for each market in a folder `price_prediction`. Note that the folder needs to be already there thought it may be empty

## Dependencies

- pandas
- seaborn
- matplotlib

# Machine Learning Modeling 

The output and the results are mentioned in the docx file. The file `AutoML_Regression_Pycaret.ipynb` contains the source code for AutoML Modelling and its results as well.

## Dependencies
Note : Run the ipynb file in colab for easy usage.
- pandas
- pycaret
