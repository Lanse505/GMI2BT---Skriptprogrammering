class SearchRatingHandler(object):

    def __init__(self, response: list):
        self.ratings = response

    def __str__(self):
        printable = "\n\t\t"
        for store in self.ratings:
            count = 1
            for key, value in store.items():
                rating = str(value).replace('Value, ', '')
                if count % 2 == 0:
                    printable = printable + f"{rating}\n\t\t"
                    count = 1
                else:
                    printable = printable + f"{rating}: "
                    count += 1
        return printable[:-3]
