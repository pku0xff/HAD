BASE_PROMPT_TEMPLATE = """### Instruction ###
Given a pair of task input and task output, your goal is to detect whether the task output contains any hallucination.
If a hallucination is present, specify the type of hallucination, identify the hallucination span, \
and provide the correct version of the output.

### Example ###
**Task Input:**
{task_input}

**Task Output:**
{task_output}

### Your Detection ###"""

BASE_RESPONSE_TEMPLATE = """**Hallucination Type:**
{hallucination_type}

**Hallucination Span:**
{hallucination_span}

**Correction:**
{correction}"""

BINARY_PROMPT_TEMPLATE = """### Instruction ###
Given a pair of task input and task output, your goal is to detect whether the task output contains any hallucination.
If a hallucination is present, identify the hallucination span and provide the correct version of the output.

### Example ###
**Task Input:**
{task_input}

**Task Output:**
{task_output}

### Your Detection ###"""

BINARY_RESPONSE_TEMPLATE = """**Hallucination Label:**
{hallucination_type}

**Hallucination Span:**
{hallucination_span}

**Correction:**
{correction}"""

BASELINE_PROMPT_TEMPLATE = """### Instruction ###
Given a pair of task input and task output, your goal is to detect whether the task output contains any hallucination.
If a hallucination is present, specify the type of hallucination based on the type description, identify the \
hallucination span, and provide the correct version of the output.

### Hallucination Type Description ###
Task Type Inconsistency: The generated output represents a different type of task than what was specified in the instruction. This does not include deviations within the same task type, such as violations of detailed requirements or specifications.
Task Requirement Inconsistency: The generated output does not align with the task requirements outlined in the instruction, including key aspects such as the expected format, length, subject matter, or tone. Note that this error stems from not following the task requirement, rather than from inconsistency with the input content.
Contradiction with Input Content: The generated output contradicts with the provided input content, presenting information or statements that are incompatible with the context given. This may result from a failure to accurately recall the input content, or from misunderstandings and confusion about the information provided.
Baseless Information: The generated output contains baseless information that are not supported by the input context, whereas the task requires the model to generate output that strictly adheres to the information provided in the input. Note that tasks seeking new information do not encounter this issue.
Information Omission: The generated output fails to include certain details or information present in the input, whereas the task requires the model\'s output to fully and accurately capture all the information provided in the input context.
Contradiction within Output Content: The generated content contains internal inconsistencies where statements directly oppose each other, or where the reasoning is logically flawed.
Structural Incoherence: The generated output contains redundant or repetitive statements that do not enhance the clarity or value of the content, or when the output is incomplete or disjointed. This does not apply instances where the incoherence is used purposefully for stylistic effect or rhetorical emphasis.
Factual Recall Error: The generated text contains incorrect atomic facts due to the model\'s inability to accurately recall or access relevant knowledge. Note that the inaccuracy is limited to a single atomic fact, rather than multiple facts.
Factual Inference Error: The generated content contains incomplete or misinterpreted facts. Common phenomena include confusion between different time periods, individuals, or events; omissions of critical conditions or contextual information; and errors in the logical sequence of events or processes. As a result, the model\'s reasoning appears to be based on seemingly factual information, but it ultimately leads to an erroneous or unreliable output.
Fabricated Entity: The generated content contains entirely new and fabricated entities that do not exist in the real world, including invented concepts, names, or objects that have no basis in reality or prior knowledge.
Fictional Attribution: The generated content fabricates information about real entities, including unverified or fabricated claims, statements, or quotes, which cannot be supported or directly refuted by established facts or reliable sources. Unlike the "fabricated entity" type, this error does not introduce entirely new entities.

### Example ###
**Task Input:**
Whats the big deal with the new AMD Ryzen CPU?

**Task Output:**
As stated on the comment above, Intel thoroughly dominated the desktop CPU market for way too long. Why you may ask? Let's rewind back to 2011, Intel just released their 2nd gen of core i3/i5/i7 CPUs and AMD needed to respond. AMD's response to the market is their Bulldozer line of CPUs, Bulldozer failed because it was made with too much emphasis on multi-core performance and as a result, Bulldozer CPU's single core performance were horrible. Combine that with the fact that most programs at the time did not support multi-core CPUs, AMD gave way for Intel. Fast forward to 2014 and Intel knew that AMD weren't a threat anymore, as a result Intel gotten lazy at generational improvements, causing them to \"milk\" the CPU market for time to come. Fast forward to the present and AMD needs to respond badly, and Zen is their last ditch effort at it. Zen was made with single core performance in mind and as a result, Zen is reported to have a 92% improvement in single core performance over Bulldozer, enough to put them in place with 5th generation core i3/i5/i7 CPUs. AMD needs Zen to succeed badly, because if they fail to meet their quota, AMD may never compete in the desktop CPU market ever again. We need Zen to succeed badly, not because of AMD's sake, but for the sake of competition in the CPU market.

**Hallucination Type:**
Factual Recall Error

**Hallucination Span:**
92%

**Correction:**
As stated on the comment above, Intel thoroughly dominated the desktop CPU market for way too long. Why you may ask? Let's rewind back to 2011, Intel just released their 2nd gen of core i3/i5/i7 CPUs and AMD needed to respond. AMD's response to the market is their Bulldozer line of CPUs, Bulldozer failed because it was made with too much emphasis on multi-core performance and as a result, Bulldozer CPU's single core performance were horrible. Combine that with the fact that most programs at the time did not support multi-core CPUs, AMD gave way for Intel. Fast forward to 2014 and Intel knew that AMD weren't a threat anymore, as a result Intel gotten lazy at generational improvements, causing them to \"milk\" the CPU market for time to come. Fast forward to the present and AMD needs to respond badly, and Zen is their last ditch effort at it. Zen was made with single core performance in mind and as a result, Zen is reported to have a 52% improvement in single core performance over Bulldozer, enough to put them in place with 5th generation core i3/i5/i7 CPUs. AMD needs Zen to succeed badly, because if they fail to meet their quota, AMD may never compete in the desktop CPU market ever again. We need Zen to succeed badly, not because of AMD's sake, but for the sake of competition in the CPU market.

### Example ###
**Task Input:**
How do limousine services bypass the open container laws?

**Task Output:**
Sometimes there's an exception in the laws regarding commercial type transports. California example:: No drinking: > 23221 >  No driver shall drink any alcoholic beverage while in a motor vehicle upon a highway.  No passenger shall drink any alcoholic beverage while in a motor vehicle upon a highway. No open containers: > 23223 >  No driver shall have in his or her possession, while in a motor vehicle upon a highway or on lands, as described in subdivision  of Section 23220, any bottle, can, or other receptacle, containing any alcoholic beverage that has been opened, or a seal broken, or the contents of which have been partially removed. ' Except when: > 23229 >  Except as provided in Section 23229.1, Sections 23221 and 23223 do not apply to passengers in any bus, taxicab, or limousine for hire licensed to transport passengers pursuant to the Public Utilities Code or proper local authority, or the living quarters of a housecar or camper. This of course doesn't mean you're entitled to drink in a commercial vehicle, just that it's allowed by law under certain circumstances.

**Hallucination Type:**
None

**Hallucination Span:**
None

**Correction:**
None

### Example ###
**Task Input:**
{task_input}

**Task Output:**
{task_output}"""
