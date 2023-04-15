from lcu_connector import Connector


def request_test() -> None:
    conn = Connector()
    conn.start()
    summoner = None
    if conn.connected:
        summoner = conn.get('/lol-summoner/v1/current-summoner')
        summoner = summoner.json()
    assert summoner is not None
