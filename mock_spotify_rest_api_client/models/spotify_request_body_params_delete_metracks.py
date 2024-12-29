from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestBodyParamsDELETEMetracks")


@_attrs_define
class SpotifyRequestBodyParamsDELETEMetracks:
    """
    Attributes:
        ids (Union[Unset, list[str]]):
    """

    ids: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = cast(list[str], d.pop("ids", UNSET))

        spotify_request_body_params_delete_metracks = cls(
            ids=ids,
        )

        return spotify_request_body_params_delete_metracks
