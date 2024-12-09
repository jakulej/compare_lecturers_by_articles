from db import extract_data
#DATA_TO_ANYLSE = ('citedby_count','author_count', 'authkeywords', 'fund_sponsor')

#Map each article to dict containing each stat f.eg
#[citedby_cout: [1,2,4,5]]
#[author_count: [1,1,2,1]]


def preproces(author_id):
    DATA_TO_ANYLSE = ('citedby_count','author_count')
    preprocesed_data = {key: [] for key in DATA_TO_ANYLSE}
    data = extract_data(author_id=author_id)
    preprocesed_data['author_id'] = []
    for article in data:
        for key in DATA_TO_ANYLSE: 
            preprocesed_data[key].append(article[key])
        preprocesed_data['author_id'].append(author_id)
            
    return preprocesed_data

#Example
#result = preproces("56285148000")
#print(result)


