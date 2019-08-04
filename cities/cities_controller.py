from .models import Region


class CitiesController:
    """
    Controller for cities for send info to front
    """
    def __init__(self):
        self.regions = []

    @staticmethod
    def get_regions_from_db():
        """
        Methods for get all regions from Data Base
        Returns:
            (object): Queryset from DB

        Examples:
            .. code-block:: python3

                from cities.cities_controllers import CitiesController

                cities_controller = CitiesController()
                data = cities_controller.prepare_data()

        """
        return Region.objects.all()

    def prepare_dict(self):
        regions = self.get_regions_from_db()
        for region in regions:
            cities = self.cities_from_region(region)
            self.regions.append(
                {'region': region,
                 'cities': cities}
            )
        return self.regions

    @staticmethod
    def cities_from_region(region):
        dict_cities = []
        cities = region.cities.all()
        for city in cities:
            if city.is_active:
                dict_cities.append({'city': city})
        return dict_cities
