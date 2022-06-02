import requests


class ProposalApi(object):
    def proposal_api(self,url,headers,params):
        url = url
        headers = headers
        params = params
        r = requests.get(url=url, headers=headers, params=params)
        return r


if __name__ == '__main__':
    ProposalApi.proposal_api(1)
