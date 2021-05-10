from functions.extractData import get_puma_price_list, get_nike_price_list
import pandas as pd


def data_list_to_csv(url, brand, gender):
    price_list = get_puma_price_list(url) if brand == "puma" else get_nike_price_list(url)
    print("Brand : Puma") if brand == "puma" else print("Brand : Nike")

    print("\n =============== Transfer data to csv files =============== \n")

    df = pd.DataFrame(data=price_list)
    print(df)

    # print("puma men ") if gender == "men" and brand == "puma" else print("puma women") if gender == "women" and brand == "puma" else print("=== NIKE ===")
    # print("nike men ") if gender == "men" and brand == "nike" else print("nike women") if gender == "women" and brand == "nike" else print("=== PUMA ===")

    # df.to_csv("./csv_files/puma-men.csv") if gender == "men" and brand == "puma" else df.to_csv(
    #     "./csv_files/puma-women.csv") if gender == "women" and brand == "puma" else df.to_csv(
    #     "./csv_files/nike-men.csv") if gender == "men" and brand == "nike" else df.to_csv(
    #     "./csv_files/nike-women.csv") if gender == "women" and brand == "nike" else print("\n===== ERROR =====\n")

    print("puma men") if gender == "men" and brand == "puma" else print(
        "puma women") if gender == "women" and brand == "puma" else print(
        "nike men") if gender == "men" and brand == "nike" else print(
        "nike women") if gender == "women" and brand == "nike" else print(
        "=== ERROR ===")

    # if brand == "puma" and gender == "men":
    #     print("puma men")
    # elif brand == "puma" and gender == "women":
    #     print("puma women")
    # elif brand == "nike" and gender == "men":
    #     print("nike men")
    # elif brand == "nike" and gender == "women":
    #     print("nike women")

