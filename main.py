import pandas as pd
from functions.extractDataNike import get_nike_shoes_list
from functions.extractDataPuma import get_puma_shoes_list
from functions.graph import plot_display_order, plot_compare_brands


def data_list_to_csv(url, brand, gender):
    price_list = get_puma_shoes_list(url) if brand == "puma" else get_nike_shoes_list(url)

    print("\n =============== Transfer " + brand + " " + gender + " data to csv files (" +
          str(len(price_list)) + ") =============== \n")

    df = pd.DataFrame(data=price_list)
    # print(df)

    df.to_csv("./csv_files/puma-men.csv") if gender == "men" and brand == "puma" else df.to_csv(
        "./csv_files/puma-women.csv") if gender == "women" and brand == "puma" else df.to_csv(
        "./csv_files/nike-men.csv") if gender == "men" and brand == "nike" else df.to_csv(
        "./csv_files/nike-women.csv") if gender == "women" and brand == "nike" else print("\n===== ERROR =====\n")


if __name__ == "__main__":
    data_list_to_csv("https://eu.puma.com/fr/fr/homme/chaussures", "puma", "men")
    # data_list_to_csv("https://eu.puma.com/fr/fr/femme/chaussures", "puma", "women")
    # data_list_to_csv("https://www.nike.com/fr/w/hommes-chaussures-nik1zy7ok", "nike", "men")
    data_list_to_csv("https://www.nike.com/fr/w/femmes-chaussures-5e1x6zy7ok", "nike", "women")

    # plot_display_order("puma")
    # plot_display_order("nike")
    # plot_compare_brands("./csv_files/nike-men.csv", "./csv_files/puma-men.csv")
    # plot_compare_brands("./csv_files/nike-women.csv", "./csv_files/puma-women.csv")


