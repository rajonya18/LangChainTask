The code in analyze_text.txt implements the task specified in LangChain Agent Task.docx


**Instructions to run the code:**

To run the code for the first time after cloning the repository, you need to install the necessary packages using:
    pip install requirements.txt

Run the code using:
    python3 analyze_text.py


**Prompt format:**

The user should always specify the instruction (eg, summarize the text) at the beginning followed by a colon(:). After that, the user should copy the passage of text on which he wants the instruction to be performed. 
The prompt should look like - "_Instruction : Target Text_"


**Input Output Format:**

For convenience of keeping a track record of inputs and corresponding outputs, we are required to store the user prompt in a txt file and provide the path of this txt file upon being prompted in the terminal. (This can be changed to accept prompts from the terminal very easily). An output_latest.txt file corresponding to the input file will be stored in the Sample_In_Out folder. We can then match the corresponding input and output files.

Some previously executed test samples have already been included in the Sample_In_Out folder


**Limitation:**

If the prompt differs from the format "_Instruction : Target Text_", then our implementation will fail. This is because although we use LLM Agent to find out the intent of the user from the prompt, the parsing of the Target Text from the prompt is still done using rule-based logic which makes the above format necessay.

Using an LLM Chain to separate the Instruction and Target Text from the prompt (as a prepocessing step) was tried out. It was observed that although the user's intent could still be found out correctly, the parsed Target Text often had slight modifications in them. (For eg, the text "It is very sunny. It is very hot" might be modified by the LLM Chain to "It is very sunny and hot"). While such small modifications would not hamper the summarization task, they would lead to incorrect token counts and also incorrect headings (in case the headings were also modified slightly). To avoid these edge cases, we could not use an LLM Agent for parsing. 

_Note_: Parsing is the only part of the implementation that does not use LLM Chains. All other tasks like understanding the intent of the user, summarizing, counting tokens, etc are done with Chains. 




