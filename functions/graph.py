import itertools

import matplotlib.pyplot as plt
import pandas as pd


def plot_display_order(brand):
    df_men = pd.read_csv("./csv_files/" + brand + "-men.csv")
    men_price = df_men["price"]

    df_women = pd.read_csv("./csv_files/" + brand + "-women.csv")
    women_price = df_women["price"]

    min_length = min(len(women_price), len(men_price))
    women_price = women_price[:min_length]
    men_price = men_price[:min_length]

    plt.plot(list(men_price), '-b', label=str(brand) + " Men")
    plt.plot(list(women_price), '-r', label=str(brand) + " Women")
    plt.ylabel('price')
    plt.title('price ' + str(brand) + '- display order')
    plt.legend()
    plt.show()


def plot_compare_brands_gender(first_csv, second_csv):
    first_df = pd.read_csv(first_csv)
    first_price = first_df["price"]
    first_price = first_price.sort_values(ascending=True)

    second_df = pd.read_csv(second_csv)
    second_price = second_df["price"]
    second_price = second_price.sort_values(ascending=True)

    first_price, second_price = resize_data(first_price, second_price)

    plt.plot(list(first_price), '-b', label=str(first_csv))
    plt.plot(list(second_price), '-r', label=str(second_csv))
    plt.ylabel('price')
    plt.title('price comparison')
    plt.legend()
    plt.show()


def plot_compare_brand(first_brand, second_brand):
    merged_first_brand_list = load_brand_data(first_brand)
    merged_second_brand_list = load_brand_data(second_brand)

    merged_first_brand_list, merged_second_brand_list = resize_data(merged_first_brand_list, merged_second_brand_list)

    plt.plot(list(merged_first_brand_list), '-b', label=str(first_brand))
    plt.plot(list(merged_second_brand_list), '-r', label=str(second_brand))
    plt.ylabel('price')
    plt.title('Brand price comparison')
    plt.legend()
    plt.show()


def resize_data(merged_first_brand_list, merged_second_brand_list):
    min_length = min(len(merged_first_brand_list), len(merged_second_brand_list))
    merged_first_brand_list = merged_first_brand_list[:min_length]
    merged_second_brand_list = merged_second_brand_list[:min_length]
    return merged_first_brand_list, merged_second_brand_list


def load_brand_data(brand):
    df_men = pd.read_csv("../csv_files/" + brand + "-men.csv")
    brand_price_men = df_men["price"]
    df_women = pd.read_csv("../csv_files/" + brand + "-women.csv")
    brand_price_women = df_women["price"]
    merged_brand_list = list(itertools.chain(brand_price_women, brand_price_men))
    merged_brand_list.sort()
    return merged_brand_list


if __name__ == '__main__':
    # plot_display_order("puma")
    # plot_display_order("nike")
    # plot_compare_brands_gender("../csv_files/nike-men.csv", "../csv_files/puma-men.csv")
    # plot_compare_brands_gender("../csv_files/nike-women.csv", "../csv_files/puma-women.csv")

    plot_compare_brand("nike", "puma")
