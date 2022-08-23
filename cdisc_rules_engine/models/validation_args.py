from typing import Literal


class ValidationArgs:
    def __init__(
        self,
        cache: str,
        pool_size: int,
        data: str,
        log_level: str,
        report_template: str,
        standard: str,
        version: str,
        controlled_terminology_package: str,
        output: str,
        output_format: str,
        raw_report: bool,
        define_version: str,
        include_rules: str,
        exclude_rules: str,
        whodrug: str,
        meddra: str,
    ):
        self.cache = cache
        self.pool_size = pool_size
        self.data = data
        self.log_level = log_level
        self.report_template = report_template
        self.standard = standard
        self.version = version
        self.controlled_terminology_package = controlled_terminology_package
        self.output = output
        self.output_format = output_format
        self.raw_report = raw_report
        self.define_version = define_version
        self.include_rules = include_rules
        self.exclude_rules = exclude_rules
        self.whodrug = whodrug
        self.meddra = meddra
