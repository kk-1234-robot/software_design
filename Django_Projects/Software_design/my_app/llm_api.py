from openai import OpenAI


# 通过API调用模型，实现中文翻译成英文
def translate_by_api(content):
    client = OpenAI(
        api_key="sk-jFLjtbqJgKldg4wT6DQFXu4pymFwviTRNk34w51YOUTdYeFh",
        base_url="https://api.moonshot.cn/v1",
    )

    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system", "content": "请将下列中文翻译成英文："},
            {"role": "system", "content": "回答时只回复英文翻译结果"},
            {"role": "user", "content": content}
        ],
        temperature=0,
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


# 通过API调用模型，实现词性标注
def annotation_pos_by_api(content):
    client = OpenAI(
        api_key="sk-jFLjtbqJgKldg4wT6DQFXu4pymFwviTRNk34w51YOUTdYeFh",
        base_url="https://api.moonshot.cn/v1",
    )

    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system", "content": "判断以下词是名词、动词、形容词、副词、代词、或都不是"},
            {"role": "system",
             "content": "不同种类对应的回答格式为名词--'n',动词--'v',形容词--'adj',副词--'adv',代词--'pron',都不是--'other'"},
            {"role": "user", "content": content}
        ],
        temperature=0,
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


# 通过API调用模型，实现实体标注
def annotation_entity_by_api(content):
    client = OpenAI(
        api_key="sk-jFLjtbqJgKldg4wT6DQFXu4pymFwviTRNk34w51YOUTdYeFh",
        base_url="https://api.moonshot.cn/v1",
    )

    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system", "content": "判断以下词是句子中的时间、人物、地点、或其他"},
            {"role": "system",
             "content": "不同种类对应的回答格式为时间--'time',人物--'person',地点--'location',其他--'other"},
            {"role": "user", "content": content}
        ],
        temperature=0,
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content
