from py_compile import main


class Univariate:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def quanQual(self):
        quantitative = []
        qualitative = []
        for column in self.dataframe.columns:
            if self.dataframe[column].dtypes == 'object':
                qualitative.append(column)
            else:
                quantitative.append(column)
        return quantitative, qualitative
    
# if __name__ == "__main__":
#     main()