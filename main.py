from functions.extractDataNike import get_nike_shoes_list
from functions.extractDataPuma import get_puma_shoes_list
import pandas as pd


def data_list_to_csv(url, brand, gender):
    price_list = get_puma_shoes_list(url) if brand == "puma" else get_nike_shoes_list(url)

    print("\n =============== Transfer data to csv files =============== \n")

    df = pd.DataFrame(data=price_list)
    # print(df)

    df.to_csv("./csv_files/puma-men.csv") if gender == "men" and brand == "puma" else df.to_csv(
        "./csv_files/puma-women.csv") if gender == "women" and brand == "puma" else df.to_csv(
        "./csv_files/nike-men.csv") if gender == "men" and brand == "nike" else df.to_csv(
        "./csv_files/nike-women.csv") if gender == "women" and brand == "nike" else print("\n===== ERROR =====\n")



if __name__ == "__main__":
    # data_list_to_csv("https://eu.puma.com/fr/fr/homme/chaussures", "puma", "men")
    # data_list_to_csv("https://eu.puma.com/fr/fr/femme/chaussures", "puma", "women")

    # data_list_to_csv("https://www.nike.com/fr/w/hommes-chaussures-nik1zy7ok", "nike", "men")
    data_list_to_csv("https://www.nike.com/fr/w/femmes-chaussures-5e1x6zy7ok", "nike", "women")

    # dfPumaMen = pd.read_csv("./csv_files/puma-men.csv")
    # pumaMenPrice = dfPumaMen["Price"]
