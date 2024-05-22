import json
import logging

import azure.functions as func

from freight_config import (
    FreightConfig,
    FreightConfigBakemark,
    FreightConfigBakemarkImage,
)
from prompt_template import system_message_image, text_prompt, user_message_image
from utils import MODEL_HAIKU, MODEL_SONNET, make_llm, read_email, read_image

app = func.FunctionApp()


@app.blob_trigger(
    arg_name="myblob",
    path="eml/{name}",
    connection="sgnstetldeveus01_STORAGE",
)
@app.blob_output(
    arg_name="outputblob",
    path="llm/{name}.json",
    connection="sgnstetldeveus01_STORAGE",
)
def blob_trigger_llm(myblob: func.InputStream, outputblob: func.Out[str]):
    logging.info(f"BLOB {myblob.name}")
    f = myblob.read()
    if myblob.name.split(".")[-1] == "eml":
        email_text, email_sender = read_email(f)
        if email_sender == "bakemark":
            llm = make_llm(MODEL_HAIKU, FreightConfigBakemark)
        else:
            llm = make_llm(MODEL_HAIKU, FreightConfig)
        extraction_chain = text_prompt | llm
        res = extraction_chain.invoke({"email": email_text})
        res_dict = res.dict()
        res_dict["sender"] = email_sender
    else:
        img_base64 = read_image(f)
        prompt = system_message_image + user_message_image(img_base64=img_base64)
        messages = prompt.format_messages()
        llm = make_llm(MODEL_SONNET, FreightConfigBakemarkImage)
        res = llm.invoke(messages)
        res_dict = res.dict()
    json_data = json.dumps(res_dict)
    outputblob.set(json_data)
