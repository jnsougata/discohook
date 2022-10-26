import traceback
from .embed import Embed
from fastapi.requests import Request
from .enums import InteractionCallbackType
from fastapi.responses import JSONResponse


def build_traceback_embed(e: Exception) -> Embed:
    err = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
    embed = Embed(title='Stack Trace', description=f'```py\n{err}\n```', color=0xff0000)
    embed.footer(text='⚠️Turn off express_debug in production!')
    return embed

