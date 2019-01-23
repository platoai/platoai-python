from __future__ import print_function

import datetime
from pprint import pprint

import voxjar

if __name__ == "__main__":
    metadata = {
        "identifier": "test_call_identifier",
        "timestamp": datetime.datetime.now(),
        # 'company': {
        #     'id': 'b87cc8ea-6820-11e7-891e-4f389aefc782'
        # },
        "type": {
            "identifier": "test_call_type_identifier",
            "name": "test_call_type_name",
        },
        "agents": [
            {
                "identifier": "test_agent_identifier",
                "name": "test_agent_name",
                "phoneNumber": 1234567890,
            }
        ],
        "customers": [
            {
                "identifier": "test_customer_identifier",
                "name": "test_customer_name",
                "phoneNumber": 9876543210,
            }
        ],
        "direction": "OUTGOING",
        "options": {"processAudio": True},
    }

    with open("./test.mp4", "rb") as f:
        client = voxjar.Client()
        try:
            pprint(client.push(metadata, audio=f))
        except RuntimeError as e:
            print(e)
