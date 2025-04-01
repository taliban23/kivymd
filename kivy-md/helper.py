
from zhipuai import ZhipuAI

client = ZhipuAI(
    api_key= "c522b9ed146a4e51ba9d9fa330a1dd87.qJoXCk6aPhqUdQaS",
    base_url= "https://open.bigmodel.cn/api/paas/v4",
    )

def print_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then prints the response of the model.
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        completion = client.chat.completions.create(
            model= "glm-4-flash",
#              model="gpt-3.5-turbo-0125", # USE THIS MODEL IF YOU ARE USING YOUR OWN OPENAI KEY
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        response = completion.choices[0].message.content
        print("_"*100)
        print(response)
        print("_"*100)
        print("\n")
    except TypeError as e:
        print("Error:", str(e))


def get_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then saves the response of the model as
    a string.
    """
    completion = client.chat.completions.create(
        model= "glm-4-flash",
#          model="gpt-3.5-turbo-0125", # USE THIS MODEL IF YOU ARE USING YOUR OWN OPENAI KEY
        messages=[
            {
                "role": "system",
                "content": "You are a helpful but terse AI assistant who gets straight to the point.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response