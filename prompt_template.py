from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

system_message_image = SystemMessage(
    content=[
        {
            "type": "text",
            "text": "You are an advance data exctractor. Your task to excract key information about shipment from email. Email consists from image.",
        }
    ]
)


def user_message_image(img_base64):
    return HumanMessage(
        content=[
            {
                "type": "image_url",
                "image_url": {
                    # langchain logo
                    "url": f"data:image/png;base64,{img_base64}"
                },
            },
            {
                "type": "text",
                "text": """Exctract information from the email which consists from followin image. 
            Some information about shipment could be in the subject of the email.
            there is the glossary about shipment: PU: pickup point, DEL: delivery point, Origin: pickup point, Destination: Delivery point, FTL: full truck load, TL: truck load.
            there could be different equipment types, for example dry, frozen, TL Dry, FTL Frozen, FTL and so on.
            Pickup and Delivery point return in format: City, State, for example: Los Angeles, CA.
            If there is no ZIP code of pickup or delivery point, you should find and return the proper one you know for that city and state, do not miss zip.
            Make sure to answer in the correct format. Use FreightInfo tool.""",
            },
        ]
    )


ai_message = AIMessage(content="your response on image")


# def prompt_template(img_base64):
#     prompt = system_message + user_message(img_base64) + ai_message + "{email}"
#     return prompt


text_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an advance data exctractor. Your task to excract key information about shipment from email.",
        ),
        (
            "human",
            """Exctract information from the following email. there is the glossary about shipment: PU: pickup point, DEL: delivery point, Origin: pickup point, Destination: Delivery point, FTL: full truck load, TL: truck load.
            there could be different equipment types, for example dry, frozen, TL Dry, FTL Frozen, FTL and so on.
            Pickup and Delivery point always return in format: city, state, for example: Los Angeles CA return as Los Angeles, CA.
            If there is no ZIP code of pickup or delivery point, you should find and return the proper one you know for that city and state, do not miss zip.
            <email>
            {email}
            </email>
            Make sure to answer in the correct format. Use FreightInfo tool. 
            """,
        ),
    ]
)
