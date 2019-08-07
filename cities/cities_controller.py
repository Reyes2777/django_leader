from .models import Region, City


class CitiesController:
    """
    Controller for cities for send info to front
    """
    def __init__(self):
        self.regions = []

    @staticmethod
    def get_cities_from_db():
        """
        Methods for get all regions from Data Base
        Returns:
            (object): Queryset from DB

        Examples:
            .. code-block:: python3

                from cities.cities_controllers import CitiesController

                cities_controller = CitiesController()
                data = cities_controller.get_cities_from_db

                >> Queryset

        """
        return City.objects.all()

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
                data = cities_controller.get_regions_from_db

                >> Queryset

        """
        return Region.objects.all()

    def prepare_dict(self):
        """
        Method for get dictionary with all regions and cities relation
        Returns:
            (dict): return dictionary with all regions and city

        Examples:
            .. code-block:: python3

                from cities.cities_controllers import CitiesController

                cities_controller = CitiesController()
                data = cities_controller.prepare_data()

                >> [{'region': <Region: Antioquia>, 'cities': [{'city': <City: Funza>}]},
                    {'region': <Region: Cundinamarca>, 'cities': [{'city': <City: Bogota>},
                    {'city': <City: Funza>}, {'city': <City: Chia>}]}]


        """
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
        """
              Method for get dictionary with all regions and cities relation
              Returns:
                  (dict): return dictionary with all regions and city

              Examples:
                  .. code-block:: python3

                      from cities.cities_controllers import CitiesController

                      cities_controller = CitiesController()
                      data = cities_controller.cities_from_region

                      >> [{'city': <City: Funza>}]},
                          {'region': <Region: Cundinamarca>, 'cities': [{'city': <City: Bogota>},
                          {'city': <City: Funza>}, {'city': <City: Chia>}]
        """
        dict_cities = []
        cities = region.cities.all()
        for city in cities:
            if not city.is_active:
                region.cities.remove(city)
            if city.is_active:
                dict_cities.append({'city': city})
        return dict_cities
