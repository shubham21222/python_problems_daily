class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source_cities = set()

        for path in paths:
            source_cities.add(path[0])

        for path in paths:
            destination_city = path[1]

            if destination_city not in source_cities:
                return destination_city