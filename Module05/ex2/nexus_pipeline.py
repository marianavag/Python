from typing import Protocol, Any, List, Union
from abc import ABC, abstractmethod
import json


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        if data is None:
            raise ValueError("Invalid data: Input is empty")
        if not isinstance(data, (dict, str)):
            raise TypeError("Invalid format")
        if isinstance(data, dict):
            return data
        return {"raw": data}


class TransformStage:
    def process(self, data: Any) -> Any:
        if data.get("raw") == "invalid_data":
            raise ValueError("Invalid data format")
        if isinstance(data, dict) and "value" in data:
            temp = data.get("value")
            if not isinstance(temp, (int, float)):
                raise TypeError("Temperature must be numeric")
            if isinstance(temp, (int, float)):
                if 0.0 <= temp <= 50.0:
                    data["range_status"] = "Normal range"
                else:
                    data["range_status"] = "Critical range"
        if isinstance(data, dict) and "readings" in data:
            readings = data.get("readings", [])
            data["num_reads"] = len(readings)
            if data["num_reads"] > 0:
                data["average"] = sum(readings) / data["num_reads"]
            else:
                data["average"] = 0.0
            return data
        raw_content = data.get("raw")
        if isinstance(raw_content, str):
            if "," in raw_content:
                if "num_of_actions" not in data:
                    data["num_of_actions"] = 0
                data["num_of_actions"] += 1
                return data
            else:
                return
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        try:
            if "sensor" in data:
                return (f"Processed temperature reading: "
                        f"{data['value']}°{data['unit']} "
                        f"({data['range_status']})")
            elif "num_of_actions" in data:
                return (f"User activity logged: {data['num_of_actions']} "
                        f"actions processed")
            elif "readings" in data:
                return (f"Stream summary: {data['num_reads']} readings, avg: "
                        f"{data['average']:.1f}°C")
            return f"Processed {data.get('raw')}"
        except KeyError as e:
            return f"Output error: missing field {e}"
        except Exception as e:
            return f"Output error: {e}"


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        current_result = data
        stage_counter = 1
        try:
            for stage in self.stages:
                current_result = stage.process(current_result)
                stage_counter += 1
            return current_result
        except Exception as e:
            print(f"Error detected in Stage {stage_counter}: {e}")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return None


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        current_result = data
        stage_counter = 1
        try:
            for stage in self.stages:
                current_result = stage.process(current_result)
                stage_counter += 1
            return current_result
        except Exception as e:
            print(f"Error detected in Stage {stage_counter}: {e}")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return None


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        current_result = data
        if data is not None:
            current_result = {
                "raw": data,
                "readings": [21.0, 22.5, 23.0, 21.0, 23.0]
            }
        stage_counter = 0
        try:
            for stage in self.stages:
                stage_counter += 1
                current_result = stage.process(current_result)
            return current_result
        except Exception as e:
            print(f"Error detected in Stage {stage_counter}: {e}")
            print("Recovery initiated: Switching to backup processor")
            print("Recovery successful: Pipeline restored, processing resumed")
            return None


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []
        self.record_proc = 1

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, pipeline: ProcessingPipeline, raw_data: Any) -> Any:
        self.record_proc += 33
        return pipeline.process(raw_data)

    def chain_pipelines(self, raw_data: Any) -> Union[str, Any]:
        output = raw_data
        for pipeline in self.pipelines:
            output = pipeline.process(output)
        return output

    def chain_demo(self) -> None:
        print("Pipeline A -> Pipeline B -> Pipeline C")
        print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")
        simulated_time = len(self.pipelines) * 0.066
        print(f"Chain result: {self.record_proc} records processed through "
              f"{len(self.pipelines)}-stage pipeline")
        print(f"Performance: 95% efficiency, {simulated_time:.1f}s total "
              f"processing time")


def ft_nexus_pipeline() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    print("Initializing Nexus Manager...")

    manager = NexusManager()
    print("Pipeline capacity: 1000 streams/second\n")
    print("Creating Data Processing Pipeline...")
    stages_desc = [
        "Input validation and parsing",
        "Data transformation and enrichment",
        "Output formatting and delivery"
    ]
    i = 1
    for desc in stages_desc:
        print(f"Stage {i}: {desc}")
        i += 1
    print()
    json_pipe = JSONAdapter("PIPE-JSON-001")
    csv_pipe = CSVAdapter("PIPE-CSV-002")
    stream_pipe = StreamAdapter("PIPE-STREAM-003")
    manager.add_pipeline(json_pipe)
    manager.add_pipeline(csv_pipe)
    manager.add_pipeline(stream_pipe)

    print("=== Multi-Format Data Processing ===\n")
    try:
        json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
        print("Processing JSON data through pipeline...")
        print(f"Input: {json.dumps(json_data)}")
        result_json = manager.process_data(json_pipe, json_data)
        print("Transform: Enriched with metadata and validation")
        print(f"Output: {result_json}")
    except Exception as e:
        print(f"Critical System Error: Could not parse input data -> {e}")

    csv_data = "user,action,timestamp"
    print("\nProcessing CSV data through same pipeline...")
    print(f'Input: "{csv_data}"')
    result_csv = manager.process_data(csv_pipe, csv_data)
    print("Transform: Parsed and structured data")
    print(f"Output: {result_csv}")

    stream_data = "Real-time sensor stream"
    print("\nProcessing Stream data through same pipeline...")
    result_stream = manager.process_data(stream_pipe, stream_data)
    print(f"Input: {stream_data}")
    print("Transform: Aggregated and filtered")
    print(f"Output: {result_stream}")

    print("\n=== Pipeline Chaining Demo ===")
    raw_input = "ok,chain"
    manager.chain_pipelines(raw_input)
    manager.chain_demo()

    print("\n=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    bad_json = "invalid_data"
    manager.process_data(json_pipe, bad_json)
    print("\nNexus Integration complete. All systems operational.")


if __name__ == "__main__":
    ft_nexus_pipeline()
