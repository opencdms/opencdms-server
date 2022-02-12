required_role_lookup = {
    "climsoft-users": {
        "post": {"ClimsoftAdmin"},
        "get": {"ClimsoftAdmin"},
        "put": {"ClimsoftAdmin"},
        "delete": {"ClimsoftAdmin"}
    },
    "file-upload/image": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "s3/image": {
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"}
    },
    "acquisition-types": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "data-forms": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "fault-resolutions": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "feature-geographical-positions": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "flags": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "instruments": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftOperator"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"}
    },
    "instrument-fault-reports": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"}
    },
    "instrument-inspections": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"}
    },
    "obselements": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "observation-finals": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftOperator"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftOperator"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftOperator"}
    },
    "observation-initials": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftQC", "ClimsoftOperator", "ClimsoftOperatorSupervisor"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftQC", "ClimsoftOperator", "ClimsoftOperatorSupervisor"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftQC", "ClimsoftOperator", "ClimsoftOperatorSupervisor"}
    },
    "obs-schedule-class": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "paper-archives": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "paper-archive-definitions": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "physical-features": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "physical-feature-class": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "qc-status-definitions": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftQC"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftQC"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftQC"}
    },
    "qc-types": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftQC"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftQC"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftQC"}
    },
    "reg-keys": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    },
    "stations": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"}
    },
    "station-elements": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"}
    },
    "station-location-histories": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"}
    },
    "station-qualifiers": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata"}
    },
    "synop-features": {
        "post": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "get": {"ClimsoftAdmin", "ClimsoftDeveloper", "ClimsoftMetadata", "ClimsoftOperator",
                "ClimsoftOperatorSupervisor", "ClimsoftProducts", "ClimsoftQC", "ClimsoftRainfall", "ClimsoftRainfall"},
        "put": {"ClimsoftAdmin", "ClimsoftDeveloper"},
        "delete": {"ClimsoftAdmin", "ClimsoftDeveloper"}
    }
}
