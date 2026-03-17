from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    show_validation = True

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if not data:
                return False
            for item in data:
                item + 0
            return True
        except TypeError:
            print("Validation Error: Found non-numeric data.")
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid numeric data"
        if DataProcessor.show_validation:
            print("Validation: Numeric data verified")
        try:
            total = 0
            count = 0
            for nbr in data:
                total += nbr
                count += 1
            avg = total / count
            return f"Processed {count} numeric values, sum={total}, avg={avg}"
        except Exception as e:
            return f"Error during processing: {e}"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            if not data:
                return False
            data + ''
            return True
        except TypeError:
            print("Validation Error: Found non-text data.")
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid text data"
        if DataProcessor.show_validation:
            print("Validation: Text data verified")
        try:
            chr_count = 0
            for char in data:
                chr_count += 1
            words = data.split()
            wrd_count = 0
            for word in words:
                wrd_count += 1
            return f"Processed text: {chr_count} characters, {wrd_count} words"
        except Exception as e:
            return f"Error during processing: {e}"

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        try:
            text = data + ''
            if ":" not in text:
                print("Validation Error: Found non-log data.")
                return False
            level = text.split(":", 1)[0].strip().upper()
            if level not in ["ERROR", "INFO"]:
                print("Validation Error: Found non-log data.")
                return False
            return True
        except TypeError:
            print("Validation Error: Found non-log data.")
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "Error: Invalid log format"
        try:
            parts = data.split(":", 1)
            level = parts[0].strip().upper()
            message = parts[1].strip()
            if level and message:
                if DataProcessor.show_validation:
                    print("Validation: Log entry verified")
                return f"{level}|{message}"
            else:
                print("Validation Error: Found non-log data.")
                return "Error: Incomplete log entry"
        except Exception as e:
            return f"Error: {e}"

    def format_output(self, result: str) -> str:
        try:
            level = "Unknown"
            message = result
            if "|" in result:
                parts = result.split("|")
                level = parts[0]
                message = parts[1]
            else:
                level = "ERROR"
                message = result
            if level == "ERROR":
                prefix = "[ALERT]"
            else:
                prefix = "[INFO]"
            return f"Output: {prefix} {level} level detected: {message}"
        except Exception as e:
            return f"Error: {e}"


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    num_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_proc = NumericProcessor()
    result = num_proc.process(num_data)
    print(num_proc.format_output(result))

    print("\nInitializing Text Processor...")
    text_data = "Hello Nexus World"
    print(f'Processing data: "{text_data}"')
    text_proc = TextProcessor()
    result = text_proc.process(text_data)
    print(text_proc.format_output(result))

    print("\nInitializing Log Processor...")
    log_data = "ERROR: Connection timeout"
    print(f"Processing data: {log_data}")
    log_proc = LogProcessor()
    result = log_proc.process(log_data)
    print(log_proc.format_output(result))

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")
    DataProcessor.show_validation = False
    all_data = [
        (NumericProcessor(), [1, 2, 3]),
        (TextProcessor(), "Hello World!"),
        (LogProcessor(), "INFO: System ready")
    ]
    count = 1
    for proc, data in all_data:
        result = proc.process(data)
        if "|" in result:
            formatted = proc.format_output(result)
            print(f"Result {count}: {formatted[8:]}")
        else:
            print(f"Result {count}: {result}")
        count += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")
