from functions.listToCsv import data_list_to_csv
import pandas as pd

if __name__ == "__main__":
    # data_list_to_csv("https://eu.puma.com/fr/fr/homme/chaussures", "puma", "men")
    # data_list_to_csv("https://eu.puma.com/fr/fr/femme/chaussures", "puma", "women")

    # data_list_to_csv("https://www.nike.com/fr/w/hommes-chaussures-nik1zy7ok", "nike", "men")
    data_list_to_csv("https://www.nike.com/fr/w/femmes-chaussures-5e1x6zy7ok", "nike", "women")


    dfPumaMen = pd.read_csv("./csv_files/puma-men.csv")
    pumaMenPrice = dfPumaMen["Price"]
