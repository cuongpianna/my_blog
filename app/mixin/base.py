class PaginatedAPIMixin:
    @staticmethod
    def to_collection_dict(query, page, per_page, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_json() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {

            }
        }
        return data