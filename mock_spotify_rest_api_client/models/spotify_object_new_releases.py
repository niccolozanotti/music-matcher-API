from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.spotify_object_paginated_spotify_object_album_simplified import (
        SpotifyObjectPaginatedSpotifyObjectAlbumSimplified,
    )


T = TypeVar("T", bound="SpotifyObjectNewReleases")


@_attrs_define
class SpotifyObjectNewReleases:
    """
    Attributes:
        albums (SpotifyObjectPaginatedSpotifyObjectAlbumSimplified):
    """

    albums: "SpotifyObjectPaginatedSpotifyObjectAlbumSimplified"

    def to_dict(self) -> dict[str, Any]:
        albums = self.albums.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "albums": albums,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.spotify_object_paginated_spotify_object_album_simplified import (
            SpotifyObjectPaginatedSpotifyObjectAlbumSimplified,
        )

        d = src_dict.copy()
        albums = SpotifyObjectPaginatedSpotifyObjectAlbumSimplified.from_dict(
            d.pop("albums")
        )

        spotify_object_new_releases = cls(
            albums=albums,
        )

        return spotify_object_new_releases
