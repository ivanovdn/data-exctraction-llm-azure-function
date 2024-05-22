import base64
import os
from io import BytesIO
from pathlib import Path

from langchain_anthropic.experimental import ChatAnthropicTools
from unstructured.partition.auto import partition

MODEL_HAIKU = "claude-3-haiku-20240307"
MODEL_SONNET = "claude-3-sonnet-20240229"


def read_image(io):
    # img_path = Path(image_path)
    img_base64 = base64.b64encode(io).decode("utf-8")
    return img_base64


def read_email(io):
    f = BytesIO(io)
    elements = partition(file=f)
    return (
        "\n".join(
            ["Subject: " + elements[0].metadata.subject] + [str(el) for el in elements]
        ),
        elements[0].metadata.sent_from[0].split("@")[-1].split(".")[0],
    )


def make_llm(model_name, freight_config):
    return ChatAnthropicTools(
        temperature=0.0,
        model=model_name,
        anthropic_api_key=os.environ["ANTHROPIC_API_KEY"],
    ).with_structured_output(freight_config)
