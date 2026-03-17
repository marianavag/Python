from typing import Any, List, Dict, Optional, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [
            item for item in data_batch
            if isinstance(item, str) and criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"id": self.stream_id, "status": "active"}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.count = 0
        self.last_avg = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            nbr_batch = [
                float(item.split(":")[1])
                for item in data_batch
                if isinstance(item, str) and item.startswith("temp:")
                ]
            if not nbr_batch:
                return "No valid sensors to process."
            avg = sum(nbr_batch) / len(nbr_batch)
            self.last_avg = avg
            self.count += len(nbr_batch)
            return f"Sensor analysis: {len(data_batch)} readings processed, avg temp: {avg}°C"
        except Exception as e:
            return f"Error during processing: {e}"
    
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return [item for item in data_batch
                if isinstance(item, str) and item.startswith(f"{criteria}:")]

    def get_stats(self) -> Dict[str, str | int | float]:
        return {
            "id": self.stream_id,
            "total_readings": self.count,
            "average_temp": self.last_avg,
            "unit": "Celsius"
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.count = 0
        self.balance = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            buy_batch = [
                float(item.split(":")[1])
                for item in data_batch
                if "buy:" in item
            ]
            sell_batch = [
                float(item.split(":")[1])
                for item in data_batch
                if "sell:" in item
            ]
            if not buy_batch or sell_batch:
                return "No valid transactions to process."
            net_flow = sum(buy_batch) - sum(sell_batch)
            self.count = len(data_batch)
            self.balance = net_flow
            return f"Transaction analysis: {len(data_batch)} operations, net flow: {net_flow:+} units"
        except Exception as e:
            return f"Error during processing: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return [item for item in data_batch
                if isinstance(item, str) and item.startswith(f"{criteria}:")]

    def get_stats(self) -> Dict[str, str | int | float]:
        return {
            "stream_id": self.stream_id,
            "total_op": self.count,
            "net_balance": self.balance,
        }


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            event_types = [
            item for item in data_batch
            if isinstance(item, str)
            ]
            if not event_types:
                return "No valid events to process."
            if "error" in event_types:
                severity = "high"
            elif "warning" in event_types:
                severity = "medium"
            else:
                severity = "low"
            self.last_severity = severity
            self.count += len(event_types)
            error_count = data_batch.count("error")
            return f"Event analysis: {len(event_types)} events, {error_count} error detected"
        except Exception as e:
            return f"Error during processing: {e}"
        
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return [item for item in data_batch
                if isinstance(item, str) and item == criteria]
    
    def get_stats(self) -> Dict[str, str | int | float]:
        return {
            "stream_id": self.stream_id,
            "total_log": self.count,
            "last_severity": self.last_severity
        }


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []
        self.batch_count = 0
    
    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)
    
    def process_all(self, all_batches: List[List[Any]]) -> List[str]:
        result = []
        index = 0
        while index < len(self.streams):
            curr_stream = self.streams[index]
            curr_batch = all_batches[index]
            text = curr_stream.process_batch(curr_batch)
            result.append(text)
            index += 1
        return result
    
    def get_all_stats(self) -> List[Dict[str, Any]]:
        all_stats = []
        index = 0
        while index < len(self.streams):
            curr_stream = self.streams[index]
            curr_stats = curr_stream.get_stats()
            all_stats.append(curr_stats)
            index += 1
        return all_stats
    
    def count_report(self, all_batches: List[List[Any]]) -> None:
        self.batch_count += 1
        results = self.process_all(all_batches)
        print(f"Batch {self.batch_count} Results:")
        for result in results:
            print(f"- {result}")

    def display_poly(self, all_batches: List[str]):
        print("=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...\n")
        self.count_report(all_batches)


if __name__ == "__main__":
    
