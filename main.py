from qtrade.questrade import Questrade
from qtrade.utility import get_access_token_yaml
from qtrade.formating import simplify_quote
import os.path

token_yaml_file = 'access_token.yml'

if os.path.isfile(token_yaml_file):
    qt = Questrade(token_yaml=token_yaml_file)
    qt.refresh_access_token()
else:
    qt = Questrade(access_code="3lOhWIPbXKWUZQhDVgkP8u2Lioy_nQCW0")


results = qt.get_quote(['MSFT', 'GOOGL'])

df = simplify_quote(results)

print(df)
#print(df.to_html(justify='left'))