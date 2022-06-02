import unittest

from nose_parameterized import parameterized

from 获取指定提案详情.api.proposal_api import ProposalApi
from 获取指定提案详情.read_json.read_proposal import ReadJson


def get_i():
    data = ReadJson("proposal.json").read_proposal()
    arr = []
    for i in data.values():
        arr.append((i.get("url"),
                    i.get("headers"),
                    i.get("params"),
                    i.get("status_code")))
    return arr


class TestProposal(unittest.TestCase):
    @parameterized.expand(get_i())
    def test_proposal(self, url, headers, params, status_code):
        # url = "http://test.zaitakugeek.cn:8000/tender/info"
        # headers = {
        #     "Content-Type": "application/json",
        #     "Authorization": "Token 1c0edb0cf33e815a48e7f07a3461987cd0cffcb3"
        # }
        # params = {"tender_id": "111645522533090336"}
        r = ProposalApi().proposal_api(url, headers, params)
        print(r.json())
        try:
            self.assertEqual(status_code, r.status_code)
        except:
            raise


if __name__ == '__main__':
    unittest.main()
