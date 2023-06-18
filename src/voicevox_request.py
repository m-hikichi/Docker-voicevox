import requests
import json
from typing import Dict, Any, Union


def create_audio_query(text: str, speaker: int=3) -> Dict[str, Any]:
    """
    与えられたテキストを話者からオーディオクエリを作成

    Args:
        text (str): 音声に変換されるテキスト
        speaker (int): 音声合成に使用する話者ID

    Return:
        生成されたオーディオクエリをJSONオブジェクトとして返す
    """
    url = "http://voicevox:50021/audio_query"
    response = requests.post(url, params={"text":text, "speaker":speaker})
    return response.json()


def synthesize_voice(query_data: Dict[str, Any], speaker: int=3) -> bytes:
    """
    与えられたオーディオクエリデータから音声を合成します

    Args:
        query_data (): JSON形式のオーディオクエリデータ
        speaker (int): 音声合成に使用する話者ID

    Return:
        合成された音声をバイナリデータとして返す
    """
    url = "http://voicevox:50021/synthesis"
    response = requests.post(url, params={"speaker":speaker}, data=json.dumps(query_data))
    return response.content


def save_to_file(content: bytes, filename: str="voicevox.wav") -> None:
    """
    与えられたコンテンツをファイルに保存

    Args:
        content : 保存されるコンテンツ
        filename (str): コンテンツを保存するファイルの名前
    """
    with open(filename, mode="wb") as f:
        f.write(content)


def main():
    text = "ずんだもんなのだ"
    query_data = create_audio_query(text)
    synthesize_voice_data = synthesize_voice(query_data)
    save_to_file(synthesize_voice_data)


if __name__=="__main__":
    main()
