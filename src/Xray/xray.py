import json, requests, os
from ntpath import join
from datetime import datetime

class Xray:
    def authentication(self) -> str:
        json_data = json.dumps({'client_id': self.config.xray_client_id(), 'client_secret': self.config.xray_client_secret()})
        resp = requests.post(f'{self.config.xray_api()}/authenticate', data=json_data, headers={'Content-Type':'application/json'})
            
        if resp.status_code == 200:
            return 'Bearer ' + resp.json()
        else:
            print(resp.json())
            print("Authentication error: {}".format(resp.status_code))

    def getTestPlan(self, key: str):
        try:
            print("\n------------------------------------------------------------------------------")
            print("A função getTestPlan está sendo executada!")
            if self.config.debug():
                print("A função recebeu key {}".format(key))
            
            json_data = f'''
                {{
                    getTestPlans(jql: "key = '{ key }'", limit: 1) {{
                        results {{
                            issueId
                        }}
                    }}
                }}
            '''

            resp = requests.post(
                f'{self.config.xray_api()}/graphql',
                json={
                    'query': json_data
                },
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': Xray.authentication(self)
                },
            )

            if resp.status_code != 200:
                print("Infelizmente ocorreu um erro ao obter o issueId do TestPlan")
                print("Código de erro {}".format(resp.status_code))
                print("------------------------------------------------------------------------------")
            else:
                if self.config.debug():
                    print(json.dumps(resp.json(), indent=4))
                print("------------------------------------------------------------------------------")
                return resp.json().get('data').get('getTestPlans').get('results')[0].get('issueId')
        except Exception as error:
            print("Ocorreu um erro na classe Xray na função getTestPlan com a seguinte mensagem:")
            print(error)
            print("------------------------------------------------------------------------------")
        
    def addTestExecutionsToTestPlan(self, issueId: str, testExecIssueId: str):
        try:
            print("\n------------------------------------------------------------------------------")
            print("A função addTestExecutionsToTestPlan está sendo executada!")
            if self.config.debug():
                print("A função recebeu issueId {} e testExecIssueId {}".format(issueId, testExecIssueId))

            json_data = f'''
                mutation {{
                    addTestExecutionsToTestPlan(
                        issueId: "{ issueId }",
                        testExecIssueIds: ["{ testExecIssueId }"]
                    ) {{
                        addedTestExecutions
                        warning
                    }}
                }}
            '''

            resp = requests.post(
                f'{self.config.xray_api()}/graphql',
                json={
                    'query': json_data
                },
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': Xray.authentication(self)
                },
            )

            if resp.status_code != 200:
                print("Infelizmente ocorreu um erro ao adicionar os resultados ao Plano de Teste")
                print("Código de erro {}".format(resp.status_code))
                print("------------------------------------------------------------------------------")
            else:
                if self.config.debug():
                    print(json.dumps(resp.json(), indent=4))
                print("------------------------------------------------------------------------------")
        except Exception as error:
            print("Ocorreu um erro na classe Xray na função addTestExecutionsToTestPlan com a seguinte mensagem:")
            print(error)
            print("------------------------------------------------------------------------------")

    def importExecutionCucumber(self, report_names, key: str = None):
        try:
            print("A importação dos resultados do testes estão a ser enviados.")
            print("Aguarde um momento...")
            print("------------------------------------------------------------------------------")
            print("A função importExecutionCucumber está sendo executada!")
            if self.config.debug():
                print("A função recebeu key {}".format(key))

            resp = requests.post(f'{self.config.xray_api()}/import/execution/cucumber', 
                data = open(self.config.cucumber_path() + f'/{report_names[1]}.json', 'rb'),
                params = { 
                    'projectKey': self.config.project_key(),
                },
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': Xray.authentication(self)
                }
            )

            if key != None:
                issueId = Xray.getTestPlan(self, key)
                Xray.addTestExecutionsToTestPlan(self, str(issueId), str(resp.json().get('id')))
            
            if resp.status_code == 200:
                print("O arquivo '{}' foi gerado!".format(join(self.config.cucumber_path(), f'{report_names[1]}.json')))
                if self.config.debug():
                    print(json.dumps(resp.json(), indent=4))
                splitInfo = resp.json().get('self').split('/')
                print("Resultados encontram-se em {}//{}/browse/{}".format(splitInfo[0], splitInfo[2], resp.json().get('key')))
                print("------------------------------------------------------------------------------")
                return resp.json().get('id')
            else:
                print("Infelizmente ocorreu um erro no envio dos resultados")
                print("Código de erro {}".format(resp.status_code))
                print(json.dumps(resp.json(), indent=4))
                print("------------------------------------------------------------------------------")
        except Exception as error:
            print("Ocorreu um erro na classe Xray na função importExecutionCucumber com a seguinte mensagem:")
            print(error)
            print("------------------------------------------------------------------------------")