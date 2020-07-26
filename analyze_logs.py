from reader import IReader
from reader.csv_reader import CSVReader
from reader.schema import CsvLog
from entity.subject import RequestLog
from entity.metrics_manager import RequestMetricsManager
from entity.subject_data import RequestUrlMethodData
from entity import IMetricsManager
from utils.url import mask
from utils.nlargest import nlargest
from writer.stdout import ConsoleWriter


class SubjectFactory(object):
    def _get_request_log(record):
        return RequestLog(
            timestamp=record["timestamp"],
            response_time=record["response_time"],
            response_code=record["response_code"],
            url=mask(record["url"]),
            method=record["method"],
        )

    _choice = {"REQUEST_LOGS": _get_request_log}

    def create(self, type, record):
        return self._choice[type](record=record)


class AggregatedResultsFactory(object):
    def _get_request_agg_results(metrics_manager):
        return [
            {
                "url": metrics_manager.metrics_map[key].subject_data.url,
                "method": metrics_manager.metrics_map[key].subject_data.method,
                "avg_response_time": metrics_manager.metrics_map[
                    key
                ].metrics_data.get_average_response_time(),
                "min_response_time": metrics_manager.metrics_map[
                    key
                ].metrics_data.get_min_response_time(),
                "max_response_time": metrics_manager.metrics_map[
                    key
                ].metrics_data.get_max_response_time(),
                "frequency": metrics_manager.metrics_map[
                    key
                ].metrics_data.get_frequency(),
            }
            for key in metrics_manager.metrics_map
        ]

    _choice = {"REQUEST_LOGS": _get_request_agg_results}

    def create(self, type, metrics_manager):
        return self._choice[type](metrics_manager=metrics_manager)


def analyzer(
    reader: IReader,
    metrics_manager: IMetricsManager,
    subject_type="REQUEST_LOGS",
    top_results_key="frequency",
    top_res_count=5,
):
    records = reader.read()
    for record in records:
        subject = SubjectFactory().create(subject_type, record)
        metrics_manager.update_metrics(subject=subject)

    agg_results = AggregatedResultsFactory().create(subject_type, metrics_manager)
    top_results = nlargest(top_res_count, agg_results, top_results_key)

    return agg_results, top_results


if __name__ == "__main__":
    reader = CSVReader(schema=CsvLog)
    metrics_manager = RequestMetricsManager(subject_data_cls=RequestUrlMethodData)
    agg_results, top_results = analyzer(reader=reader, metrics_manager=metrics_manager)
    ConsoleWriter(
        first_line="Time taken for each endpoint:",
        col_order=[
            "method",
            "url",
            "min_response_time",
            "max_response_time",
            "avg_response_time",
        ],
        col_name_dict={
            "method": "METHOD",
            "url": "URL",
            "min_response_time": "Min Time",
            "max_response_time": "Max Time",
            "avg_response_time": "Average Time",
        },
    ).write(agg_results)

    ConsoleWriter(
        first_line=f"Top 5 highest throughput URLs:",
        col_order=["method", "url", "frequency"],
        col_name_dict={"method": "METHOD", "url": "URL", "frequency": "Frequency"},
    ).write(top_results)
