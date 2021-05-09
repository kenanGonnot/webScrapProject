import requests
from bs4 import BeautifulSoup

my_url = {}
url = "https://eu.puma.com/fr/fr/homme/chaussures/baskets"

reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, 'html.parser')

# product_containers = soup.find_all({"class": "row product-grid no-gutters"})
#
# product_title_containers = product_containers.find_all({"class": "product-tile-info-text"})
#
# product_price_containers = product_containers.find_all(
#     {"class": "product-tile-price-standard product-tile__price--standard"})
#
# dico_all_product = dict()
dico_prices = dict()

print(reponse.content[:100])

# print(product_price_containers.text)

#
# if __name__ == '__main__':
#     request.request(url)
#     writeToCsv.writeCSV()
#


# ====== // =======

# def get_commentary_and_date(list):
#     name_text_list = []
#     date_text_list = []
#     comment_text_list = []
#     like_nbr_list = []
#     # print(name, "\n", date, "\n", commentary, "\n", like_nbr, "\n")
#
#     for comment in list:
#         text_list = comment.split('\n')
#         if len(text_list) < 4: continue
#         text_list = text_list[:-1]
#         name = text_list[0]
#         date = text_list[1]
#         comment = "|".join(text_list[2:-1])
#         like_nbr = text_list[-1]
#         name_text_list.append(name)
#         date_text_list.append(date)
#         comment_text_list.append(comment)
#         like_nbr_list.append(like_nbr)
#     dict = {'name': name_text_list, 'date': date_text_list, 'comment': comment_text_list, 'like': like_nbr_list}
#
#     return dict
