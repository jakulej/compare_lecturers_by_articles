def manova(first_id, second_id):
    
    import pandas as pd
    from statsmodels.multivariate.manova import MANOVA
    from preproces import preproces
    #TO TEST:

    #FIRST ID = "6701511885"
    #SECOND ID = "56285148000"


# data = pd.DataFrame({
#     'Autor': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
#     'Słowa_kluczowe': [15, 16, 14, 12, 11, 13, 20, 21, 19],
#     'Sentyment': [0.8, 0.9, 0.7, -0.2, -0.1, -0.3, 0.5, 0.6, 0.4],
#     'Cytowania': [25, 26, 24, 30, 29, 31, 15, 16, 14]
# })
    first = preproces(first_id)
    second = preproces(second_id)
    #print(first)
    for key in first.keys():
        first[key].extend(second[key])


    data = pd.DataFrame.from_dict(first)

    manova = MANOVA.from_formula('citedby_count + author_count + authkeywords ~ author_id', data=data)
    result = manova.mv_test()
    result_df = result['author_id']['stat'].to_json()
    #print(type(result_df))
    print(result_df)
    return result_df
#manova("6602252130", "57204034434")
