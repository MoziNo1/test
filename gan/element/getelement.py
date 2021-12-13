class Summary:

        
        # 证件到期提醒弹框确定
        end_card_info = '//*[@id="layui-layer5"]/div[3]/a'
        # 证件到期提醒页面刷新提示框
        end_card_info_refresh = '//*[@id="layui-layer1"]/div[3]/a'
        # 业务管理模块
        business_management = '//span[text()="业务管理"]'
        # 个人业务申请点击按钮
        personal_business_applications = '//a[text()="个人业务申请"]'
        # 证件号码输入框
        id_card_input = '//*[@id="prjApplyCustomForPerCtrl"]/form/div/div/div[2]/div[2]/input'
        # 查询客户信息按钮
        cust_personal_search = '//*[@id="prjApplyCustomForPerCtrl"]/form/div/div/div[2]/div[3]/button[1]'
        # 选择要申请业务的客户
        individual_customer_quota = '//*[@id="prjApplyCustomForPerCtrl"]/div[3]/div[1]/table/tbody/tr[3]/td'
        # "业务申请按钮"
        bussiness_apply_button = '//*[@id="prjApplyCustomForPerCtrl"]/div[2]/button'
        # 选择业务申请模式，判断是额度下申请还是单笔单批
        business_module = '//*[@id="prjApplyCustomForComCtrl"]/form/div/div/div/div/select'
        # 单笔单批
        business_module_single = '//*[@id="prjApplyCustomForComCtrl"]/form/div/div/div/div/div[1]/dl/dd[4]'
        # 获取变化的id值
        business_change_id = '//*[@id="projectprojectapplycreditPersonal"]/div/div/div[1]/div[1]'

        # apply_quota = '//*[@id="grid162199255656012"]/table/tbody/tr[4]/td[2]'

        # 产品名称选输入框
        product_name_input = ['//*[@id="companyPro"]/div[2]/input', '//*[@id="prjApplyCustomForComCtrl"]/div/div[1]/div[2]/input']
        # 单笔单批时，一级产品加号
        one_product_plus = '//*[@jf-tree="selector.tree"]/ul/li/span[1]'
        # 二级产品加号
        second_product_plus = '//*[@jf-tree="selector.tree"]/ul/li/ul/li[2]/span[1]'
        # 三级产品加号
        third_product_plus = '//*[@jf-tree="selector.tree"]/ul/li/ul/li[2]/ul/li/span[1]'
        # 个人政策性贷款
        policy_product = '//*[@jf-tree="selector.tree"]/ul/li/ul/li[2]/ul/li/ul/li/a/span[2]'
        # 产品名称
        product_name = ['//span[@class="node_name"]', '//*[@jf-tree="selector.tree"]/ul/li/ul/li[2]/ul/li/ul/li/a/span[2]']
        # 确认按钮
        confirm_button = ['//*[@id="prjApplyCustomForComCtrl"]/div/div[3]/button[1]/i', '//*[@id="prjApplyCustomForComCtrl"]/div/div[2]/button[1]/i']

        # 进入下一界面

        # 反显的业务编号
        prj_numb = '//*[@id="prjNumb"]'
        # 申请金额输入框
        apply_amount = '//*[@id="aplyAmt"]'
        # 业务起始日期输入框
        business_start_date = '//*[@id="prjStDt"]'
        # 业务起始日期输入框的确定按钮
        business_start_date_button = '//*[@id="layui-laydate1"]/div[2]/div/span[2]'
        # 业务结束日期输入框
        business_end_date = '//*[@id="prjCoDt"]'
        # 业务日期向后调整按钮
        next_date_adjust = '//*[@id="layui-laydate2"]/div[1]/div[1]/i[4]'
        # 业务结束日期输入框的确定按钮
        business_end_date_button = '//*[@id="layui-laydate2"]/div[2]/div/span[2]'
        # 多次放款，一次性放款选择按钮
        lending_options = '//*[@id="dsbrMtdCdDiv"]/div[2]/div[1]/span'
        # 执行利率输入框
        execution_rate = '//*[@id="intrtRate"]'
        # 申请期限输入框
        application_period = '//*[@id="aplyDdln"]'
        # 当前页面第一个保存按钮
        save_button = '//*[@ng-if="item.show"]/div/div/form/div[3]/button'
        # 选择审批人
        select_person_button = '//*[@id="td_per"]/div[2]/i'
        # 可审批人列表,此处默认选择第一个人
        approver_list = '//*[@class="level2"]/span[2]'
        # 审批人列表中的提交按钮
        approver_list_button = '//a[text()="提交"]'
        # 同意按钮
        business_admit_button = '//span[text()="同意"]'
        # 审批意见输入款
        approval_opinions = '//*[@id="tr_comment"]/div[2]/textarea'
        # 最后的提交按钮
        finally_submit_button = '//*[@id="dontClick"]'
        # 退出登录
        sign_out = '/html/body/div[1]/div/div[1]/div[2]/div/ul/li[1]/a/i'

        # 为了获取下一个审批人的登录名,获取下面的元素
        next_login_name = '//div[@jf-tree="pertree"]/ul/li[1]/ul/li[1]/ul/li[1]/a/span[2]'

        # 下一审批人的界面
        # 从待办列表中获取业务
        # business_data_list = login_read('B', '../../146/data/quota.xlsx')
        # print(business_data_list)
        # print(data_list[6])
        # cust_name = business_data_list[0]
        # business_to_do_list = '//*[@class="module_box"]/div/div/table/tbody/tr/td[text()="{}"]'.format(cust_name)

        final_admit_button = '//span[text()="同意"]'

        a = '//*[@id="td_per"]/div[2]/input'
        # 退回指定步骤
        back = '//span[text()="退回指定步骤"]'

        # 额度元素
        # 额度管理模块
        # quota_data_list = login_read('B', '../../146/data/quota.xlsx')
        # print(quota_data_list)
        quota_management = '//span[text()="额度管理"]'
        # 额度申请
        quota_apply = '//a[text()="额度申请"]'
        # 新增额度按钮
        quota_new_button = '//*[@id="pcrAplyPcslmtAplyList"]/div/div/div[2]/button[1]'
        # 个人客户按钮
        quota_personal_cust_button = '//li[text()="个人客户"]'
        # 额度申请客户名称输入框
        quota_cust_name_input = '//*[@id="pcrAplyPcslmtItt"]/div/div[2]/div/div[2]/form/div/div[1]/div[1]/div/input'
        # 根据客户名称查询按钮
        quota_cust_search_button = '//*[@id="pcrAplyPcslmtItt"]/div/div[2]/div/div[2]/form/div/div[2]/button[1]'
        # 选中所申请额度的客户
        quota_select_cust = []
        for i in range(1, 11):
                n = '//*[@id="pcrAplyPcslmtItt"]/div/div[2]/div[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[{}]/td[2]'.format(i)
                quota_select_cust.append(n)
        # 额度申请的第一个确认按钮
        quota_first_confirm_button = '//*[@id="pcrAplyPcslmtItt"]/div/div[2]/div/div[2]/div[1]/button'
        # 专项额度输入框
        quota_special_input = '//*[@ng-include="item.url"]/div/div/div[1]/div[12]/div[2]/input'
        # 额度有效期
        quota_effective_date = '//*[@ng-include="item.url"]/div/div/div[1]/div[15]/div[2]/input'
        # 额度期限单位下拉框
        quota_date_select = '//*[@ng-include="item.url"]/div/div/div[1]/div[16]/div[2]/div[1]/div/input'
        # 下拉框中的年单位
        quota_date_select_year = '//*[@ng-include="item.url"]/div/div/div[1]/div[16]/div[2]/div[1]/dl/dd[3]'
        # 担保方式选择
        quota_Guaranteed_method_select = '//span[text()="信用"]'
        # 担保方式说明输入
        quota_Guaranteed_method_input = '//*[@ng-include = "item.url"]/div/div/div[1]/div[20]/div[2]/textarea'
        # 额度申请保存按钮
        quota_apply_save_button = '//button[@ng-click="saveLmtPln()"]'
        # 额度明细新增按钮
        quota_detail_new_apply_button = '//button[@ng-click="addLmtDtl()"]'
        # 额度类型输入框，其含有下拉框
        quota_type_input = '//*[@ng-include = "item.url"]/div/div[3]/div/form/div/div[2]/div[1]/div[2]/div[1]/div/input'
        # 额度类型输入框中的专项额度
        quota_type_input_special = '//dd[text()="专项额度"]'
        # 额度分项输入框，其含有下拉框
        quota_item_input = '//*[@ng-include = "item.url"]/div/div[3]/div/form/div/div[2]/div[2]/div[2]/input[2]'
        # 一级加号展开
        quota_first_plus_expand = '//div[@jf-tree="selector.tree"]/ul[1]/li/span'
        # 二级加号展开
        quota_second_plus_expand = '//div[@jf-tree="selector.tree"]/ul[1]/li/ul/li[2]/span'
        # 额度分项中的个人类额度
        quota_item_input_personal_quota = '//span[text()="个人政策性贷款额度"]'
        # 分项金额输入框
        quota_item_cash_input = '//*[@ng-include = "item.url"]/div/div[3]/div/form/div/div[2]/div[4]/div[2]/input'
        # 循环额度下拉框选择
        quota_loop_select = '//select[@name="rvlInd"]'
        # 额度明细的保存按钮
        quota_detail_save_button = '//button[@ng-click="saveLmtDtlInfo()"]'
        # 额度申请时的同意按钮
        quota_first_admit_button = '//span[text()="同意"]'
        # 额度申请选人按钮
        quota_select_person_button = '//i[text()="选人"]'
        # 额度申请下一审批人
        quota_apply_next_Approval_button = '//div[@jf-tree="pertree"]/ul/li[1]/ul/li[1]/ul/li[1]/span[2]'
        # 为了获取下一个节点审批人
        quota_next_login_name = '//div[@jf-tree="pertree"]/ul/li[1]/ul/li[1]/ul/li[1]/a/span[2]'
        # 额度申请时，选人界面的提交
        quota_select_person_submit_button = '//a[text()="提交"]'
        # 额度申请审批意见输入框
        quota_apply_opinion_input = '//*[@id="tr_comment"]/div[2]/textarea'
        # 额度申请最终提交按钮
        quota_finally_submit_button = '//button[@ng-click="submitWorkflow()"]'
        # quota_cust_name = quota_data_list[0]
        # quota_to_do_list = '//*[@class="module_box"]/div/div/table/tbody/tr/td[text()="{}"]'.format(quota_cust_name)

        # 合同申请
        # 合同管理模块
        contract_management = '//span[text()="合同管理"]'
        # 新增合同
        contract_new_contract = '//a[text()="新增合同"]'
        # 点击过后取消悬浮框
        contract_fast = '//*[@id="demoSingle"]'
        # 新增合同客户名称输入框
        contract_cust_name_input = '//*[@id="rtlcontractmaincontractcontApplyqueryProject"]/div/form/div/div[1]/div[1]/div/input'
        # 新增合同业务编号输入框
        contract_prj_numb_input = '//*[@id="rtlcontractmaincontractcontApplyqueryProject"]/div/form/div/div[1]/div[2]/div/input'
        # 新增合同中的查询按钮，过滤客户信息
        contract_search_button = '//button[@ng-click="projectList.search()"]'
        # 点击所要制作的合同,获取变化的id
        contract_change_id = '//*[@ng-controller="contApplyCtrl"]/div[2]/div[1]'
        contract_select_button = '//*[@id="rtlcontractmaincontractcontApplyqueryProject"]/div/div[2]/div[1]/table/tbody/tr[3]/td[2]'

        # 制作合同按钮
        contract_make_button = '//button[@ng-click="checkBlackCustmor()"]'
        # 纸质合同编号输入框
        contract_paper_id_input = '//*[@id="ctrPcrNumb"]'
        # 贷款投向输入框，通过点击获取下拉列表
        contract_loan_invested = '//*[@id="idyTpCd"][3]'
        # 贷款投向中的第一个加号展开按钮
        contract_loan_invested_first_plus = '//div[@jf-tree="selector.tree"]/ul[1]/li[1]/span'
        # 贷款投向中的第二个加号展开按钮
        contract_loan_invested_second_plus = '//div[@jf-tree="selector.tree"]/ul[1]/li[1]/ul[1]/li[1]/span'
        # 贷款投向具体信息
        contract_loan_invested_info = '//div[@jf-tree="selector.tree"]/ul[1]/li[1]/ul[1]/li[1]/ul/li/a/span[2]'
        # 贷款用途详细说明
        contract_loan_invested_detail_input = '//*[@id="loanUseDtlCmnt"]'
        # 是否为新增贷款
        contract_newloan_judge = '//*[@id="wthrNewDiv"]/div[2]/div[1]/div/input'
        # 选择贷款为新增
        contract_newloan = '//*[@id="wthrNewDiv"]/div[2]/div[1]/dl/dd[3]'
        # 合同申请信息界面第一个保存按钮
        contract_first_save_button = '//div[@ng-if="item.show"][1]/div/div/div/div/button'
        # 合同申请信息界面第二个保存按钮
        contract_second_save_button = '//div[@ng-if="item.show"][2]/div/div/div/div/button'
        # 表头为了定位到以下元素
        contract_tab = '//*[@id="rpmdCdDiv"]/div[2]/div[1]/div/input'
        # 放款账户账号输入框
        contract_lending_account_input = '//*[@id="wePyAcctno"]'
        # 还款账号输入框
        contract_repay_account_input = '//*[@id="coRepAccno"]'

        # 贴息贷款选择
        contract_discount_loan = '//*[@id="wthrSsonintDiv"]/div[2]/div[1]/div/input'
        contract_discount_loan_true = '//*[@id="wthrSsonintDiv"]/div[2]/div[1]/dl/dd[4]'
        # 合同申请信息界面第三个保存按钮
        contract_third_save_button = '//div[@ng-if="item.show"][3]/div/div/div/div/button'
        # 合同申请信息中的贷款试算按钮
        contract_Loan_trial_calculation_button = '//div[@ng-controller="contRepyPlnCtrl"]/div[2]/button'
        # 贷款投向地区
        loan_area_province = '//*[@id="dktxdq"]/div/div[1]/div/div/input'
        loan_area_province_select = '//*[@id="dktxdq"]/div/div[1]/div/dl/dd[3]'
        loan_area_city = '//*[@id="dktxdq"]/div/div[2]/div/div/input'
        loan_area_city_select = '//*[@id="dktxdq"]/div/div[2]/div/dl/dd[3]'
        loan_area_line = '//*[@id="dktxdq"]/div/div[3]/div/div/input'
        loan_area_line_select = '//*[@id="dktxdq"]/div/div[3]/div/dl/dd[3]'
        # 合同申请的第四个保存按钮
        contract_fouth_save_button = '//*[@id="xxView"]/div/button'
        # 合同申请信息界面中的同意按钮
        contract_admit_button = '//*[@id="redioIds"]/div/i'
        # 合同申请信息界面中的选人按钮
        contract_select_person_button = '//*[@id="td_per"]/div[2]/i'
        # 选人界面中的第一个审批人
        first_approver_button = '//div[@jf-tree="pertree"]/ul[1]/li[1]/ul[1]/li[1]/ul/li[1]/span[2]'
        # 选人界面中的审批人登录名
        contract_next_login_name = '//div[@jf-tree="pertree"]/ul[1]/li[1]/ul[1]/li[1]/ul/li[1]/a'
        # 选人界面的审批按钮
        # contract_approver_submit_button = '//a[text()="提交"]'
        # 合同申请信息界面中的审批意见输入框
        # contract_opinion_input = '//*[@id="tr_comment"]/div[2]/textarea'
        # 合同申请信息界面中的最终提交按钮
        # contract_last_submit_button = '//*[@id="dontClick"]'
        # 从待办列表中去要审批的合同
        # contract_to_do_list = '//*[@class="module_box"]/div/div/table/tbody/tr/td[text()="{}"]'.format(contract_data_list[0])
        # 审批人界面的同意按钮



        # 放款管理模块

        loan_request_management = '//*[text()="放款管理"]'
        # 放款申请
        loan_request_button = '//a[text()="放款申请"]'
        # 客户名称输入框
        loan_request_cust_name_input = '//*[@id="payDsbrCdAplylist"]/div/form/div/div[1]/div[1]/div/input'
        # 合同编号输入框
        loan_request_ctr_numb_input = '//*[@id="payDsbrCdAplylist"]/div/form/div/div[1]/div[2]/div/input'

        # 过滤客户信息查询按钮
        loan_request_search_button = '//*[@id="payDsbrCdAplylist"]/div/form/div/div[2]/button[1]'
        # 获取变化的id值
        loan_request_change_id = '//div[@ng-controller="payDsbrCdAplyCtrl"]/div[2]/div1'
        # 点击所要进行的放款
        loan_request_select_cust = '//div[@ng-controller="payDsbrCdAplyCtrl"]/div[2]/div[1]/table/tbody/tr[3]/td[4]'
        # 点击发起按钮
        loan_request_launch = '//*[@id="payDsbrCdAplylist"]/div/div[1]/button'
        # 当前页面的第一个保存按钮
        loan_request_first_save_button = '//*[@id="payInfoListlist"]/div/div[2]/div/div[2]/div/div[1]/div/div/div/div/button'
        # 弹出框中的确认按钮
        loan_request_pop_up_box = '//a[text()="确定"]'
        # 当前页面的第二个保存按钮
        loan_request_second_save_button = '//*[@id="payInfoListlist"]/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/button'
        # 当前页面的第三个保存按钮
        loan_request_third_save_button = '//*[@id="payInfoListlist"]/div/div[2]/div/div[2]/div/div[3]/div/div/div/div/button'
        # 贷款试算按钮
        loan_request_calc_button = '//*[@id="payInfoListlist"]/div/div[2]/div/div[2]/div[1]/div[4]/div/div/div[2]/div/button/i'
        # 放款申请的第一个按钮
        loan_request_first_admit_button = '//span[text()="同意"]'
        # 放款申请的选人按钮
        loan_request_select_person_button = '//*[@id="td_per"]'
        # 选择审批人
        loan_request_choose_person = '//div[@jf-tree="pertree"]/ul/li[1]/ul/li[1]/ul/li[1]/span[2]'
        # 获取下一节点审批人
        loan_request_next_login_name = '//div[@jf-tree="pertree"]/ul/li[1]/ul/li[1]/ul/li[1]/a/span[2]'
        # 选人界面的提交按钮
        loan_request_first_submit_button = '//a[text()="提交"]'
        # 审批意见输入框
        loan_request_approval_input = '//*[@id="tr_comment"]/div[2]/textarea'
        # 最后的提交按钮
        loan_request_last_submit_button = '//*[@id="dontClick"]'
        # 从待办列表中获取放款申请额任务
        # loan_to_do_list = '//*[@class="module_box"]/div/div/table/tbody/tr/td[text()="{}"]'.format(loan_data_list[0])