import os
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI

class LangChainAgent:
    def __init__(self, api_key, model_name="gemini-2.0-flash"):

        # set google API key
        os.environ["GOOGLE_API_KEY"] = api_key

        # load the dataset once
        self.df = pd.read_excel("student-data.xlsx")

        # build dataset context string for LLM
        self.dataset_context = self.build_dataset_context()

        # initialize model
        self.model = ChatGoogleGenerativeAI(
            model=model_name,
            api_key=api_key
        )

    # ---------------------------------------------------------
    # Build dataset summary context
    # ---------------------------------------------------------
    def build_dataset_context(self):
        preview = self.df.head().to_string()
        columns = ", ".join(self.df.columns)
        row_count = len(self.df)

        return f"""
Rows: {row_count}
Columns: {columns}

Preview:
{preview}
        """

    # ---------------------------------------------------------
    # Main run function
    # ---------------------------------------------------------
    def run(self, user_input):

        # Build prompt for LLM
        prompt = f"""
You are an AI assistant that:
- Greets the user naturally.
- Understands questions about the dataset.
- Returns *either* a greeting OR a pandas data instruction.

RULES:
1. If the user says hello/hi/hey/etc → reply with:
   GREET: <your friendly greeting>

2. If the question CAN be answered using the dataset:
   Output:
   ACTION: <explanation for pandas>

3. If the question CANNOT be answered from dataset:
   Output ONLY:
   NOT_ANSWERABLE

### DATASET:
{self.dataset_context}

### USER QUESTION:
{user_input}

### OUTPUT FORMAT:
- GREET: <text>
- ACTION: <text>
- NOT_ANSWERABLE
"""

        # LLM response
        result = self.model.invoke(prompt)
        output = result.content.strip()

        # -------------------
        # 1. GREETING
        # -------------------
        if output.startswith("GREET:"):
            return output.replace("GREET:", "").strip()

        # -------------------
        # 2. NOT ANSWERABLE
        # -------------------
        if "NOT_ANSWERABLE" in output:
            return "Sorry, I could not find this information in the dataset."

        # -------------------
        # 3. ACTION
        # -------------------
        if output.startswith("ACTION:"):
            instruction = output.replace("ACTION:", "").strip()
            return self.execute_instruction(instruction)

        # -------------------
        # 4. Unexpected output
        # -------------------
        return "Sorry, I couldn't understand the request."

    # ---------------------------------------------------------
    # Execute dataset logic
    # ---------------------------------------------------------
    def execute_instruction(self, instruction):
        """
        The LLM gives natural-language instructions like:
        'Find the student with the highest marks in Math.'

        This function converts common instructions into pandas logic.
        """

        instr = instruction.lower()

        # --------------------------
        # Find highest scorer
        # --------------------------
        if "highest" in instr or "top" in instr:
            for col in self.df.columns:
                if col.lower() in instr:
                    top_row = self.df.loc[self.df[col].idxmax()]
                    return f"Highest {col} scorer:\n{top_row.to_string()}"

            # if no specific column given, try total score
            if "total" in self.df.columns:
                top_row = self.df.loc[self.df["total"].idxmax()]
                return "Top student (by total score):\n" + top_row.to_string()

            return "I could not identify the subject to compute highest score."

        # --------------------------
        # Lowest scorer
        # --------------------------
        if "lowest" in instr or "least" in instr:
            for col in self.df.columns:
                if col.lower() in instr:
                    low_row = self.df.loc[self.df[col].idxmin()]
                    return f"Lowest {col} scorer:\n{low_row.to_string()}"

            return "I could not identify the subject to compute lowest score."

        # --------------------------
        # Average of a column
        # --------------------------
        if "average" in instr or "mean" in instr:
            for col in self.df.columns:
                if col.lower() in instr:
                    value = self.df[col].mean()
                    return f"Average {col}: {value}"

            return "I could not identify which column to calculate the average."

        # --------------------------
        # Count rows
        # --------------------------
        if "how many" in instr or "count" in instr:
            return f"Number of records: {len(self.df)}"

        # --------------------------
        # Column listing
        # --------------------------
        if "column" in instr or "structure" in instr:
            return f"Available columns:\n{', '.join(self.df.columns)}"

        # fallback
        return "I understood the question but cannot execute it with current rules."
