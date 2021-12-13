import business_apply
import quota_apply
import New_contracts
import os
import time

from gan.service.loan_request import LoanRequest

basicurl = ['http://172.21.1.146:8180/xyjk-erp-app-pc/login', 'http://172.21.4.34:8080/xyjk-erp-app-pc/login']


# a = quota_apply.QuotaApply(basicurl[0])
# a.quota_first_apply()
# time.sleep(2)

b = business_apply.Business(basicurl[0])
business_judge = b.business_first_apply()
# prj_number = b.prj_numb
# print(business_judge)
if business_judge == 1:
    time.sleep(2)
    c = New_contracts.NewContracts(basicurl[0])
    end_flag = c.contracts_first_apply()
    if end_flag == 1:
        time.sleep(2)
        d = LoanRequest(basicurl[0])
        d.loan_first_apply()


