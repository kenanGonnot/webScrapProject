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


def plot_compare_brands(first_csv, second_csv):
    first_df = pd.read_csv(first_csv)
    first_price = first_df["price"]
    first_price = first_price.sort_values(ascending=True)

    second_df = pd.read_csv(second_csv)
    second_price = second_df["price"]
    second_price = second_price.sort_values(ascending=True)

    min_length = min(len(first_price), len(second_price))
    first_price = first_price[:min_length]
    second_price = second_price[:min_length]

    plt.plot(list(first_price), '-b', label=str(first_csv))
    plt.plot(list(second_price), '-r', label=str(second_csv))
    plt.ylabel('price')
    plt.title('price comparison')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # plot_display_order("puma")
    # plot_display_order("nike")

    plot_compare_brands("../csv_files/nike-men.csv", "../csv_files/puma-men.csv")
    plot_compare_brands("../csv_files/nike-women.csv", "../csv_files/puma-women.csv")
