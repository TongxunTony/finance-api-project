from screening import screen_companies


companies = [

    "AAPL",
    "MSFT",
    "NVDA",
    "GOOGL",
    "AMZN"

]


results = screen_companies(
    companies
)


for r in results:

    print(r)