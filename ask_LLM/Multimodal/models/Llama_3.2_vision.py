import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
from langchain_ollama import OllamaLLM


import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../tools")))
from config import load_env_vars
from processing import process_questions


if __name__ == '__main__':

    LLMmodel = OllamaLLM(
        model = "llama3.2-vision",
        temperature = 0.7,
    )

    paths = {
    "error_log_path": load_env_vars().get("ErrorLogPath") + "Llama/Llama_3.2_vision_ErrorLog.json",
    "zeroshot_path": load_env_vars().get("cot_path") + "Llama/Llama_3.2_vision_zeroshot.json",
    "fewshot_path": load_env_vars().get("cot_path") + "Llama/Llama_3.2_vision__fewshot.json",
    "dataset_path": load_env_vars().get("dataset"),
    }

    process_questions(LLMmodel, paths)





