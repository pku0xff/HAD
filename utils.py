import re
from prompt_templates import *


def format_prompt(data_item, prompt_template=BASE_PROMPT_TEMPLATE, response_template=BASE_RESPONSE_TEMPLATE):
    prompt = prompt_template.format(
        task_input=data_item["task_input"],
        task_output=data_item["task_output"],
    )
    response = response_template.format(
        hallucination_type=data_item["hallucination_type"],
        hallucination_span=data_item["hallucination_span"],
        correction=data_item["correction"],
    )
    return {"prompt_id": data_item["id"], "prompt": prompt, "response": response}


def parse_response(response_text):
    if type(response_text) == list:
        response_text = response_text[0]
    results = {}

    hallucination_type = re.search(
        r"(?<=\*\*Hallucination Type:\*\*)(.*?)(?=\*\*Hallucination Span:\*\*)",
        response_text,
        re.DOTALL,
    )
    if hallucination_type:
        results["hallucination_type"] = hallucination_type.group().strip()
    else:
        # print(response_text)
        hallucination_type = re.search(
            r"(?<=\*\*Hallucination Label:\*\*)(.*?)(?=\*\*Hallucination Span:\*\*)",
            response_text,
            re.DOTALL,
        )
        if hallucination_type:
            results["hallucination_type"] = hallucination_type.group().strip()
        else:
            results["hallucination_type"] = ""

    hallucination_span = re.search(
        r"(?<=\*\*Hallucination Span:\*\*)(.*?)(?=\*\*Correction:\*\*)",
        response_text,
        re.DOTALL,
    )
    if hallucination_span:
        results["hallucination_span"] = hallucination_span.group().strip()
    else:
        # print(response_text)
        results["hallucination_span"] = ""
    correction = re.search(r"(?<=\*\*Correction:\*\*)(.*)", response_text, re.DOTALL)
    if correction:
        results["correction"] = correction.group().strip()
    else:
        results["correction"] = ""

    return results
