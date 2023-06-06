from ..internal import BaseAPI
from .objects import ObjectsAPI
from .schemas import SchemasAPI


class IOCeanAPI(BaseAPI):
    """IOCean API."""

    @property
    def collections(self):
        """Get IOCean collections handle."""
        return None  # TODO: implement CollectionsAPI

    @property
    def schemas(self) -> SchemasAPI:
        """Get IOCean schemas handle."""
        return SchemasAPI(self._connector)

    @property
    def objects(self) -> ObjectsAPI:
        """Objects API handle."""
        return ObjectsAPI(self._connector)
