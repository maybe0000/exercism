def transform(legacy_data):
    transformed_data = {}
    for key, value in legacy_data.items():
        # print('key value ', key, value)
        for item in value:
            # print('item ',item)
            transformed_data[item.lower()] = key
    return dict(sorted(transformed_data.items()))