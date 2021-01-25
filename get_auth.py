import requests
import json

# user name = Deerio
# password = UpperLower
auth_code = "def50200dc6c27266da1a5e17e80aae1d7b51097702e3fd3c3647e52b1e0df73595eaea9f28a042b56591a3d7d4bdddd48f7d5ca571dd54aec34dbb3f64302acf6bf0ac2c6b1d094aaa1241773dd6bcc4f9a9bcf2419b259188e68242821c82c17b8521d4ab799454b2ae38851a8564685496f9a63dcc27caba9bfbf573670fb758e4b9469eeb02257a44076f35cbe3834998e9c35b8a0fff9696c3a69e7c5d4696c2623fdb7fbe2f3344c0929bba3bd2dc343ec66c00b815feb9aef2300ef4c16c6277be698fa341d589b12aaeb6742fc854a88f667cb6b5f884565c9f4948824f8d0faa43ada93420bc50f21116ec8a411a1670f2bfceb2afe4796cb6d65e119da75950cdb642581ff0ad3aedd968a1733cc54ffab5311546d164e176af3594de5e8812013eecd11a60fb330e677dd1e1350ee4bd4190f26ded1dccfa334e64498e1a195132c3f9d2d144cc2b7fe6af3989896dd7911558a224292bd74fd1fa0ae927ddd5ff55b1b0b6ed8990469b42602ba23473650e874281b79ea290fcc0326a779deab0627e3c07a8314a7cc4663be8e75fce2dc7e7630caed086e9f372a8f9fff70509f4d0299e2f0d7b996b0a07fb8060e328860f01b27b8d97baa3c8786168c104330332f0a759b14072b6175f391370b9d46dc456989cb7aabc418e3189265e5ab446436"
client_id = "981d1e994f524fd585e727fc0e937e49"
client_secret = "277d674e78806c820a11ad373dc3ef62f0d394bfaf6f6f0b9421cb8329ac3975"
code_challenge = "Q8ZHhe2d4N2MDm1dFRd1VEv2Mk60KBgc4ABXdLdSyc0JA3PEIFQoXL4_qztfWSL_Q4XqMm9j_ppHKVQbUjIio1n0dOmRvxCOFibOSx8Tv8LfTtPsoRyxkCRtQaU9Lf_"
code_verifier = code_challenge

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjliMTg1ZTI0M2Y1NWNhN2FhNDUzZTRjZWZiZjVjMjVlZDVhZTFmNjk2MmVkOGNmMjdlYzZiNDZmNjU5YjlhMzdmYjEwOTYyMjMyNjkzNzc5In0.eyJhdWQiOiI5ODFkMWU5OTRmNTI0ZmQ1ODVlNzI3ZmMwZTkzN2U0OSIsImp0aSI6IjliMTg1ZTI0M2Y1NWNhN2FhNDUzZTRjZWZiZjVjMjVlZDVhZTFmNjk2MmVkOGNmMjdlYzZiNDZmNjU5YjlhMzdmYjEwOTYyMjMyNjkzNzc5IiwiaWF0IjoxNjExNDU1OTkxLCJuYmYiOjE2MTE0NTU5OTEsImV4cCI6MTYxNDEzNDM5MSwic3ViIjoiMTE0NDY4MDQiLCJzY29wZXMiOltdfQ.Yfv1NeMMb-ETJ8sxBV56ewi82PYASIJ7gKjr-C_EFJQAyK7bvcoc-FMbXy2ib70889vSr-FUY45OnvR-ao_5dhOcwqe8NaIRlg6ohbdU-ScUhyfwHaYFiHK5RjH87HssNPvxTEi9kNUBlMW0MZyEq4jK5lzLYR1Z0ai6WREVVVsbpPaTjTs9BebtuVYHyAhxMvJOTggjLW388JhvEKve_3WDbpgALK8qZ8tCa0JjZslxL_OKf1p7y4OSwZ8uYKn5dCkgUlWF5QOJmH6UGOwgtxPUMciWo33B5zSlmcP4w5LC39cwTrQ0XfucMRZRJzTU4CReeurDX29dpBAY8hp2Sw"
refresh_token = "def502008f64ae4fb80db63135c23d86ad4b72b39c76875cec298868e2f02240a37b34790be081b007f3deaf7f95a08cc4de0764abfdb2faca837083b0edc1e9ce7ceabe720d09b43cafb2e2a9e9d0319658e43d4599bde2968d51857e895cc3ce231cce150a036f250f1371677028ca5806772178a42c1e4bed1ce8c5f76a1c3c88074883af4082dc68bfcfc78d6b8b6f5951fc06f28ce51a36e63ae6e5bbfb2eaf3673fb5326e98f1862e7b9f979944c6ae3bb93f95b28ac20a7822b4a9002ac102c5fa35a8fbc047ea4f4a1855eb042769c7d5518fd29918a0f95fd2e38f50755a309267d41056899c932de6b3a16e83b07cf70d7276af36a6fdbdd9c4009021fb2efe61aae4758e23451d090a1aaf77118fa972d646c6057e499a16e5528447fdb3ff45540158067b68df709898d48f9f5e06152b3b7095bdb04b8a885ecab6e230d75b159ec7e598a960663e8470bebc7d36da32a805fe0a26eecf6fcb703f748c14768bf861462f93895876afe6680bdd14c89eb8e847aecf35231ffc79d3a48f63b031e7f02"
# expires in 2678400 from 6:41pm 1/23/2021 (31 days)

def get_auth() :
    auth_url = ("https://myanimelist.net/v1/oauth2/authorize"
    "?response_type=code"
    "&client_id=" + client_id +
    "&code_challenge=" + code_challenge +
    "&state=1")

    print(auth_url)

def complete_auth():
    url = "https://myanimelist.net/v1/oauth2/token"
    data = {
        "client_id"    : client_id,
        "client_secret" : client_secret,
        "code"          : auth_code,
        "code_verifier" : code_verifier,
        "grant_type"    : "authorization_code"
    }
    response = requests.post(url, data)
    print(response.status_code)
    print(response.text)

def test_auth():
    url = "https://api.myanimelist.net/v2/users/@me"
    response = requests.get(url, headers={"Authorization" : "Bearer " + access_token})
    print(response.status_code)
    print(response.text)
    
# get_auth()
# complete_auth()
test_auth()
