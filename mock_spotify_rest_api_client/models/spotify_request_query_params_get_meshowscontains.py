from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMeshowscontains")


@_attrs_define
class SpotifyRequestQueryParamsGETMeshowscontains:
    """
    Attributes:
        ids (str):
    """

    ids: str

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "ids": ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = d.pop("ids")

        spotify_request_query_params_get_meshowscontains = cls(
            ids=ids,
        )

        return spotify_request_query_params_get_meshowscontains