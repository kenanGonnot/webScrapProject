from functions.extractDataPuma import get_puma_shoes_list, get_nike_shoes_list
import pandas as pd
import matplotlib.pyplot as plt

def data_list_to_csv(url, brand, gender):
    price_list = get_puma_shoes_list(url) if brand == "puma" else get_nike_shoes_list(url)

    print("\n =============== Transfer data to csv files =============== \n")

    df = pd.DataFrame(data=price_list)
    # print(df)


    # df.to_csv("./csv_files/puma-men.csv") if gender == "men" and brand == "puma" else df.to_csv(
    #     "./csv_files/puma-women.csv") if gender == "women" and brand == "puma" else df.to_csv(
    #     "./csv_files/nike-men.csv") if gender == "men" and brand == "nike" else df.to_csv(
    #     "./csv_files/nike-women.csv") if gender == "women" and brand == "nike" else print("\n===== ERROR =====\n")

    print("puma men") if gender == "men" and brand == "puma" else print(
        "puma women") if gender == "women" and brand == "puma" else print(
        "nike men") if gender == "men" and brand == "nike" else print(
        "nike women") if gender == "women" and brand == "nike" else print(
        "=== ERROR ===")

