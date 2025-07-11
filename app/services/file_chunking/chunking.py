def chunk_srt_file(file_path, chunk_size=100):
    """
    Reads an .srt subtitle file and chunks it into blocks of `chunk_size` subtitles.

    Args:
        file_path (str): Path to the .srt file.
        chunk_size (int): Number of subtitle blocks per chunk. Default is 100.

    Returns:
        List[str]: List of subtitle chunks, each a single string containing `chunk_size` blocks.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split into blocks (subtitle blocks are separated by double newlines)
    subtitle_blocks = content.strip().split("\n\n")

    # Chunk blocks into groups of `chunk_size`
    chunks = []
    for i in range(0, len(subtitle_blocks), chunk_size):
        chunk = "\n\n".join(subtitle_blocks[i : i + chunk_size])
        chunks.append(chunk)

    return chunks
