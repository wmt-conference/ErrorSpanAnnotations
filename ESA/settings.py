raise Exception("This code uses old loader, please refactor.")
PROJECT = "GEMBA" # used for Vilem's and Tom's side project
#PROJECT = "ESA" # used for WMT ESA protocol


methods = {
    "esa": {
        "name": "ESA"
    },
    "esa_severity": {
        "name": "ESA (severities)"
    },
    "mqm": {
        "name": "MQM"
    },
    "wmt-dasqm": {
        "name": "DA+SQM (WMT23)"
    },
    "wmt-mqm": {
        "name": "MQM (WMT23)"
    },
    "gemba_severity": {
        "name": r"ESA$^\mathrm{AI}$ (severities)"
    },
    "gemba": {
        "name": r"ESA$^\mathrm{AI}$"
    },
    "llm": {
        "name": "GEMBA (no humans)"
    },
}

