class Asset:
    """
    Represents a Discord asset.

    This is used internally by the library. You should not need to use this.

    Parameters
    ----------
    hash: :class:`str`
        The hash of the asset.
    fragment: :class:`str`
        The fragment of the asset path.
    """
    base_url = "https://cdn.discordapp.com"

    def __init__(self, *, hash: str, fragment: str) -> None:  # noqa
        self._hash = hash
        self._fragment = fragment

    def __str__(self) -> str:
        if self.dynamic:
            return f"{self.base_url}/{self._fragment}/{self._hash}.gif?size=1024"
        return f"{self.base_url}/{self._fragment}/{self._hash}.webp?size=1024"

    @property
    def dynamic(self) -> bool:
        """
        Checks if the asset is animated.

        Returns
        -------
        :class:`bool`
        """
        return self._hash.startswith("a_")

    @property
    def url(self) -> str:
        """
        Returns the URL of the asset in its default size with `.webp` format.

        Returns
        -------
        :class:`str`
        """
        return str(self)

    def url_as(self, *, size: int = 1024, format: str = "png") -> str:  # noqa
        """
        Returns the URL of the asset in the specified size and format.

        Parameters
        ----------
        size: :class:`int`
            The size of the asset.
        format: :class:`str`
            The format of the asset.

        Returns
        -------
        :class:`str`
        
        """
        return f"{self.base_url}/{self._fragment}.{format}?size={size}"
