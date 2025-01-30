import logging


def get_discord_token(mode_file: str, logger: logging.Logger) -> str:
    ## Ascertain mode: dev or production
    try:
        with open(mode_file, "r") as f:
            mode = f.readline().rstrip()
    except FileNotFoundError:
        logger.warning(f"Mode file ({mode_file}) not found, assuming production.")

    ## Read in Discord bot token from file
    token_file = "prodToken.txt"
    if mode == "dev":
        token_file = "devToken.txt"
    try:
        with open(token_file, "r") as f:
            return f.readline().rstrip()
    except FileNotFoundError:
        logger.error(f"File with Discord token missing: {token_file}")
        exit(1)
