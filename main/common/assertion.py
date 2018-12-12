# def assertHTTPCode(response, codeList=None):
#      responseCode = response.status_code
#     if not codeList:
#         codeList = [200]


def assertHTTPCode(response, codeList = None):
    pass
    responseCode = response.status_code
    if not codeList:
        codeList=[200]
    if responseCode not in codeList:
        raise Exception('响应code不在列表中！')

