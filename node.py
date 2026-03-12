import os
import urllib.request
import subprocess


class MyFirstNode:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "hello"})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "run"

    CATEGORY = "MyNodes"

    def run(self, text):
        url = "https://koldunov.com/wp-content/uploads/2021/03/06.jpg"
        download_dir = "/Users/ptmff/Downloads"
        os.makedirs(download_dir, exist_ok=True)
        file_path = os.path.join(download_dir, "06.jpg")
        try:
            urllib.request.urlretrieve(url, file_path)
            # Открыть скачанный файл стоковым приложением
            try:
                subprocess.run(["open", file_path], check=False)
                result = text.upper()
            except Exception as e:
                result = f"ERROR opening image: {e}"
        except Exception as e:
            result = f"ERROR downloading image: {e}"

        return (result,)


NODE_CLASS_MAPPINGS = {
    "MyFirstNode": MyFirstNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MyFirstNode": "My First Node"
}
