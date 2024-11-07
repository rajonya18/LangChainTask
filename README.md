The code in analyze_text.txt implements the task specified in LangChain Agent Task.docx


Instructions to run the code:

To run the code for the first time, you need to install the necessary packages using:
    pip install requirements.txt

Run the code using:
    python3 analyze_text.py



Prompt format: 
The user should always specify the instruction (summarize, count tokens or extract titles) in his own words at the beginning followed by a colon(:). After that, the user should copy the passage of text on which he wants the operations to be performed. 
The prompt should look like - "Instruction : Target Text"


Input Output Format:

For convenience of keeping records of input and corresponding outputs, we are required to store the user prompt in a txt file and provide the path of this txt file upon being prompted in the terminal. (This can be changed to accept prompts from the terminal very easily). An output file correspong to the input file will be stored in the Sample_In_Out folder. We can then match the corresponding input and output files.

 

Some previously executed test samples have already been included in the Sample_In_Out folder




