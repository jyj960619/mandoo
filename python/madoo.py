import pandas as pd 
data = pd.read_excel('mandoo_management.xlsx', sheet_name='Sheet1');
# print(data);
# print(data['이름']);

# 근무시간 컬럼 추가
data['근무시간'] = data['퇴근시간'] - data['출근시간'];
# 근무시간 컬럼 추가
data['시간당 만두'] = data['만두생산'] / data['근무시간'];

data = data.sort_values(by=['시간당 만두','근무시간'], ascending=[False, False]);

print(data);

data.to_excel('result.xlsx', sheet_name = '만두공장');