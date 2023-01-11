import iperf_parser

class TestSiute():
  def test_iperf3_client_connection(self, client):
    output = client
    parsed_json = iperf_parser.parse(output)
    
    assert not parsed_json.get("error", None), parsed_json["error"]

    for interval in parsed_json["intervals"]:
      transfer = round(interval["sum"]["bytes"] / 1024, 2)
      bitrate = round(interval["sum"]["bits_per_second"] / 1000, 2)
      assert transfer > 2 and bitrate > 20
