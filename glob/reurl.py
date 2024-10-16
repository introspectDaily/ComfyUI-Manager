def reurl(url:str):
    if url.startswith("https://raw.githubusercontent.com/") or url.startswith("https://github.com") or url.startswith("gist.githubusercontent.com"):
        url = "https://ghp.ci/" + url
    elif url.startswith("https://huggingface.co"):
        url = url.replace("huggingface.co", "hf-mirror.com")
    elif url.startswith("https://civitai.com"):
        url = url.replace("civitai.com", "civitai.work")
    return url