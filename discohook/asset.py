
class Asset:

    base_url = "https://cdn.discordapp.com"

    def __init__(self, *, hash: str, fragment: str) -> None:
        self._hash = hash
        self._fragment = fragment
    
    def __str__(self) -> str:
        if self.dynamic:
            return f"{self.base_url}/{self._fragment}/{self._hash}.gif?size=1024"
        return f"{self.base_url}/{self._fragment}/{self._hash}.webp?size=1024"
    
    @property
    def dynamic(self) -> bool:
        return self._hash.startswith("a_")
    
    @property
    def url(self) -> str:
        return str(self)
    
    def url_as(self, *, size: int = 1024, format: str = "png") -> str:
        return f"{self.base_url}/{self._fragment}.{format}?size={size}"