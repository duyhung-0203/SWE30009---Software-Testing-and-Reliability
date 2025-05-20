import os
from tabulate import tabulate
from language_tool_python import LanguageTool

# Initialize LanguageTool for grammar and spell checking
tool = LanguageTool('en-US')

# Define 20 mutants
def mutant_1(text): return text  # Skip grammar checking completely
def mutant_2(text): return tool.correct(text)[:5]  # Limit to first 5 corrections
def mutant_3(text): return tool.correct(text).upper()  # Convert corrections to uppercase
def mutant_4(text): return tool.correct(text).replace(" ", "")  # Remove all spaces
def mutant_5(text): return tool.correct(text).rstrip()  # Ignore trailing spaces
def mutant_6(text): return tool.correct(text) + " XYZ"  # Add random characters at the end
def mutant_7(text): return tool.correct(text)[::-1]  # Reverse corrected text
def mutant_8(text): return tool.correct(text).replace(".", "")  # Remove punctuation
def mutant_9(text): return tool.correct(tool.correct(text))  # Apply double corrections
def mutant_10(text): return tool.correct(text)[:-1] + "?"  # Introduce a typo at the end
def mutant_11(text): return tool.correct(text)[:100]  # Limit output length to 100 characters
def mutant_12(text): return " ".join(word + " " for word in tool.correct(text).split())  # Add redundant spaces
def mutant_13(text): return tool.correct(text).replace("grammar", "syntax")  # Replace grammar corrections
def mutant_14(text): return " ".join(tool.correct(text).split()[::-1])  # Reverse word order
def mutant_15(text): return tool.correct(text).replace("test", "exam")  # Replace specific word
def mutant_16(text): return tool.correct(text).replace("sentence", "line")  # Replace another word
def mutant_17(text): return "   " + "    ".join(text.split()) + "   "  # Add excessive spaces
def mutant_18(text): return tool.correct(text) + " This is random."  # Add random sentence
def mutant_19(text): return tool.correct(text).lower()  # Convert corrections to lowercase
def mutant_20(text): return tool.correct(text).replace("spelling", "orthography")  # Replace specific word

# Mutants list
mutants = [
    mutant_1, mutant_2, mutant_3, mutant_4, mutant_5,
    mutant_6, mutant_7, mutant_8, mutant_9, mutant_10,
    mutant_11, mutant_12, mutant_13, mutant_14, mutant_15,
    mutant_16, mutant_17, mutant_18, mutant_19, mutant_20
]

# Define test cases for Metamorphic Relations
test_cases = [
    {
        "description": "MR1: Case Sensitivity (Uppercase)",
        "input": "THIS IS A TEST SENTENCE.",
        "expected_output": tool.correct("This is a test sentence."),
    },
    {
        "description": "MR1: Case Sensitivity (Lowercase)",
        "input": "this is a test sentence.",
        "expected_output": tool.correct("This is a test sentence."),
    },
    {
        "description": "MR2: Redundant Whitespace",
        "input": "   This    is   a    test   sentence   .  ",
        "expected_output": tool.correct("This is a test sentence."),
    },
]

# Function to test mutants for a specific test case
def test_mutants(mr_description, test_input, expected_output, mutants):
    table = []
    original_output = tool.correct(test_input)
    
    for i, mutant in enumerate(mutants, 1):
        try:
            mutant_output = mutant(test_input)
            detected = "Yes" if mutant_output != original_output else "No"
            status = "Kill" if mutant_output != expected_output else "Survived"
            table.append([f"mut{i}", original_output, expected_output, mutant_output, detected, status])
        except Exception as e:
            table.append([f"mut{i}", original_output, expected_output, str(e), "Error", "Error"])
    
    # Print results for the test case
    print(f"\nResults for {mr_description}:")
    headers = ["Mutant", "Original Output", "Expected Output", "Mutant Output", "Detected", "Status"]
    print(tabulate(table, headers=headers, tablefmt="grid"))

# Execute tests for each test case
for case in test_cases:
    test_mutants(case["description"], case["input"], case["expected_output"], mutants)
