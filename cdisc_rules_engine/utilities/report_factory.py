from typing import List
from cdisc_rules_engine.enums.report_types import ReportTypes
from cdisc_rules_engine.models.rule_validation_result import RuleValidationResult
from cdisc_rules_engine.models.validation_args import ValidationArgs
from cdisc_rules_engine.utilities.excel_report import ExcelReport
from cdisc_rules_engine.utilities.json_report import JsonReport
from cdisc_rules_engine.services.data_services.local_data_service import (
    LocalDataService,
)


class ReportFactory:
    """
    This class is a factory that creates reporting service depending on the output format.

    Constructor arguments:
    data_path -- path to the output file
    results -- list with rule results generated by the engine
    elapsed_time -- time spent on validation
    args -- CLI arguments for the validate command
    data_service -- instance of engine data service to read file contents
    """

    def __init__(
        self,
        data_path: str,
        results: List[RuleValidationResult],
        elapsed_time: float,
        args: ValidationArgs,
        data_service: LocalDataService,
    ):
        self._data_path = data_path
        self._results = results
        self._elapsed_time = elapsed_time
        self._args = args
        self._data_service = data_service

    def get_report_service(self):
        output_type = self._args.output_format.upper()
        if output_type == ReportTypes.XLSX.value:
            template = self._data_service.read_data(self._args.report_template, "rb")
            return ExcelReport(
                self._data_path,
                self._results,
                self._elapsed_time,
                self._args,
                template,
            )
        elif output_type == ReportTypes.JSON.value:
            return JsonReport(
                self._data_path,
                self._results,
                self._elapsed_time,
                self._args,
            )
