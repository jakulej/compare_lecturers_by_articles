from db import extract_data
#DATA_TO_ANYLSE = ('citedby_count','author_count')
DATA_TO_ANYLSE = ('citedby_count','author_count', 'authkeywords', 'fund_sponsor')


def preproces(author_id):
    preprocesed_data = {key: [] for key in DATA_TO_ANYLSE}
    data = extract_data(author_id=author_id)

    for article in data:
        for key in preprocesed_data.keys(): 
            preprocesed_data[key].append(article[key])
    return preprocesed_data


print(preproces("6701511885"))