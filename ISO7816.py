# ISO-7816 High Level Analyzer

from saleae.analyzers import HighLevelAnalyzer, AnalyzerFrame, StringSetting, NumberSetting, ChoicesSetting


class Hla(HighLevelAnalyzer):
    # List of settings
    Decode_level = ChoicesSetting(choices=('character', 'APDU', 'TPDU'))

    # List of produced types
    result_types = {
        'char': {
            'format': 'Output type: {{type}}, Input type: {{data.input_type}}'
        }
    }

    def __init__(self):
        pass

    def get_capabilities(self):
        pass

    def set_settings(self, settings):
        pass

    def decode(self, frame: AnalyzerFrame):

        # Return the data frame itself
        return AnalyzerFrame('char', frame.start_time, frame.end_time, {
            'input_type': frame.type
        })
