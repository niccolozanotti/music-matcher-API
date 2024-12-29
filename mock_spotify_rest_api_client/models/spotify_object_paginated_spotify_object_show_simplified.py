from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_show_simplified import SpotifyObjectShowSimplified


T = TypeVar("T", bound="SpotifyObjectPaginatedSpotifyObjectShowSimplified")


@_attrs_define
class SpotifyObjectPaginatedSpotifyObjectShowSimplified:
    """
    Attributes:
        items (list['SpotifyObjectShowSimplified']):
        href (str):
        limit (float):
        next_ (Union[None, str]):
        offset (float):
        previous (Union[None, str]):
        total (float):
    """

    items: list["SpotifyObjectShowSimplified"]
    href: str
    limit: float
    next_: Union[None, str]
    offset: float
    previous: Union[None, str]
    total: float

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        href = self.href

        limit = self.limit

        next_: Union[None, str]
        next_ = self.next_

        offset = self.offset

        previous: Union[None, str]
        previous = self.previous

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "items": items,
                "href": href,
                "limit": limit,
                "next": next_,
                "offset": offset,
                "previous": previous,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.spotify_object_show_simplified import SpotifyObjectShowSimplified

        d = src_dict.copy()
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = SpotifyObjectShowSimplified.from_dict(items_item_data)

            items.append(items_item)

        href = d.pop("href")

        limit = d.pop("limit")

        def _parse_next_(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_ = _parse_next_(d.pop("next"))

        offset = d.pop("offset")

        def _parse_previous(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        previous = _parse_previous(d.pop("previous"))

        total = d.pop("total")

        spotify_object_paginated_spotify_object_show_simplified = cls(
            items=items,
            href=href,
            limit=limit,
            next_=next_,
            offset=offset,
            previous=previous,
            total=total,
        )

        return spotify_object_paginated_spotify_object_show_simplified