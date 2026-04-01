from typing import Any, List, Dict, Optional, Union
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type

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
        super().__init__(stream_id, "Environmental Data")
        self.count = 0
        self.last_avg = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temp_batch = []
            for item in data_batch:
                if not isinstance(item, str):
                    print(f"'{item}' is invalid: item must be a string")
                    continue
                parts = item.split(":")
                if len(parts) != 2 or parts[1] == "":
                    print(f"'{item}' is format invalid: expected 'type:value'")
                    continue
                key, value_str = parts
                try:
                    value = float(value_str)
                except ValueError:
                    print(f"'{item}' is format invalid: value must be numeric")
                    continue
                if key == "temp":
                    try:
                        temp_batch.append(value)
                    except ValueError:
                        print(f"'{item}' is format invalid: "
                              f"value must be numeric")
                        continue
            self.count += len(data_batch)
            if not temp_batch:
                return (
                    f"Sensor analysis: {len(data_batch)} readings processed, "
                    f"No valid temperature to process."
                )
            avg = sum(temp_batch) / len(temp_batch)
            self.last_avg = avg
            return (
                f"Sensor analysis: {len(data_batch)} readings processed, "
                f"avg temp: {avg}°C"
            )
        except Exception as e:
            return f"Error during processing: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        if criteria == "high":
            alert_count = 0
            for item in data_batch:
                if isinstance(item, str):
                    pt = item.split(":")
                    if len(pt) == 2:
                        try:
                            v = float(pt[1])
                            t_a = pt[0] == "temp" and (v > 45 or v < 0)
                            h_a = pt[0] == "humidity" and (v > 70 or v < 20)
                            p_a = pt[0] == "pressure" and (v > 1015 or v < 980)
                            if t_a or h_a or p_a:
                                alert_count += 1
                        except ValueError:
                            continue
            if alert_count == 1:
                return ["1 critical sensor alert"]
            elif alert_count > 1:
                return [f"{alert_count} critical sensor alerts"]
            else:
                return ["No valid sensors in this type of priority"]
        if criteria != "high":
            return [
                item for item in data_batch
                if isinstance(item, str)
            ]
        return []

    def get_stats(self) -> Dict[str, str | int | float]:
        return {
            "id": self.stream_id,
            "total_readings": self.count,
            "average_temp": self.last_avg,
            "units": "readings",
            "batch_type": "Sensor"
        }


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")
        self.count = 0
        self.balance = 0.0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            buy_batch = []
            sell_batch = []
            for item in data_batch:
                if not isinstance(item, str):
                    print(f"'{item}' is invalid: item must be a string")
                    continue
                parts = item.split(":")
                if len(parts) != 2 or parts[1] == "":
                    print(f"'{item}' is format invalid: expected 'type:value'")
                    continue
                key, value_str = parts
                try:
                    value = int(value_str)
                except ValueError:
                    print(f"'{item}' is format invalid: value must be numeric")
                    continue
                if len(parts) == 2:
                    try:
                        value = int(parts[1])
                        if parts[0] == "buy":
                            buy_batch.append(value)
                        elif parts[0] == "sell":
                            sell_batch.append(value)
                    except ValueError:
                        continue
                else:
                    print(f"'{item}' is format invalid: expected 'type:value'")
                    continue
            if not buy_batch and not sell_batch:
                return "No valid transactions to process."
            net_flow = sum(buy_batch) - sum(sell_batch)
            self.count = len(data_batch)
            self.balance = net_flow
            return (
                f"Transaction analysis: {len(data_batch)} operations, "
                f"net flow: {net_flow:+} units"
            )
        except Exception as e:
            return f"Error during processing: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        alert_count = 0
        if criteria == "high":
            for item in data_batch:
                if isinstance(item, str):
                    parts = item.split(":")
                    if len(parts) == 2:
                        try:
                            value = float(parts[1])
                            if value > 150:
                                alert_count += 1
                        except ValueError:
                            continue
            if alert_count == 1:
                return [f"{alert_count} large transaction"]
            elif alert_count > 1:
                return [f"{alert_count} large transactions"]
            else:
                return ["No valid transactions"]
        if criteria != "high":
            return [
                item for item in data_batch
                if isinstance(item, str)
            ]
        return []

    def get_stats(self) -> Dict[str, str | int | float]:
        return {
            "stream_id": self.stream_id,
            "total_op": self.count,
            "net_balance": self.balance,
            "units": "operations",
            "batch_type": "Transaction"
        }


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")
        self.count = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            event_types = []
            for item in data_batch:
                if not isinstance(item, str) or item == "":
                    print(f"'{item}' is invalid: item must be a string")
                    continue
                if not item.isalpha():
                    print(f"'{item}' is not an event")
                    continue
                event_types.append(item)
            if not event_types:
                return "No valid events to process."
            self.count += len(event_types)
            error_count = event_types.count("error")
            return (
                f"Event analysis: {len(event_types)} events, "
                f"{error_count} error detected"
                )
        except Exception as e:
            return f"Error during processing: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        if criteria == "high":
            error_count = data_batch.count("error")
            if error_count > 1:
                return [f"{error_count} critical system errors"]
        if criteria != "high":
            return [
                item for item in data_batch
                if isinstance(item, str)
            ]
        return [item for item in data_batch
                if isinstance(item, str) and item == criteria]

    def get_stats(self) -> Dict[str, str | int | float]:
        return {
            "batch_type": "Event",
            "total_log": self.count,
            "units": "events",
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
        self.process_all(all_batches)
        print(f"Batch {self.batch_count} Results:")
        index = 0
        while index < len(self.streams):
            curr_stream = self.streams[index]
            curr_batch = all_batches[index]
            stats = curr_stream.get_stats()
            name = stats.get("batch_type", curr_stream.stream_type)
            unit = stats.get("units", "items")
            current_count = len(curr_batch)
            print(f"- {name} data: {current_count} {unit} processed")
            index += 1

    def process_filtered(self, all_batches: List[Any],
                         criteria: Optional[str] = None) -> None:
        if criteria == "high":
            print(f"\nStream filtering active: {criteria.capitalize()}-"
                  f"priority data only")
            filtered = []
            index = 0
            while index < len(self.streams):
                curr_stream = self.streams[index]
                curr_batch = all_batches[index]
                items = curr_stream.filter_data(curr_batch, criteria)
                filtered.extend(items)
                index += 1
            if filtered:
                print(f"Filtered results: {', '.join(filtered)}")
            else:
                print("Filtered results: None")
        elif criteria == "" or criteria is None:
            print("\nStream filtering inactive: showing all data")
            all_data = []
            index = 0
            while index < len(all_batches):
                all_data.extend(all_batches[index])
                index += 1
            print("All data: [" +
                  ", ".join(str(item) for item in all_data) +
                  "]")
        elif criteria != "high":
            print(f"\nStream filtering active: {criteria.capitalize()}-"
                  f"priority data only")
            all_data = []
            index = 0
            while index < len(all_batches):
                all_data.extend(all_batches[index])
                index += 1
            print(f"Filtered results: {all_data}")


def data_stream() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(
        "Processing sensor batch: [" +
        ", ".join(str(item) for item in sensor_batch) +
        "]"
    )
    try:
        result = sensor.process_batch(sensor_batch)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: {trans.stream_type}")
    trans_batch = ["buy:100", "sell:150", "buy:75"]
    print(
        "Processing transaction batch: [" +
        ", ".join(str(item) for item in trans_batch) +
        "]"
    )
    try:
        result = trans.process_batch(trans_batch)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    event_batch = ["login", "error", "logout"]
    print(
        "Processing event batch: [" +
        ", ".join(str(item) for item in event_batch) +
        "]"
    )
    try:
        result = event.process_batch(event_batch)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(trans)
    processor.add_stream(event)
    all_batches = [
        ["temp:48", "humidity:80"],
        ["buy:200", "sell:50", "buy:10", "sell:20"],
        ["login", "error", "logout"]
    ]
    try:
        processor.count_report(all_batches)
        processor.process_filtered(all_batches, "high")
    except Exception as e:
        print(f"Error: {e}")
    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
