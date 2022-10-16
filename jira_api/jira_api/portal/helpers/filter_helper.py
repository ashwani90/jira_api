def filter_query(request, fields,manager):
    for field in fields:
        query_value = request.GET.get(field['value'])
        if query_value:
            if field['type'] == "contains":
                field_con=field['value']+"__contains"
                manager = manager.filter(**{field_con:query_value})
            if field['type'] == "equal":
                field_dict = {field['value']:query_value}
                manager = manager.filter(**field_dict)
            if field['type'] == "range":
                dates = query_value.split(",")
                
                field_dict={field['value']+"__range":(str(dates[0]),str(dates[1]))}
                manager = manager.filter(**field_dict)

    return manager