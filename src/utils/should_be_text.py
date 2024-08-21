def should_be_text(chunk):
    return chunk.startswith((" ", ".", ":", ";")) or chunk.endswith(" ")
