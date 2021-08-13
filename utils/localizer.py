def localize_region(slug: str):
    regions = [
        {'slug': 'nyc1', 'name': '纽约 1'}, {'slug': 'nyc2', 'name': '纽约 2'}, {'slug': 'nyc3', 'name': '纽约 3'},
        {'slug': 'sfo1', 'name': '旧金山 1'}, {'slug': 'sfo2', 'name': '旧金山 2'}, {'slug': 'sfo3', 'name': '旧金山 3'},
        {'slug': 'ams2', 'name': '阿姆斯特丹 2'}, {'slug': 'ams3', 'name': '阿姆斯特丹 3'},
        {'slug': 'sgp1', 'name': '新加坡 1'}, {'slug': 'lon1', 'name': '伦敦 1'},
        {'slug': 'fra1', 'name': '法国 1'}, {'slug': 'blr1', 'name': '班加罗尔 1'},
        {'slug': 'tor1', 'name': '多伦多 1'},
    ]

    for region in regions:
        if region['slug'] == slug:
            return region['name']

    return slug
