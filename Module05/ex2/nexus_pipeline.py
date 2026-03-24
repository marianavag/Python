from typing import Protocol, Any, List, Dict, Union
from abc import ABC, abstractmethod
import json

class InputStage:
    def process(self, data: Any) -> Any:
        print("Stage 1: Input validation and parsing")
        if data is None:
            raise ValueError("Invalid data: Input is empty")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        print("Stage 2: Data transformation and enrichment")
        return f"Processed {data}"


class OutputStage:
    def process(self, data: Any) -> Any:
        print("Stage 3: Output formatting and delivery")
        return data


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[Any] = []
    
    def add_stage(self, stage: Any) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass
