import pandas as pd


def get_drug_reference(df_drug: pd.DataFrame, df_article: pd.DataFrame, drug_column_name = "drug", article_column_name = "title"):
    """
        Return the reference for each drugs (in articles)
    """

    #combine words list into one string, separated by |
    drug_names = '|'.join(df_drug[drug_column_name].tolist()).lower()

    # Reset index of articles
    df_article = df_article.reset_index()

    #extract all words from keywords_combined found in titles' title column
    common = (df_article[article_column_name]
            .str.lower()
            .str.extractall(fr'({drug_names})')
            .reset_index()
            .drop('match',axis=1)
            .set_axis(['index',drug_column_name],axis='columns'))

    #hook back our result to keyword dataframe
    result = df_drug.merge(
        common, 
        left_on=df_drug[drug_column_name].str.lower(), 
        right_on=common[drug_column_name].str.lower(), 
        how='left')

    #finally, merge with titles 
    result = result.join(df_article,on='index', rsuffix="_article", lsuffix="_drug")

    result = result[["internal_id_article", "internal_id_drug"]]

    return result
